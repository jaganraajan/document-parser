from pinecone import Pinecone

class VectorStore:
    def __init__(self, api_key, environment, index_name):
        Pinecone.init(api_key=api_key, environment=environment)
        self.index = Pinecone.Index(index_name)

    def store_vector(self, vector, metadata, stable_id):
        self.index.upsert(vectors=[(stable_id, vector)], metadata=metadata)

    def retrieve_vector(self, query_vector, top_k=5):
        return self.index.query(queries=[query_vector], top_k=top_k)

    def delete_vector(self, stable_id):
        self.index.delete(ids=[stable_id])