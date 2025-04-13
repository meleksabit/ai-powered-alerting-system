from transformers import AutoModelForSequenceClassification, AutoTokenizer

print("⏬ Downloading Hugging Face model and tokenizer...")
AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english", cache_dir="/model_cache")
AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english", cache_dir="/model_cache")
print("✅ Model and tokenizer downloaded successfully!")
