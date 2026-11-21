### COMPLETE THE CODE ###
from policy_loader import load_policy_documents
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

documents = load_policy_documents()
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# Create an empty vector store
vector_store = Chroma(
    embedding_function=embeddings,
    collection_name="university_policies"
)

# Add documents in batches to prevent Ollama from crashing
batch_size = 20
for i in range(0, len(documents), batch_size):
    batch = documents[i:i + batch_size]
    vector_store.add_documents(batch)
    print(f"Successfully indexed {i + len(batch)} / {len(documents)} documents")

def retrieve(query, k=3):
    results = vector_store.similarity_search(query, k=k)
    return results
