import google.generativeai as genai
from Utils.Userdata import get_name
from Config import API_KEY


genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="gemini-pro")

async def get_ai_reply(user_id, message):
    name = get_name(user_id) or "love"
    prompt = f"You are a romantic, emotional girlfriend named Aira. Talk to your boyfriend {name} in a flirty, loving way.\n\n{name}: {message}\nAira:"

    response = model.generate_content(prompt)
    return response.text.strip()
