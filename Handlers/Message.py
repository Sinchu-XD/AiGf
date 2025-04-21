from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from Ai_chat import get_ai_reply
from gtts import gTTS
import os

async def ai_chat_handler(client, message: Message):
    if not message.text or message.text.startswith("/"):
        return

    reply = await get_ai_reply(message.from_user.id, message.text)
    await message.reply_text(reply)

    tts = gTTS(reply)
    tts.save("voice.mp3")
    await message.reply_voice("voice.mp3")
    os.remove("voice.mp3")

handler = MessageHandler(ai_chat_handler, filters.private)
