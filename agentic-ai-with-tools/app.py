import sys
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from tools import calculator, get_system_status

def main():
    try:
        print("Initializing local agent with ollama (Llama 3.1) .....")

        #initialize local LLM
        llm = ChatOllama(
            model = "llama3.1",
            temperature = 0
        )

        #package available tools from tools.py
        tools = [calculator,get_system_status]

        # create a react agent graph
        agent_executor = create_react_agent(llm,tools)

        #test query 1 : triggers calculator tool
        prompt_1 = "what is 154 multiplied by 38?"
        print(f"\n--- User query 1 : {prompt_1} ----")
        response_1 = agent_executor.invoke({"messages": [("user", prompt_1)]})

        final_msg_1 = response_1["messages"][-1].content
        print(f"Agent output: \n{final_msg_1}")

        #test query 2 : triggers system status tool
        prompt_2 = "Check the system status for our database service"
        print(f"\n---user query 2: {prompt_2} ---")
        response_2 = agent_executor.invoke({'messages': [("user",prompt_2)]})

        final_msg_2 = response_2["messages"][-1].content
        print(f"Agent output : \n{final_msg_2}")

    except Exception as e:
        print(f"\nError executing Agent : {e}")
        print("ensure 'ollama serve' is active and llama 3 is available locally")
        sys.exit(1)

if __name__ =="__main__":
    main()
