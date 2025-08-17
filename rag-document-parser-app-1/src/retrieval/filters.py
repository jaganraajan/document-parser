from typing import Dict, Any, List

class MetadataFilter:
    def __init__(self, filters: Dict[str, Any]):
        self.filters = filters

    def apply(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        filtered_documents = documents
        for key, value in self.filters.items():
            filtered_documents = [doc for doc in filtered_documents if doc.get(key) == value]
        return filtered_documents

def filter_by_jurisdiction(documents: List[Dict[str, Any]], jurisdiction: str) -> List[Dict[str, Any]]:
    return [doc for doc in documents if doc.get('jurisdiction') == jurisdiction]

def filter_by_framework(documents: List[Dict[str, Any]], framework: str) -> List[Dict[str, Any]]:
    return [doc for doc in documents if doc.get('framework') == framework]

def filter_by_document_type(documents: List[Dict[str, Any]], doc_type: str) -> List[Dict[str, Any]]:
    return [doc for doc in documents if doc.get('document_type') == doc_type]

def filter_by_date(documents: List[Dict[str, Any]], date: str) -> List[Dict[str, Any]]:
    return [doc for doc in documents if doc.get('date') == date]