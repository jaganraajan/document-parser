import logging

class AuditLogger:
    def __init__(self, log_file='audit.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

    def log_event(self, event_message):
        self.logger.info(event_message)

    def log_error(self, error_message):
        self.logger.error(error_message)

    def log_retrieval(self, query, results_count):
        self.logger.info(f'Retrieval Query: "{query}" returned {results_count} results.')

    def log_ingestion(self, document_id):
        self.logger.info(f'Document with ID: {document_id} ingested successfully.')

    def log_benchmark(self, benchmark_name, duration):
        self.logger.info(f'Benchmark "{benchmark_name}" completed in {duration:.2f} seconds.')