import unittest
from src.llm.responder import LLMResponder
from src.llm.prompts import PromptTemplates

class TestLLMPipeline(unittest.TestCase):

    def setUp(self):
        self.llm_responder = LLMResponder(api_key="test_api_key")
        self.prompt_templates = PromptTemplates()

    def test_llm_response(self):
        prompt = self.prompt_templates.generate_prompt("test query", {"metadata_key": "metadata_value"})
        response = self.llm_responder.get_response(prompt)
        self.assertIsNotNone(response)
        self.assertIn("expected_output", response)

    def test_prompt_template_generation(self):
        prompt = self.prompt_templates.generate_prompt("test query", {"key": "value"})
        self.assertEqual(prompt, "Expected prompt format with key=value")

    def test_logging_accuracy(self):
        # Assuming there's a method to log accuracy
        accuracy = self.llm_responder.log_accuracy("test query", "expected_output", "actual_output")
        self.assertTrue(accuracy)

if __name__ == '__main__':
    unittest.main()