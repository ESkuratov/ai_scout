# AI Scout

AI Scout is a tool that uses an agent-based approach to research and generate insights about AI technologies and their applications, with a particular focus on generative AI implementation scenarios.

## Features

- Uses the LangGraph ReAct agent framework
- Integrates with OpenAI's GPT-4.1-mini model
- Includes web search capabilities via Tavily
- Generates Mermaid diagrams for agent execution visualization
- Supports structured query formats with detailed processing instructions
- Delivers results in tabular format with analytical summaries
- Provides multilingual output (supports Russian)

## Components

### Main Application (main.py)
- Initializes the LangGraph ReAct agent
- Executes queries about generative AI implementations
- Visualizes the agent's reasoning process
- Outputs formatted responses

### Prompts System (prompts.py)
- Contains structured XML-formatted system prompts
- Defines detailed query objectives and output requirements
- Specifies table formats with column definitions
- Includes processing instructions with step-by-step guidelines
- Sets quality requirements and search protocols
- Supports language customization (e.g., Russian output)

### Web Search Tool (tools.py)
- Integrates with Tavily Search API for web querying
- Configured to return comprehensive, trusted results
- Supports searching for current events and latest information
- Returns up to 10 search results per query

## Setup

1. Create a `.env` file with the following keys:
   - `OPENGPT_API_KEY`: Your OpenAI API key
   - `BASE_URL`: The API base URL
   - `TAVILY_API_KEY`: Your Tavily API key for web search

2. Install dependencies (see requirements.txt)

## Usage

Run the main.py script to execute the agent. By default, it will:
1. Initialize the LangGraph ReAct agent with the GPT-4.1-mini model
2. Execute a search for new generative AI implementation scenarios in September 2025
3. Apply rating filters and sorting criteria as specified in the prompt
4. Generate a visualization of the agent's reasoning process
5. Save the visualization as "react_graph.png"
6. Display the final response in the specified format and language

You can modify the query in the `agent.invoke()` call or update the SYSTEM_PROMPT in prompts.py to customize your search parameters.
## Output

The tool provides:
- A detailed text response to your query in the specified language
- Results formatted according to the prompt specifications (e.g., tables with ratings)
- A visual representation of the agent's reasoning process as a PNG image
- Search protocol statistics showing the filtering process

