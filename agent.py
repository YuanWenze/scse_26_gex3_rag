### COMPLETE THE CODE ###
import re

from langchain_ollama import ChatOllama
from rag_tool import rag_search
llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0,
    num_predict=180,
    reasoning=False,
)

question = "What exact phone number should I call for the university IT Service Desk?"

context = rag_search(question)

PHONE = re.compile(r"(?:\+?\d[\d\s\-().]{6,}\d)")

if re.search(r"\b(phone|telephone|call)\b", question, re.I) and not PHONE.search(context):
    print(
        "I don't know. The provided university IT policies do not contain "
        "a Service Desk phone number."
    )
else:
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
