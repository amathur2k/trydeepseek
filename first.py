# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "How to catch a data scientist?"},
]
pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")
print(pipe(messages))