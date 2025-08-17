import pytest
from src.retrieval.retriever import Retriever
from src.storage.vector_store import VectorStore

@pytest.fixture
def setup_retriever():
    vector_store = VectorStore()
    retriever = Retriever(vector_store)
    return retriever

def test_retrieval_by_query(setup_retriever):
    retriever = setup_retriever
    query = "Sample query text"
    results = retriever.retrieve(query)
    assert results is not None
    assert isinstance(results, list)

def test_retrieval_with_filters(setup_retriever):
    retriever = setup_retriever
    query = "Sample query text"
    filters = {"jurisdiction": "US", "document_type": "report"}
    results = retriever.retrieve(query, filters=filters)
    assert results is not None
    assert isinstance(results, list)

def test_empty_query(setup_retriever):
    retriever = setup_retriever
    query = ""
    results = retriever.retrieve(query)
    assert results == []  # Expecting no results for empty query

def test_retrieval_accuracy(setup_retriever):
    retriever = setup_retriever
    query = "Accuracy test query"
    expected_result_count = 5  # Example expected count
    results = retriever.retrieve(query)
    assert len(results) == expected_result_count  # Check if the count matches expected
