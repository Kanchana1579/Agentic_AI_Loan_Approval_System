import os
from dotenv import load_dotenv

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
anthropic_base_url = os.getenv("ANTHROPIC_BASE_URL", "https://llmgw-wp.tekstac.com")

if not anthropic_api_key:
    raise ValueError("ANTHROPIC_API_KEY not found in environment")

os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key
os.environ["ANTHROPIC_BASE_URL"] = anthropic_base_url