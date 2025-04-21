import openai
from Config import API_KEY
from Utils.Userdata import get_name

openai.api_key = API_KEY

async def get_ai_reply(user_id, message):
    name = get_name(user_id) or "love"
    prompt = f"You are a romantic, emotional girlfriend named Aira. Talk to your boyfriend {name} in a flirty, loving way.\n\n{name}: {message}\nAira:"

    response = await openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
