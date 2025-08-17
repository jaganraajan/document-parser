# RAG Document Parser App

## Overview
The RAG Document Parser App is a robust application designed to ingest, process, and retrieve information from documents, particularly PDFs. It leverages advanced techniques in document parsing, embedding, and retrieval to provide contextual responses using large language models (LLMs).

## Features
- Document ingestion from PDF files
- Metadata extraction and normalization
- Text chunking for efficient processing
- Vectorization of content for storage and retrieval
- Contextual retrieval using LLMs
- Logging and evaluation of retrieval accuracy

## Project Structure
```
rag-document-parser-app
├── README.md
├── pyproject.toml
├── requirements.txt
├── src
│   ├── ingestion
│   ├── embeddings
│   ├── storage
│   ├── retrieval
│   ├── llm
│   ├── evaluation
│   ├── logging_utils
│   ├── api
│   ├── ui
│   └── config
├── scripts
├── tests
└── docs
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/rag-document-parser-app.git
   cd rag-document-parser-app
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure settings in `src/config/settings.py` as needed.

## Usage Guidelines
- To ingest documents, run:
  ```
  python scripts/ingest_documents.py
  ```

- To rebuild the vector index, use:
  ```
  python scripts/rebuild_index.py
  ```

- To run benchmarks, execute:
  ```
  python scripts/run_benchmarks.py
  ```

## API Documentation
The application provides an API for document ingestion and querying. Refer to the `src/api/routers` directory for available endpoints.

## Testing
Unit tests are located in the `tests` directory. To run tests, use:
```
pytest tests/
```

## Contribution
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.