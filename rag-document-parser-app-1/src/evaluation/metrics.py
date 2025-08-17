def calculate_accuracy(retrieved_docs, relevant_docs):
    if not retrieved_docs:
        return 0.0
    correct_retrievals = len(set(retrieved_docs) & set(relevant_docs))
    return correct_retrievals / len(retrieved_docs)

def precision(retrieved_docs, relevant_docs):
    if not retrieved_docs:
        return 0.0
    true_positives = len(set(retrieved_docs) & set(relevant_docs))
    return true_positives / len(retrieved_docs)

def recall(retrieved_docs, relevant_docs):
    if not relevant_docs:
        return 0.0
    true_positives = len(set(retrieved_docs) & set(relevant_docs))
    return true_positives / len(relevant_docs)

def f1_score(precision, recall):
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)

def log_metrics(metrics):
    # Placeholder for logging metrics to a file or monitoring system
    pass