import os
from dotenv import load_dotenv
import generate

PETSTORE = "https://petstore.swagger.io/v2/swagger.json"

def main():
    print("Welcome to LangChain Test Generator!")
    load_dotenv()  # Load environment variables from .env
    api_key = os.getenv("OPENAI_API_KEY")
    generate_instance = generate.Generate(api_key=api_key)
    
    generate_instance.generate_test("What is the capital of France?")

if __name__ == "__main__":
    main()