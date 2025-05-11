from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

load_dotenv()
search_google = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))