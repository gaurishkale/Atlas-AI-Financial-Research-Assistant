from langchain_ollama import ChatOllama


class AtlasLLM:

    def __init__(self):

        self.llm = ChatOllama(
            model="qwen2.5:3b",
            temperature=0
        )

    def ask(self, prompt: str):

        response = self.llm.invoke(prompt)

        return response.content