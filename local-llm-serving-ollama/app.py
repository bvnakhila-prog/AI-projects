from langchain_ollama import ChatOllama

# initializing the local ollama model
llm = ChatOllama(
    model = "llama3",
    temperature=0.7
)

# prompting the model
print(" sending request to local ollama model......")
response = llm.invoke("give me a 1 sentence joke about a software engineer")

#print llm's response
print("\n LLM Output:")
print(response.content)
