import asyncio
from pyrogram import Client, filters
from Config import API_ID, API_HASH, BOT_TOKEN
from Handlers import Start, Message, Setname, Lovemeter
from Utils.Scheduler import schedule_daily_messages
from Utils.Userdata import load_data

app = Client("ai_gf_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

Start.handler = start
Message.handler = message
Setname.handler = setname
Lovemeter.handler = lovemeter

CHAT_USERNAME = "@nusickatic"
USER_IDS = []

@app.on_message()
async def track_user(client, msg):
    if msg.chat.type == "private" and msg.from_user.id not in USER_IDS:
        USER_IDS.append(msg.from_user.id)

async def main():
    app.add_handler(start)
    app.add_handler(setname)
    app.add_handler(lovemeter)
    app.add_handler(message)

    schedule_daily_messages(app, USER_IDS)
    await app.start()
    print("Bot is running...")
    await app.send_message(CHAT_USERNAME, "✅ Bot has started!")
    
    await asyncio.get_event_loop().create_future()

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print("🛑 Bot stopped manually.")

