import os
from dotenv import load_dotenv
import openai


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2") == "true"
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT")


# Set the OpenAI API key globally for the OpenAI client
os.environ["OPENAI_API_KEY"]= OPENAI_API_KEY
openai.api_key = os.environ["OPENAI_API_KEY"]

# Optional: Raise an error if the API key is missing
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please check your .env file.")
