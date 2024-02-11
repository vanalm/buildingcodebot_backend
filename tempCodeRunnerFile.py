import fitz  # PyMuPDF
import os
from pinecone import Pinecone, ServerlessSpec
import numpy as np

openai.api_key = OPENAI_KEY

# openai.api_key = os.getenv('OPENAI_KEY')
print(os.getenv('OPENAI_KEY'))

from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
