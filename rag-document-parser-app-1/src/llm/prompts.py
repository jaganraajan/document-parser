from typing import Dict, Any

def generate_prompt(template: str, metadata: Dict[str, Any]) -> str:
    """
    Generates a prompt for the LLM based on the provided template and metadata.
    
    Args:
        template (str): The prompt template to use.
        metadata (Dict[str, Any]): The metadata to incorporate into the prompt.
    
    Returns:
        str: The generated prompt.
    """
    for key, value in metadata.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))
    return template

# Example prompt templates
PROMPT_TEMPLATES = {
    "basic_query": "Please summarize the following document: {{{{document}}}}",
    "detailed_analysis": "Analyze the document with the following details: {{{{document}}}}. Consider the context of {{{{jurisdiction}}}} and framework {{{{framework}}}}.",
    "specific_query": "What are the key points regarding {{{{topic}}}} in the document dated {{{{date}}}}?",
}