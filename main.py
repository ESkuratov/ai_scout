import os
import io
import logging
import getpass
from dotenv import load_dotenv
from IPython.display import Image, display
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from prompts import SYSTEM_PROMPT
from tools import search_web

load_dotenv()
api_key = os.getenv("OPENGPT_API_KEY")
base_url = os.getenv("BASE_URL")
tavily_key = os.getenv("TAVILY_API_KEY")

# Initialize the model
model = ChatOpenAI(
    model="openai/gpt-4.1-mini",
    api_key = api_key,
    base_url = base_url)

agent = create_react_agent(
    model = model,
    tools = [search_web],
    prompt = SYSTEM_PROMPT
)

result = agent.invoke (
    {"messages": [{"role": "user", "content": "Find 10 new scenarios for the use and implementation of Generative AI in companies over the September 2025."}]}
    
    
)

# Show

mermaid_png = agent.get_graph(xray=True).draw_mermaid_png()


# If you're in a Jupyter notebook, display the image
try:
    display(Image(mermaid_png))
except:
    print("Image display only works in notebook environments")

# Save the Mermaid diagram to a file
with open("react_graph.png", "wb") as f:
    f.write(mermaid_png)


# Extract and print only the final message content
if 'messages' in result and result['messages']:
    final_message = result['messages'][-1]  # Get the last message
    print("\n=== FINAL RESPONSE ===\n")
    print(final_message.content)
else:
    print("No response received or unexpected response format.")