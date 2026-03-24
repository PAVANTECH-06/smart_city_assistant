import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('models/gemini-2.5-flash') # Using a common free-tier model

# Generate text from a text prompt
def response(query):
    prompt = query+" answer this query!"
    response = model.generate_content(prompt)
    return response.text
