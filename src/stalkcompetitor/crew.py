import os
from dotenv import load_dotenv
load_dotenv()   # os.environ['SERPER_API_KEY'] and ['GOOGLE_API_KEY'] are set

import yaml
from crewai import Agent, Task, Crew, LLM
from stalkcompetitor.tools.search_tool import search_google

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def build_crew():
    agents_data = load_yaml("src/stalkcompetitor/config/agents.yaml")
    tasks_data = load_yaml("src/stalkcompetitor/config/tasks.yaml")

    agents = {}
    for name, data in agents_data.items():
        agents[name] = Agent(
            role=data["role"],
            goal=data["goal"],
            backstory=data["backstory"],
            verbose=data.get("verbose", False)
        )

    tasks = []
    for name, data in tasks_data.items():
        task_agent = agents[data["agent"]]
        task_tools = [search_google] if "tools" in data and "search_google" in data["tools"] else []
        tasks.append(Task(
            description=data["description"],
            expected_output=data["expected_output"],
            agent=task_agent,
            tools=task_tools
        ))

    llm = LLM(model="gemini/gemini-2.0-flash")
    crew = Crew(
        agents=list(agents.values()),
        tasks=tasks,
        llm=llm,
        verbose=True
    )
    return crew
