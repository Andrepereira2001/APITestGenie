import os
import argparse
from dotenv import load_dotenv
import generate
import utils

PETSHOP = {
    "api": "https://petstore.swagger.io/v2/swagger.json",
    "requirement": "./requirements/pet_shop.txt"
}

CATFACT = {
    "api": "https://catfact.ninja/docs?api-docs.json",
    "requirement": "./requirements/cat_fact.txt"
}

def main():
    parser = argparse.ArgumentParser(description="Choose API: catFact or petShop")
    parser.add_argument("api", choices=["catFact", "petShop"], help="API to use")
    args = parser.parse_args()

    print("Welcome to APITestGenie!")

    load_dotenv()  # Load environment variables from .env
    api_key = os.getenv("OPENAI_API_KEY")

    generate_instance = generate.Generate(api_key=api_key)

    if args.api == "catFact":
        config = CATFACT
    else:
        config = PETSHOP

    requirement = utils.read_file(config["requirement"])
    api_spec = utils.fetch_json(config["api"])
    
    generation = generate_instance.generate_test_with_chat_prompt(user_story=requirement, api_specification=api_spec)
    _, _, test = generate_instance.parse_generation(generation=generation)

    utils.write_file("./test_output/test.ts", test)

if __name__ == "__main__":
    main()