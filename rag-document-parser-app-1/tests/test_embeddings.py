import pytest
from src.embeddings.embedder import vectorize_content
from src.embeddings.models import EmbeddingModel

def test_vectorize_content():
    # Sample text for testing
    sample_text = "This is a test document."
    
    # Expected output shape (depends on the embedding model)
    expected_shape = (1, 768)  # Example for a model with 768 dimensions

    # Create an instance of the embedding model
    model = EmbeddingModel()

    # Vectorize the sample text
    vector = vectorize_content(sample_text, model)

    # Assert the shape of the output vector
    assert vector.shape == expected_shape, f"Expected shape {expected_shape}, but got {vector.shape}"

def test_embedding_model_initialization():
    # Test if the embedding model initializes correctly
    model = EmbeddingModel()
    assert model is not None, "Embedding model should be initialized."