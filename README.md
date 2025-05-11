AI app that monitors your competitors by analyzing recent web news, classifying each one as good or bad, and generating an executive summary. Multiple AI Agents orchestrated by crewAI.

## Features

🌐 Searches the web for real-time news using Serper.dev (Search API)

🤖 Classifies articles as "Good News" or "Bad News" using CrewAI agents

📋 Generates a clear, structured competitor monitoring report

🧠 Built with Gemini as the LLM provider

🖥️ Flask-based minimalist web interface


## How It Works

1- User enters a company name on the frontend

2- A search agent uses Serper.dev to fetch recent news headlines

3- Two agents independently analyze and classify good vs. bad news

4- A final report-writing agent summarizes findings for executives

5- Report is displayed via a clean Flask web interface


## Folder Structure
```markdown
StalkCompetitor/
├── src/
│   └── stalkcompetitor/
│       ├── app.py              # Flask UI
│       ├── crew.py             # Crew + task execution
│       ├── tools/
│       │   └── search_tool.py  # Serper API integration
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── templates/
│           └── index.html      # UI template
├── .env                        # API keys
├── pyproject.toml / poetry.lock
└── README.md
```

## Add your secrets

Create a .env file:
```bash
GEMINI_API_KEY=your-openai-key
SERPER_API_KEY=your-serper-key
```
