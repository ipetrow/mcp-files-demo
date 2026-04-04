from mcp_client.mcp_client import MCPClient

RESOURCE_URI = "file://receipts/receipt-001.pdf"
RESOURCE_DIR = "receipts"

class ChatInterface:

    def __init__(self, client: MCPClient):
        self.client = client

    async def start_session(self):
        """Starts an interactive chat session."""
        
        print("\nChat session started!")
        print("Type your queries or 'quit' to exit.")
        print("Use the format '@receipts: <query>' to retrive data from the receipt.")

        while True:
            try:
                query = input("\nQuery: ").strip()

                if query.lower() == "quit":
                    break
                
                if (query.startswith('@')):
                    resource = query[1:]
                    print(f"Debug 2: ", resource)
                    if resource == RESOURCE_DIR:
                        response = await self.client.process(query=query, resource_uri=RESOURCE_URI)
                    else:
                        response = "Invalid input!"
                else:
                    response = "Invalid input!"

                print("\n" + response)
            except Exception as e:
                print(f"\nError: {str(e)}")

        print("\nPlease let me know if I can provide further assistance!")
