from langchain_ollama.chat_models import ChatOllama

if __name__ == "__main__":
    llm = ChatOllama(model="qwen3:4b")
    resp = llm.stream("你是谁")
    for c in resp:
        print(c.content,end="")
