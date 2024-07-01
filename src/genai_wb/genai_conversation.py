from itertools import chain
import json
from typing import Iterable

from anthropic.types import Message, MessageParam

from genai_wb.claude_api import GenAI


class GenAIConversation:
    genai_api: GenAI

    messages = []

    def __init__(self, genai_api: GenAI, system_prompt: str):
        self.genai_api = genai_api
        self.messages = []
        self.system_prompt = system_prompt

    def messages_create(self, message: MessageParam | None = None,
                        user_text : str | None = None, temperature: float = 1.0) -> Message:
        
        msg, messages = self.genai_api.messages_create(self.system_prompt, messages=self.messages, message=message, user_text=user_text, temperature=temperature)
        self.messages = messages
        self.messages.append({"role": msg.role, "content": msg.content})

        return msg
