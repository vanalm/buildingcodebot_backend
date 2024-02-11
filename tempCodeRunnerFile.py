import fitz  # PyMuPDF
import os
from pinecone import Pinecone, ServerlessSpec
import numpy as np

PINECONE_KEY="a6bc829e-961f-4cda-b8cb-bf283cf6b032"
OPENAI_KEY = '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'
# print("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" == OPENAI_KEY)
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
