import os
import sys
from src.storage.vector_store import VectorStore
from src.ingestion.pdf_loader import load_pdfs
from src.ingestion.normalizer import normalize_metadata
from src.ingestion.chunker import chunk_text
from src.embeddings.embedder import embed_content

def rebuild_index(pdf_directory):
    # Load PDFs from the specified directory
    pdf_files = load_pdfs(pdf_directory)
    
    # Initialize the vector store
    vector_store = VectorStore()

    for pdf_file in pdf_files:
        # Extract metadata and normalize it
        metadata = extract_metadata(pdf_file)
        normalized_metadata = normalize_metadata(metadata)

        # Chunk the text from the PDF
        text_chunks = chunk_text(pdf_file)

        # Embed the content
        embeddings = embed_content(text_chunks)

        # Store the embeddings with metadata in the vector store
        for chunk, embedding in zip(text_chunks, embeddings):
            vector_store.store(embedding, normalized_metadata)

    print("Index rebuilt successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rebuild_index.py <pdf_directory>")
        sys.exit(1)

    pdf_directory = sys.argv[1]
    rebuild_index(pdf_directory)