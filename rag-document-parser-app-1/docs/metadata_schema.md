# Metadata Schema for Document Parser Application

This document outlines the metadata schema used for extracting and normalizing metadata from documents in the RAG Document Parser Application.

## Metadata Fields

| Field Name       | Data Type | Description                                           |
|------------------|-----------|-------------------------------------------------------|
| title            | string    | The title of the document.                            |
| author           | string    | The author(s) of the document.                        |
| publication_date | date      | The date the document was published.                 |
| document_type    | string    | The type of document (e.g., report, article, etc.).  |
| jurisdiction     | string    | The legal jurisdiction relevant to the document.     |
| framework        | string    | The framework or guidelines the document adheres to. |
| keywords         | array     | A list of keywords associated with the document.     |
| summary          | string    | A brief summary of the document's content.           |

## Normalization Rules

- **Title**: Capitalize the first letter of each word.
- **Author**: Format as "Last Name, First Name".
- **Publication Date**: Convert to ISO 8601 format (YYYY-MM-DD).
- **Document Type**: Use predefined categories.
- **Jurisdiction**: Normalize to a standard list of jurisdictions.
- **Framework**: Map to recognized frameworks.
- **Keywords**: Convert to lowercase and remove duplicates.
- **Summary**: Limit to 250 characters.

## Example Metadata

```json
{
  "title": "Understanding the Legal Framework of AI",
  "author": "Doe, John",
  "publication_date": "2023-01-15",
  "document_type": "report",
  "jurisdiction": "United States",
  "framework": "AI Ethics Guidelines",
  "keywords": ["AI", "ethics", "law"],
  "summary": "This document explores the intersection of AI technology and legal frameworks."
}
```