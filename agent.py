### COMPLETE THE CODE ###
from langchain_ollama import ChatOllama
from rag_tool import rag_search

llm = ChatOllama(model="qwen3:0.6b")

question = "What exact phone number should I call for the university IT Service Desk?"

context = rag_search(question)

prompt = (
    "You are a university IT support assistant.\n"
    "Use ONLY the context below to answer.\n"
    "If the answer is not in the context, say you don't know.\n\n"
    "Context:\n" + context + "\n\n"
    "User: " + question + "\n\n"
    "Assistant:"
)

response = llm.invoke(prompt)
print(response.content)