### COMPLETE THE CODE ###
from policy_loader import load_policy_documents

documents = load_policy_documents()

from rag import retrieve

def rag_search(question):
    docs = retrieve(question, k=3)
    context = "\n\n".join([d.page_content for d in docs])
    return context