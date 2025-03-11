##  Starting a ChromaDB Client and Collection

import chromadb
from chromadb.config import Settings

# Initialize the client with persistence enabled
client = chromadb.Client(
    Settings(chroma_db_impl="duckdb+parquet",
             persist_directory="./advanced_chroma_db")
)

# Create a collection with additional metadata
collection = client.create_collection(
    name="advanced_collection",
    metadata={"description": "A complex collection for advanced vector DB operations"}
)
