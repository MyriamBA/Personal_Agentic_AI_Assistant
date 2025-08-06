from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from dotenv import load_dotenv
import os
import requests
from langchain.agents import Tool
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_experimental.tools import PythonREPLTool
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from langchain_core.callbacks import CallbackManagerForToolRun
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from typing import Dict, Type


load_dotenv(override=True)

serper = GoogleSerperAPIWrapper()

async def playwright_tools():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    return toolkit.get_tools(), browser, playwright


def get_file_tools():
    toolkit = FileManagementToolkit(root_dir="sandbox")
    return toolkit.get_tools()

class EmailInput(BaseModel):
    """Input schema for the email tool."""
    subject: str = Field(description="The subject line of the email")
    html_body: str = Field(description="The HTML content of the email body")

class SendEmailTool(BaseTool):
    """Tool for sending emails via SendGrid."""
    
    name: str = "send_email"
    description: str = """
    Send an email with the given subject and HTML body.
    Use this tool when you need to send emails to communicate with users or send reports.
    """
    args_schema: Type[BaseModel] = EmailInput
    
    def _run(
        self, 
        subject: str, 
        html_body: str, 
        run_manager: CallbackManagerForToolRun = None
    ) -> Dict[str, str]:
        """Execute the email sending operation."""
        try:
            sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
            from_email = Email("benahmeed.myriam@gmail.com")  
            to_email = To("benahmeed.myriam@gmail.com") 
            content = Content("text/html", html_body)
            mail = Mail(from_email, to_email, subject, content)
            
            response = sg.client.mail.send.post(request_body=mail.get())
            
            return {
                "status": "success",
                "message": f"Email sent successfully with subject: '{subject}'",
                "status_code": response.status_code
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to send email: {str(e)}"
            }



async def other_tools():
    file_tools = get_file_tools()
    email_tool = SendEmailTool()

    tool_search =Tool(
        name="search",
        func=serper.run,
        description="Use this tool when you want to get the results of an online web search"
    )

    wikipedia = WikipediaAPIWrapper()
    wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)

    python_repl = PythonREPLTool()
    
    return file_tools + [ tool_search, python_repl, wiki_tool, email_tool]

