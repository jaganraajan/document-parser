from fastapi import FastAPI
from src.api.routers import ingest, query

app = FastAPI()

app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(query.router, prefix="/query", tags=["query"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Parser API!"}