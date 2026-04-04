import json
import os
from openai import OpenAI

from mcp_client.llm.base_service import LLMService

MODEL = "" # TODO add respective model name
MAX_TOKENS = 1000
ENDPOINT = "" # TODO add azure endpoint

class OpenAIService(LLMService):
    """Handles the communication between the OpenAI Responses API and the MCP resources."""

    def __init__(self):
        api_key = os.getenv("AZURE_OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "AZURE_OPENAI_API_KEY environment variable is empty."
            )
        
        self.openai = OpenAI(
            api_key=api_key,
            base_url=ENDPOINT
        )

    async def process(self, query: str, resource_base64: str, resource_name: str) -> str:
        """
        Processes query using OpenAI Responses API and available resources.
        
        Args:
            query: a query provided by the User.
            resource_base64: the content of the resource in a base64 encoded string.

        Returns:
            A string representing the history of all exchanged messages for processing the query (e.g., logs, final answer).
        """

        input = [
            {
                "role": "user", 
                "content": [
                    {
                        "type": "input_file",
                        "filename": resource_name,
                        "file_data": f"data:application/pdf;base64,{resource_base64}",
                    },
                    {
                        "type": "input_text",
                        "text": str(query),
                    }
                ]
            }
        ]

        # Initial OpenAI API call
        initial_response = self.openai.responses.create(
            model=MODEL, 
            max_output_tokens=MAX_TOKENS, 
            input=input
        )

        final_result = []

        # Appends the model message content if present
        response_message_content = initial_response.output_text
        if response_message_content:
            final_result.append(response_message_content)

        return "Assistant: " + "\n".join(final_result)