# # from config.model_config import load_config

# # cfg = load_config()

# # print(cfg.model)
# # print(cfg.debugging_app.explanation_language)

# # -------------------------------------------------
# import os
# from dotenv import load_dotenv
# from huggingface_hub import InferenceClient

# # 1. Load your hidden .env file
# load_dotenv()
# hf_token = os.environ.get("HF_TOKEN")

# # 2. Initialize the client with your token
# client = InferenceClient(token=hf_token)

# # 3. Use chat.completions.create and specify a model (like Llama 3)
# response = client.chat.completions.create(
#     model="meta-llama/Meta-Llama-3-8B-Instruct", 
#     messages=[{"role": "user", "content": "tell me the one riches person in mharastra ?"}],
#     max_tokens=500
# )

# # 4. Print out the text response
# print(response.choices[0].message.content)
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from utils.debugging_helper import build_debugging_promt

# Load your Hugging Face API key
load_dotenv()

# Initialize the Hugging Face client with your token
client = InferenceClient(token=os.getenv("HF_TOKEN"))

user_code = "s=6  print(s) "
prompt = build_debugging_promt(user_code)

# FIX: Using chat completion structure satisfies the provider requirements
response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct", 
    messages=[{"role": "user", "content": prompt}]
)

# Extract and print the final result string
result = response.choices[0].message.content
print(result)