from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    metadata_filters = request.json.get('filters', {})
    
    # Call the API to retrieve relevant documents based on the user query and filters
    response = requests.post('http://localhost:5000/api/query', json={
        'query': user_query,
        'filters': metadata_filters
    })
    
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Failed to retrieve documents'}), response.status_code

@app.route('/ingest', methods=['POST'])
def ingest():
    document = request.json.get('document')
    
    # Call the API to ingest the document
    response = requests.post('http://localhost:5000/api/ingest', json={
        'document': document
    })
    
    if response.status_code == 200:
        return jsonify({'message': 'Document ingested successfully'}), 200
    else:
        return jsonify({'error': 'Failed to ingest document'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)