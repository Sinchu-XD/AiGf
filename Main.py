import asyncio
from pyrogram import Client
from Config import API_ID, API_HASH, BOT_TOKEN
from Handlers.Start import handler as start_handler
from Handlers.Setname import handler as setname_handler
from Utils.Scheduler import schedule_daily_messages
from Utils.Userdata import load_data

app = Client("ai_gf_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def main():
    user_data = load_data()
    user_ids = list(user_data.keys())

    app.add_handler(start_handler)
    app.add_handler(setname_handler)

    schedule_daily_messages(app, user_ids)

    await app.start()
    print("Bot is running...")
    await asyncio.get_event_loop().create_future()

if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
