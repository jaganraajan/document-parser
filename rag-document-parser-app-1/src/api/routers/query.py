from fastapi import APIRouter, HTTPException
from src.retrieval.retriever import retrieve_documents
from src.llm.responder import generate_response

router = APIRouter()

@router.post("/query")
async def query_documents(query: str, jurisdiction: str = None, framework: str = None, document_type: str = None, date: str = None):
    try:
        # Retrieve documents based on the query and filters
        documents = retrieve_documents(query, jurisdiction, framework, document_type, date)
        
        if not documents:
            raise HTTPException(status_code=404, detail="No documents found")

        # Generate a response using the LLM
        response = generate_response(query, documents)
        
        return {
            "documents": documents,
            "response": response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))