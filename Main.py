from pyrogram import Client
from Config import API_ID, API_HASH, BOT_TOKEN
from Utils.Scheduler import schedule_daily_messages

from Handlers import Start, Message, Setname, Lovemeter

app = Client("ai_gf_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


USER_IDS = []

@app.on_message()
async def track_user(client, msg):
    if msg.chat.type == "private" and msg.from_user.id not in USER_IDS:
        USER_IDS.append(msg.from_user.id)

app.add_handler(Start.handler)
app.add_handler(Setname.handler)
app.add_handler(Lovemeter.handler)
app.add_handler(Message.handler)

schedule_daily_messages(app, USER_IDS)

print("✅ AI GF/BF Bot running...")
app.run()
