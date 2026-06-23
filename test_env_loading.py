import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("LLMGW_API_KEY")
base_url = os.getenv("LLMGW_BASE_URL")

print(f"API Key loaded: {api_key is not None}")
print(f"Base URL: {base_url}")
print("✓ Environment variables are loading correctly")
