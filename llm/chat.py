from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import settings


class AtlasLLM:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=settings.LLM_MODEL,
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0,
        )

    def ask(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content