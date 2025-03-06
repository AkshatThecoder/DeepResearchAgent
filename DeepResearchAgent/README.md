# Deep Research AI Agentic System

This project is a dual-agent system using LangGraph (via LangChain) to perform deep web research and draft final reports.

- **Research Agent:** Uses Tavily to gather web content.
- **Drafting Agent:** Uses Llama 3 (hosted by Groq) to summarize and format the response.

## System Flow
1. Input query (research topic).
2. Research agent collects data using Tavily.
3. Drafting agent summarizes the data using Groq (Llama 3).

## Setup Instructions
1. Create a `.env` file (see `.env.example`).
2. Now put your TAVILY_API_KEY and GROQ_API_KEY in your `.env` file
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run the system:
    ```
    python main.py
    ```

## No OpenAI or Anthropic needed ✅
