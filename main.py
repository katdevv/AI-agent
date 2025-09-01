# message class that represents a user’s input in a chat-like format
from langchain_core.messages import HumanMessage

# OpenAI Chat API
from langchain_openai import ChatOpenAI

# A decorator (@tool) that turns a Python function into a tool 
from langchain.tools import tool

# a helper to create a ReAct agent.
# ReAct = Reasoning + Acting -> the LLM decides whether to think, call a tool, or reply
from langgraph.prebuilt import create_react_agent

# Loads API keys from venv
from dotenv import load_dotenv

load_dotenv()

# Custom calculator tool for the AI agent to use
@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers"""
    return f"The sum of {a} and {b} is {a + b}"

# Custom greeting tool for the AI agent to use
@tool
def say_hello(name: str) -> str:
    """Useful for greating a user"""
    return f"Nice meeting you, {name}!\nHow can I assist you?"

def main():
    model = ChatOpenAI(model="gpt-5-nano", temperature=0)

    # Test connection
    msg = model.invoke("ping")
    print("Model actually used:", msg.response_metadata.get("model_name"))

    # Agent 
    tools = [calculator, say_hello]
    agent_executor = create_react_agent(
        model, 
        tools,
        system_prompt="You are an assistant. For any arithmetic, always use the calculator tool instead of mental math."
    )

    print("Welcome! I'm your AI assistant and math tutor. Type 'quit' to exit.")
    print("Ask me anything!")

    # Chatbot
    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break
        
        print("\nAssistant: ", end="")

        # Executes agent with user input
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            # Print messages
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
