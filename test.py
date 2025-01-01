from transformers import AutoTokenizer

# # Load the tokenizer
# tokenizer = AutoTokenizer.from_pretrained("google/pegasus-cnn_dailymail")

# # Save the tokenizer
# tokenizer.save_pretrained("D:/Projects/Google-TS/artifacts/model_trainer/tokenizer")

import os
tokenizer_path = "D:/Projects/Google-TS/artifacts/model_trainer/tokenizer"
if not os.path.exists(tokenizer_path):
    raise FileNotFoundError(f"Tokenizer path does not exist: {tokenizer_path}")
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)