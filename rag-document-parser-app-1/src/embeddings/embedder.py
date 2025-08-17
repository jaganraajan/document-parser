from sentence_transformers import SentenceTransformer
import numpy as np

class Embedder:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, texts):
        embeddings = self.model.encode(texts, convert_to_tensor=True)
        return embeddings.cpu().numpy()

    def normalize_embeddings(self, embeddings):
        norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
        normalized_embeddings = embeddings / norms
        return normalized_embeddings

    def embed_and_normalize(self, texts):
        embeddings = self.embed_text(texts)
        return self.normalize_embeddings(embeddings)