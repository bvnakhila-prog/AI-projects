from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# step 1 : document loading
print(" 1. Loading the document . . . . . . . . ")
loader = TextLoader("company_policy.txt") # target the text file in the urrent folder
print("Loader : ",loader)
docs = loader.load()  #reading the document and converting to langchain document object
print("Docs : ",docs) 


# step 2: text chunking
print(" Splitting the chunks . . . . . . . . . .")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap = 20) # chunk size cuts text into 200 characters to fit embedding/context constraints, chunk overlap overlaps chunks by 20 characters so sentence boundaries dont lose context

splits = text_splitter.split_documents(docs) # executing the split logic on the loaded document array


# step 3 : vector embedding and storage
print("Embedding and storing in Chroma. . . . . . . ")
embeddings = OllamaEmbeddings(model = "mxbai-embed-large")# connecting to local Ollama to use Llama3 as the vector embedding model

vectorstore = Chroma.from_documents(documents=splits,embedding=embeddings)#embeddings and text go into Chroma and Chroma calls Ollama to convert each tino vector and index them 
 # converts vector database into retriever itnerface
retriever = vectorstore.as_retriever(search_kwargs = {"k":2}) #search kwargs tells Chromadb to retrieve only top 2 relavant chunks per search query

# step 4 : llm and system prompt setup
print("Setting up LLama 3 RAG CHAIN. . . . . . . ")
llm = ChatOllama(model = "llama3",temperature = 0) # 0 means greedy,non creative

# defininig the system prompts not to make up any hallucinations/facts
system_prompt = ("You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, say that you don't know.\n\n"
    "{context}"
    ) #{context} is the placeholder where chromadb's top - k retrieved chunks will be dynamicallys injected


# tempalte combining the system instructions with the users incoming query
prompt = ChatPromptTemplate.from_messages([("system",system_prompt),
                                           ("human","{input}"),])


# format retrieved documents into a single text block
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# step 5 : chain assembly 
# connects retriever >> prompt >>>>llm >>>>string output
rag_chain = (
    {"context" : retriever | format_docs, "input": RunnablePassthrough()}
    | prompt
    |llm
    | StrOutputParser()
)

# step 6 : execution
query = " how much money do employees get for home office equipment, and when are claims due? "
print(f"\n > question : {query}\n")

response = rag_chain.invoke(query)

print("RAG Answer : ",response)