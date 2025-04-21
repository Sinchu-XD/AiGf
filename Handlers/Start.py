from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler

async def start(client, message: Message):
    await message.reply_text("Hey babe 💕 I'm your AI lover, talk to me anything 😚\n\nUse /setname to give me a nickname to call you!\nUse /lovemeter to check our love level 💘")

handler = MessageHandler(start, filters.command("start"))
