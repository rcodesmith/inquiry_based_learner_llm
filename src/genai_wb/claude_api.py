from itertools import chain
import os
import json
from typing import Iterable
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from anthropic.types import Message, MessageParam

from dotenv import load_dotenv

load_dotenv()

CLAUDE_MODEL = "claude-3-5-sonnet-20240620"

EMPTY_LIST = []

def extract_text(msg) -> str:
    txt = msg.content[0].text
    assert len(msg.content) == 1

    return txt

def extract_json(msg) -> dict:
    txt = extract_text(msg)

    try:
        return json.loads(txt)
    except json.JSONDecodeError:
        return {"error": "Failed to generate valid JSON", "raw_response": txt}

    
class GenAI:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def messages_create(self, system, messages: Iterable[MessageParam] | None = None,
                        user_text : str | None = None, temperature: float = 1.0) -> Message:
        user_message_iterable : Iterable[MessageParam]= [{"role": "user", "content": user_text}] if user_text is not None else EMPTY_LIST

        messages_combined = list(chain(messages, user_message_iterable)) if messages is not None else user_message_iterable

        msg = self.client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=2048,
            system=system, # <-- role prompt
            messages=messages_combined,
            temperature=temperature
        )
        return msg
