from fastapi import APIRouter, HTTPException
from src.ingestion.pdf_loader import load_pdf
from src.ingestion.metadata_schema import MetadataSchema
from src.ingestion.normalizer import normalize_metadata
from src.ingestion.chunker import chunk_text
from src.storage.vector_store import store_vectors
from pydantic import BaseModel
from typing import List

router = APIRouter()

class IngestRequest(BaseModel):
    file_path: str

@router.post("/ingest")
async def ingest_document(request: IngestRequest):
    try:
        # Load PDF document
        pdf_content = load_pdf(request.file_path)
        
        # Extract and normalize metadata
        metadata = MetadataSchema.extract(pdf_content)
        normalized_metadata = normalize_metadata(metadata)
        
        # Chunk text for processing
        text_chunks = chunk_text(pdf_content)
        
        # Store vectors in the vector database
        store_vectors(text_chunks, normalized_metadata)
        
        return {"message": "Document ingested successfully", "metadata": normalized_metadata}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))