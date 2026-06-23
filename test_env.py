import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("ANTHROPIC_API_KEY")

print("Key found:", key is not None)
print("Length:", len(key) if key else 0)

if key:
    print("Starts with:", key[:15])