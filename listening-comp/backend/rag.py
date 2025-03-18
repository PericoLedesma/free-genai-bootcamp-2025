import chromadb
import numpy as np

# Dummy embedding function for demonstration purposes
def dummy_embedding(text):
    # Returns a fixed random vector based on the text hash for reproducibility
    np.random.seed(hash(text) % 2**32)
    return np.random.rand(128).tolist()


def main():
    # Initialize Chroma client
    client = chromadb.Client()

    # Create or get a collection for documents
    collection_name = 'document_collection'
    collection = client.get_or_create_collection(name=collection_name)

    # Example documents to add to the vector db
    documents = [
        {'id': 'doc1', 'content': 'This is the first document.', 'metadata': {'source': 'manual'}},
        {'id': 'doc2', 'content': 'This is the second document.', 'metadata': {'source': 'manual'}}
    ]

    # Prepare data for adding
    ids = [doc['id'] for doc in documents]
    contents = [doc['content'] for doc in documents]
    metadatas = [doc['metadata'] for doc in documents]
    embeddings = [dummy_embedding(content) for content in contents]

    # Add documents to the collection
    collection.add(
        ids=ids,
        documents=contents,
        metadatas=metadatas,
        embeddings=embeddings
    )

    # Example query: retrieve similar document for a given query text
    query_text = 'first'
    query_embedding = dummy_embedding(query_text)
    results = collection.query(query_embeddings=[query_embedding], n_results=1)

    print('Query results for:', query_text)
    print(results)


if __name__ == '__main__':
    main()
