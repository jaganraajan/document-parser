class EmbeddingModel:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def embed(self, text: str):
        # Placeholder for embedding logic
        pass

class SentenceTransformerModel(EmbeddingModel):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        super().__init__(model_name)

    def embed(self, text: str):
        # Implement embedding logic using Sentence Transformers
        pass

class OpenAIEmbeddingModel(EmbeddingModel):
    def __init__(self, api_key: str):
        super().__init__("OpenAI")
        self.api_key = api_key

    def embed(self, text: str):
        # Implement embedding logic using OpenAI API
        pass