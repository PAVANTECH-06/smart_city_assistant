import google.generativeai as genai
import os

# The API key will be automatically picked up from the GOOGLE_API_KEY environment variable.
# If you used GEMINI_API_KEY, it will also be picked up, but GOOGLE_API_KEY takes precedence.

# Or, if you specifically set GEMINI_API_KEY:
genai.configure(api_key="AIzaSyDtcxjCmQynRWm__qMromDVEmYYwoXLTU4")

model = genai.GenerativeModel('gemini-1.5-flash') # Using a common free-tier model

# Generate text from a text prompt
def response(query):
    prompt = query+" answer this query!"
    response = model.generate_content(prompt)
    return response.text
