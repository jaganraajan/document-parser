from typing import Any, Dict
import requests

class LLMResponder:
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.api_key = api_key

    def generate_response(self, prompt: str, metadata: Dict[str, Any]) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "prompt": prompt,
            "metadata": metadata
        }
        response = requests.post(self.api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("response", "")

    def create_prompt(self, base_prompt: str, filters: Dict[str, Any]) -> str:
        filter_str = " ".join([f"{key}: {value}" for key, value in filters.items()])
        return f"{base_prompt}\n\nFilters:\n{filter_str}"