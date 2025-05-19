# Handles interactions with the LLM via LangChain

from langchain.llms import OpenAI
from langchain.prompts import ChatPromptTemplate

class Generate:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.llm = OpenAI(openai_api_key=api_key)

    def generate_test(self, prompt: str) -> str:
        # Call the LLM to generate a test based on the prompt
        return self.llm(prompt)

    def generate_test_with_chat_prompt(self, system_prompt: str, user_prompt: str) -> str:
        """
        Generates a test using ChatPromptTemplate with system and user prompts.
        """
        chat_prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", user_prompt)
        ])
        formatted_prompt = chat_prompt.format()
        return self.llm(formatted_prompt)