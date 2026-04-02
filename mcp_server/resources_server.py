import base64
import os
from pathlib import Path 
from typing import List
from mcp.server.fastmcp import FastMCP

RECEIPTS_DIR = "receipts"

# Initialize FastMCP server
# mcp = FastMCP("receipts")

# @mcp.resource("receipts://receipt-001.pdf")
def get_receipt() -> bytes:
    """
    TODO
    """

    for item in os.listdir(RECEIPTS_DIR):
        file_path = os.path.join(RECEIPTS_DIR, item)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "rb") as pdf_file:
                    encoded_file = base64.b16encode(pdf_file.read())
            except FileNotFoundError as e:
                print(f"Error reading {file_path}: {str(e)}")
                continue
        
        return encoded_file

if __name__ == "__main__":
    get_receipt()
    # mcp.run(transport="stdio")