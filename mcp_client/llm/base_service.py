from abc import ABC, abstractmethod

class LLMService(ABC):

    @abstractmethod
    async def process(self, query: str, resource_base64: str, resource_name: str) -> str:
        pass