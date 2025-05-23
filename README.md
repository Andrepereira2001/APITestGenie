# APITestGenie
Replication package for API Test Genie, an LLM based approach to generate integration tests based on API specification and Business Requirements.

This project uses LangChain and LLMs to autonomously generate TypeScript tests (Jest) for your code.

## Setup

1. Create a virtual environment:
   ```
   py -m venv venv
   ```

2. Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the main script:
   ```
   py src/main.py
   ```