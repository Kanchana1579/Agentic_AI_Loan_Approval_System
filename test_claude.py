import os
import sys
from dotenv import load_dotenv

load_dotenv()

from anthropic import Anthropic

client = Anthropic()

response = client.messages.create(
    model="global.anthropic.claude-sonnet-4-6",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Say hello"
        }
    ]
)

print(response.content[0].text)