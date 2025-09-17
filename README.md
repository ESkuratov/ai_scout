# AI Scout

AI Scout is a tool that uses an agent-based approach to research and generate insights about AI technologies and their applications.

## Features

- Uses the LangGraph ReAct agent framework
- Integrates with OpenAI's GPT-4.1-mini model
- Includes web search capabilities via Tavily
- Generates Mermaid diagrams for agent execution visualization

## Setup

1. Create a `.env` file with the following keys:
   - `OPENGPT_API_KEY`: Your OpenAI API key
   - `BASE_URL`: The API base URL
   - `TAVILY_API_KEY`: Your Tavily API key for web search

2. Install dependencies (see requirements.txt)

## Usage

Run the main.py script to execute the agent. By default, it will:
1. Initialize the LangGraph ReAct agent with the GPT-4.1-mini model
2. Execute a search for new generative AI implementation scenarios
3. Generate a visualization of the agent's reasoning process
4. Save the visualization as "react_graph.png"
5. Display the final response

You can modify the query in the `agent.invoke()` call to ask different questions.

## Output

The tool provides:
- A detailed text response to your query
- A visual representation of the agent's reasoning process as a PNG image

