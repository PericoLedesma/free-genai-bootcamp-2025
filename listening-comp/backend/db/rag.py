import chromadb
import numpy as np


class VectorDB:
    def __init__(self, persist_directory: str):
        print("Initializing VectorDB...")
        # use the new PersistentClient API
        self.client = chromadb.PersistentClient(path=persist_directory)
        # get or create our chunks collection
        self.collection = self.client.get_or_create_collection("conversation_chunks")
        print("Collections:", self.client.list_collections())


    def _next_chunk_id(self, conversation_id: str) -> str:
        """Compute next chunk_id = '{conversation_id}_{n+1}'."""
        # fetch existing chunks for this conversation
        convo = self.collection.get(where={"conversation_id": conversation_id})
        existing_count = len(convo["ids"])
        return f"{conversation_id}_{existing_count + 1}"

    def add_chunk(
        self,
        conversation_id: str,
        embedding: list[float],
        text: str,
        metadata: dict | None = None
    ) -> str:
        """
        Add a chunk to the DB, auto‑assigning chunk_id.
        Returns the chunk_id used.
        """
        chunk_id = self._next_chunk_id(conversation_id)
        md = metadata.copy() if metadata else {}
        md.update({
            "conversation_id": conversation_id,
            "text": text
        })
        self.collection.add(
            ids=[chunk_id],
            embeddings=[embedding],
            metadatas=[md]
        )
        return chunk_id

    def search_chunks(self, query_embedding: list[float], top_k: int = 5):
        """Return the top_k most similar chunks."""
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

    def get_chunks_by_conversation(self, conversation_id: str):
        """Fetch all chunks for a given conversation."""
        return self.collection.get(where={"conversation_id": conversation_id})


if __name__ == "__main__":
    db = VectorDB()

    conv_id = "conv001"
    # first chunk
    cid1 = db.add_chunk(
        conversation_id=conv_id,
        embedding=np.random.rand(10).tolist(),
        text="Hey, how are you doing today?",
        metadata={"speaker": "user", "timestamp": "2025-04-18T10:00:00"}
    )
    print(f"Added chunk: {cid1}")

    # second chunk
    cid2 = db.add_chunk(
        conversation_id=conv_id,
        embedding=np.random.rand(10).tolist(),
        text="I'm great, thanks for asking!",
        metadata={"speaker": "assistant", "timestamp": "2025-04-18T10:00:05"}
    )
    print(f"Added chunk: {cid2}")

    # semantic search
    query = np.random.rand(10).tolist()
    res = db.search_chunks(query, top_k=3)
    print("\n🔍 Top similar chunks:")
    for cid, md in zip(res["ids"][0], res["metadatas"][0]):
        print(f" - {cid} [{md['conversation_id']}]: {md['text']}")

    # fetch full conversation
    convo = db.get_chunks_by_conversation(conv_id)
    print(f"\n🧵 Full conversation '{conv_id}':")
    for cid, md in zip(convo["ids"], convo["metadatas"]):
        print(f" • {cid}: {md['text']}")