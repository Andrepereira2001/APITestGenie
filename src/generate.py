# Handles interactions with the LLM via LangChain

from langchain_community.llms import OpenAI
from langchain.prompts import ChatPromptTemplate
import utils

class Generate:

    test_example = """import axios from 'axios';

describe('General description of the test', () => {
test('Specific description of the test', async () => {
    // Prepared test data
    data = {...}
    // Setup test environment
    // Make request with generated data
    const response = await axios.post(url, data);
    // Validate response of request
    expect(response...).toBe(...);
    // Add additional assertions based on response data                             
});
test('Another specific description of the test', async () => {                    
    // Prepared test data
    data = {...}
    // Setup test environment
    // Make request with generated data
    const response = await axios.get(url, data);
    // Validate response of request
    expect(response...).toBe(...);
    // Add additional assertions based on response data  
    });
    // Add more tests for other scenarios
    ...                                                                        
});  
"""

    default_system_prompt = """
As an AI coding assistant, my goal is to facilitate the creation of executable API integration tests in TypeScript.
Many users may not be familiar with coding, so I am here to bridge the gap and help them craft tests that validate their application's business requirements.

To ensure the tests are practical and meet the users' needs, I will generate integration test cases in TypeScript using the Axios and Jest libraries.
These tests will be designed for immediate execution and will interact with the API endpoints defined in the API specification.

I am expected to create more complex tests following the example:

***
{test_example}
***

The tests will be assessed on several key factors:
**Executability**: The tests must run smoothly and without errors.
**Relevance**: The tests must be meaningful and appropriate for the requirement
**Correctness**: The test code should be free of logical errors.
**Coverage**: The tests should cover as many endpoints and scenarios as possible to ensure thorough validation.
**Code Quality**: The code is reliable, executable, and includes clear explanations where necessary.
**Endpoint Accuracy**: The API call matches the type of the request and response object. 

When generating tests, I will consider these important guidelines:
**Informational Completeness**: I will strive to collect as much information as possible. Additionally, I will generate experimental data to use in placeholders.
**Environment setup**: In the setup phase, I will make sure to collect all the data to guarantee that I have the data to execute the test.


Here's how the test generation will be accomplished:

1. **Clarifying the Business Requirement**: In a summarized way, explain the business requirement, along with the specific aspects the tests are verifying.
I will describe the data and the environment state of the test.

2. **Listing Endpoints**: Then, I will list the endpoints that the test script will interact with. For each endpoint, I will specify the types of the request object and the types of the response object.
I will also provide a brief list of steps to reach the correct test environment state.

3. **Craft Executable Test Code**: Finally, I will generate code test cases in TypeScript using Axios and Jest libraries. The code must be presented in a single code block and ready to run. 
Make sure to explain any property that is unclear. Minimize any other prose.

Document your generation using the following format, and only provide information related to the generation step specified in the placeholder.
```
REQUIREMENT:
<1. **Clarifying the Business Requirement**>
ENDPOINTS:
<2. **Listing Endpoints**>
TEST:
\"\"\"typescript
<3. **Craft Executable Test Code**>
\"\"\"
"""
    
    default_user_prompt = """
Following is the business requirement that you will be testing.
This narrative will guide the creation of your tests and provide the context needed to determine the data for API requests.
Here is the business requirement for your reference:
***
{user_story}
***
Next, you will review an API specification that details the available endpoints with the requests/response data structure.
The test you develop should validate the correct functioning of these endpoints
Ensure that you respect the requirements detailed in the specification and the request and response object types.
Here is the API specification:
***
{api_specification}
***
Let's start!

"""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.llm = OpenAI(openai_api_key=api_key)

    def generate_test(self, prompt: str) -> str:
        # Call the LLM to generate a test based on the prompt
        return self.llm(prompt)

    def generate_test_with_chat_prompt(self, user_story: str, api_specification: str,
                                        system_prompt: str = default_system_prompt, user_prompt: str = default_user_prompt) -> str:
        """
        Generates a test using ChatPromptTemplate with system and user prompts.
        """
        content = {
            "user_story": user_story,
            "api_specification": api_specification,
            "test_example": Generate.test_example
        }

        chat_prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", user_prompt)
        ])
        formatted_prompt = chat_prompt.format(**content)

        utils.write_file("./test_output/prompt.txt", formatted_prompt)

        return self.llm(formatted_prompt)
    
    def parse_generation(self, generation: str) -> str:
        """
        Parses the generated test code to ensure it meets the required format.
        """
        
        #Parse requirements "REQUIREMENT:"
        requirement_start = generation.find("REQUIREMENT:") + len("REQUIREMENT:")
        requirement_end = generation.find("ENDPOINTS:")

        #Parse endpoints "ENDPOINTS:"
        endpoints_start = requirement_end + len("ENDPOINTS:")
        endpoints_end = generation.find("TEST:")

        #Parse test "TEST:"
        test_start = endpoints_end + len("TEST:\n\"\"\"typescript\n")
        test_end = generation.find("\"\"\"", test_start)

        requirement = generation[requirement_start:requirement_end].strip()
        endpoints = generation[endpoints_start:endpoints_end].strip()
        test = generation[test_start:test_end].strip()

        return requirement, endpoints, test
