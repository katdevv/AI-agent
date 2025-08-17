from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers"""
    return f"The sum of {a} and {b} is {a + b}"

@tool
def say_hello(name: str) -> str:
    """Useful for greating a user"""
    return f"Nice meeting you, {name}!\nHow can I assist you?"

def main():
    model = ChatOpenAI(model="gpt-5-nano", temperature=0)

    msg = model.invoke("ping")
    print("Model actually used:", msg.response_metadata.get("model_name"))


    tools = [calculator, say_hello]
    agent_executor = create_react_agent(
        model, 
        tools,
        system_prompt="You are an assistant. For any arithmetic, always use the calculator tool instead of mental math."
    )

    print("Welcome! I'm your AI assistant and math tutor. Type 'quit' to exit.")
    print("Ask me anything!")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break
        
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
