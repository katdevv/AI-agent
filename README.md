# AI Agent with Custom Tools ⚙️  

This is a **learning project** built with **LangChain** and the **OpenAI API**.  
It demonstrates how to create an interactive AI agent that can:  
- Respond to user messages in a chatbot-like loop  
- Call **custom tools** (a calculator and a greeting function)  
- Stream responses in real-time  

---

## 🚀 Usage  

1. Create and activate a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate    # Linux/Mac
   .\venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Add your OPENAI_API_KEY to a .env file:
```bash
   OPENAI_API_KEY=your_api_key_here
```

4. Run the script:
```bash
   python main.py
```

5. Type a question (e.g. what is 2+2?).
For math, the agent will call the calculator tool.
For greetings, it will use the say_hello tool.
Type quit to exit.