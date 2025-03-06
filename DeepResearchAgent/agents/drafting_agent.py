from langchain_groq import ChatGroq
from utils.prompt_templates import DRAFTING_PROMPT

def draft_answer(context):
    llm = ChatGroq(model_name="llama3-8b-8192")
    prompt = DRAFTING_PROMPT.format(context=context)
    response = llm.invoke(prompt)
    return response.content
