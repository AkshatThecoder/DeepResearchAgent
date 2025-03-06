import os
from dotenv import load_dotenv
from agents.research_agent import fetch_research_data
from agents.drafting_agent import draft_answer

load_dotenv()

def deep_research_pipeline(query):
    research_data = fetch_research_data(query)
    
    print("\n Research Data Collected:\n")
    print(research_data[:500] + "...")

    final_response = draft_answer(research_data)
    
    print("\nFinal Response:\n")
    print(final_response)

if __name__ == "__main__":
    query = input("Enter your research topic: ")
    deep_research_pipeline(query)
