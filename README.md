# Overview
This repository presents an agentic MCP Client-Server workflow that allows to extract data from a PDF file.

# Prerequisites
- Installed Python `uv` package and project management tool. A basic understanding of how the tool works would be helpful for a better insight of how the project is set up and executed.
- Installed Python version 3.14.2 or higher. **Note**: It is recommended to keep the system Python clean. Therefore, use `pyenv`, `uv` for managing other Python versions.
- An OpenAI API key included in the environment variables.

# Project Details
## Structure
The project consists of 3 main directories:
- `mcp_client`: the Python module includes all the code related to the MCP Client and the integration of the MCP Server and the LLM.
- `mcp_server`: the directory includes the MCP Server related code, the tools definitions and the database itself.- `receipts`: the folder contains a receipt PDF file from which the model extracts and reasons data.

# MCP Server
The MCP Server is created using `FastMCP` with `stdio` as transport layer. It exposes only one primitive type - resources. 

There is only one exposed resource - `get_receipt()`. 
- It extracts the content of the PDF file (situated in `receipts/`) in a base64 encoded string.
- It is created to handle only one PDF file.

# File Data
The PDF file represents a receipt for 3 books.
- Book information: The following data for each book is available: ***isbn***, ***title***, ***author***, ***number of pages***, ***quantity* and ***price***.
- Other information: Furthermore, the ***receipt number***, ***texes amount***, ***total price*** (with and without texes), ***seller*** and ***buyer*** data.

# Large Language Model
In this example, OpenAI `gpt-5-mini` model is used from Azure - The GPT model was deployed in Azure and the Azure OpenAI API key used for the connection with the LLM. This integration allows the User to interact on an abstract level with the tools exposed from the MCP Server.

## Integration Details
- OpenAI Python API: the library provides access to the OpenAI REST API.
- Responses API: an interface for interacting with the LLM.

# Running the Example
## Setup
1. Clone the repository: `git clone git@github.com:ipetrow/mcp-files-demo.git`.
2. Sync the project in order to download and install all the required project dependencies and they are up to date: `uv sync`. This will create the project virtual environment (`.venv`) as well.
3. Update the model name in `mcp_client/llm/openai_service.py` by providing a value for the `MODEL` constant.
4. Update the Azure endpoint in `mcp_client/llm/openai_service.py` by providing a value for the `ENDPOINT` constant.
5. Double check the OpenAI API key is added in the environment variables. The name of the variable is `OPENAI_API_KEY` and retrieved in `mcp_client/llm/openai_service.py`.

## Execution
Start the MCP Client and connect to the MCP Server by: `uv run python -m mcp_client --server ./mcp_server/resources_server.py`

## Prompt Examples
The prompts should follow a strict format: `@receipts: <query>`:
- "@receipts: List all the ordered books in the receipt."
- "@receipts: Extract the receipt number."
- "@receipts: What is the total price in the receipt?"

# Resources
- Build an MCP server: https://modelcontextprotocol.io/docs/develop/build-server
- Build an MCP client: https://modelcontextprotocol.io/docs/develop/build-client
- Build a Python MCP Client to Test Servers From Your Terminal: https://realpython.com/python-mcp-client/
- File Inputs: https://developers.openai.com/api/docs/guides/file-inputs 