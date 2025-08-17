from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DocumentMetadata(BaseModel):
    title: str
    author: List[str]
    created_date: datetime
    modified_date: Optional[datetime]
    document_type: str
    jurisdiction: str
    framework: str
    keywords: List[str]

class MetadataSchema:
    def __init__(self, metadata: DocumentMetadata):
        self.metadata = metadata

    def normalize(self):
        # Implement normalization logic here
        pass

    def validate(self):
        return self.metadata.dict()  # Validate and return metadata as dict