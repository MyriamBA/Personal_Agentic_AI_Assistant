# Personal Agentic AI Assistant

## Project Overview
This project implements a personal assistant powered by an agentic AI. It can help you with your daily personal tasks, such as browsing the web and sending emails. It is built using **LangGraph** and follows an **Evaluator/Worker** design pattern from [Anthropic](https://www.anthropic.com/engineering/building-effective-agents). The assistant's capabilities are extended through the integration of various **tools**. 

<img src="images/sidekick.png" alt="Description" width="500"/>

## Main Tools & Technologies

This agentic AI system is built using the following core tools:

- **LangGraph**: for building agentic workflows.
- **LangSmith**:  for tracing and monitoring.
- **OpenAI ChatGPT-4-o-mini**: as the main LLM for task completion and planning.
- **Gradio**: a simple UI for interacting with the personal assistant.

## Agent Tools
The worker agent uses the following tools:
1. [PlayWright Browser ToolKit](https://python.langchain.com/docs/integrations/tools/playwright/) : for computer and Browser use.
2. [Google Serper](https://python.langchain.com/docs/integrations/tools/google_serper/) : for accessing Google Search.
3. [SendGrid Email API](https://sendgrid.com/en-us) : for sending emails.

## Learning Resources
1.  [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
2.  [The complete Agentic AI Engineering Course](https://www.udemy.com/course/the-complete-agentic-ai-engineering-course/?couponCode=KEEPLEARNING)
   

