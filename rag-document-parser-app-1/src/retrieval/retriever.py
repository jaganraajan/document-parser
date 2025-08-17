from storage.vector_store import VectorStore
from retrieval.filters import MetadataFilters

class DocumentRetriever:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def retrieve_documents(self, query: str, filters: MetadataFilters = None):
        # Use the vector store to retrieve documents based on the query
        results = self.vector_store.query(query, filters)
        return results

    def retrieve_by_id(self, document_id: str):
        # Retrieve a document by its stable ID
        document = self.vector_store.get_by_id(document_id)
        return document

    def retrieve_with_context(self, query: str, context: str):
        # Retrieve documents with additional context
        results = self.vector_store.query_with_context(query, context)
        return results