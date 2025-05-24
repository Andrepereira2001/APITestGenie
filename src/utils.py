# Helper functions
import requests

def read_file(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(filepath: str, content: str):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

def fetch_json(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()