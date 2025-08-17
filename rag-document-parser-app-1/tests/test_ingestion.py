import unittest
from src.ingestion.pdf_loader import load_pdf
from src.ingestion.metadata_schema import extract_metadata
from src.ingestion.normalizer import normalize_metadata
from src.ingestion.chunker import chunk_text

class TestDocumentIngestion(unittest.TestCase):

    def test_load_pdf(self):
        pdf_path = 'path/to/sample.pdf'
        content = load_pdf(pdf_path)
        self.assertIsNotNone(content)
        self.assertGreater(len(content), 0)

    def test_extract_metadata(self):
        sample_content = "Sample document content with metadata."
        metadata = extract_metadata(sample_content)
        self.assertIn('title', metadata)
        self.assertIn('author', metadata)

    def test_normalize_metadata(self):
        raw_metadata = {
            'title': '   Sample Title   ',
            'author': 'John Doe'
        }
        normalized = normalize_metadata(raw_metadata)
        self.assertEqual(normalized['title'], 'Sample Title')
        self.assertEqual(normalized['author'], 'John Doe')

    def test_chunk_text(self):
        long_text = "This is a long text that needs to be chunked into smaller pieces."
        chunks = chunk_text(long_text, chunk_size=10)
        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(len(chunk) <= 10 for chunk in chunks))

if __name__ == '__main__':
    unittest.main()