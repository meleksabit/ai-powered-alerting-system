import os
from transformers import pipeline

model_name = os.getenv("HF_MODEL_NAME", "distilbert-base-uncased-finetuned-sst-2-english")
cache_dir = os.getenv("MODEL_CACHE", "/model_cache")

pipeline("text-classification", model=model_name, tokenizer=model_name, cache_dir=cache_dir)
