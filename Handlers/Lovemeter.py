from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
import random

async def love_meter(client, message: Message):
    percent = random.randint(60, 100)
    emojis = "❤️" * (percent // 10)
    await message.reply_text(f"Your love meter is at **{percent}%** today!\n{emojis} 😘")

handler = MessageHandler(love_meter, filters.command("lovemeter"))
