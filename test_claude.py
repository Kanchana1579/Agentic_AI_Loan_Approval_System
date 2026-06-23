import os

from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

try:

    response = client.messages.create(
        model="global.anthropic.claude-haiku-4-5-20251001-v1:0",
        max_tokens=100,
        messages=[
            {
                "role": "user",
                "content": "Say hello and confirm you are working."
            }
        ]
    )

    print("✅ Claude Connection Successful")
    print(response.content[0].text)

except Exception as e:

    print("❌ Claude Connection Failed")
    print(e)