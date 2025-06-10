import os
import argparse
from dotenv import load_dotenv
import generate
import utils

PETSHOP = {
    "api": "https://petstore.swagger.io/v2/swagger.json",
    "user_story": "./user_stories/pet_shop.txt"
}

CATFACT = {
    "api": "https://catfact.ninja/docs?api-docs.json",
    "user_story": "./user_stories/cat_fact.txt"
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

    user_story = utils.read_file(config["user_story"])
    api_spec = utils.fetch_json(config["api"])
    
    generation = generate_instance.generate_test_with_chat_prompt(user_story=user_story, api_specification=api_spec)
    utils.write_file("./test_output/generation.txt", generation)

    _, _, test = generate_instance.parse_generation(generation=generation)
    utils.write_file("./test_output/test.ts", test)

    print("Test generated, you may now execute it!")

if __name__ == "__main__":
    main()