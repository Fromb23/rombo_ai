from transformers import AutoTokenizer
import json

# Load the pre-trained tokenizer (e.g., GPT-2)
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Set the padding token (if not already set)
tokenizer.pad_token = tokenizer.eos_token  # Or set a custom token like '[PAD]'

# Load your output_data.json file
with open("output_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Tokenize the questions and answers
input_texts = [entry["title"] for entry in data]
output_texts = [entry["answer"] for entry in data]

# Tokenizing the input (questions) and output (answers)
input_ids = tokenizer(input_texts, padding=True, truncation=True, return_tensors="pt").input_ids
output_ids = tokenizer(output_texts, padding=True, truncation=True, return_tensors="pt").input_ids

print(f"Tokenized input (question) IDs: {input_ids}")
print(f"Tokenized output (answer) IDs: {output_ids}")
