# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "How to find a data scientist?"},
]
#pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B")
#pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B")
pipe = pipeline("text-generation", model="deepseek-ai/deepseek-coder-1.3b-instruct")
print(pipe(messages))
