### COMPLETE THE CODE ###

from policy_loader import load_policy_documents

documents = load_policy_documents()

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="university_policies"
)


def retrieve(query, k=3):
    results = vector_store.similarity_search(query, k=k)
    return results