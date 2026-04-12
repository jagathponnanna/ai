from google import genai
import os

# Initialize client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

SYSTEM_PROMPT = "You are a helpful AI assistant."

def generate_reply(messages):
    """
    messages = [
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": "..."}
    ]
    """

    # Build prompt (Gemini no longer manages chat history automatically)
    prompt = SYSTEM_PROMPT + "\n\n"

    for m in messages:
        prompt += f"{m['role']}: {m['content']}\n"

    # Call Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",   # or gemini-2.5-flash if enabled
        contents=prompt,
        config={
            "temperature": 0.7,
            "max_output_tokens": 500,
        }
    )

    return response.text