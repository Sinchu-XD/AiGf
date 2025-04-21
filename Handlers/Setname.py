from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from Utils.Userdata import set_name

async def setname_cmd(client, message: Message):
    parts = message.text.split(" ", 1)
    if len(parts) < 2:
        await message.reply_text("Please send a name like this:\n`/setname baby`")
        return

    name = parts[1]
    set_name(message.from_user.id, name)
    await message.reply_text(f"Got it! I'll call you **{name}** from now on 😚")

handler = MessageHandler(setname_cmd, filters.command("setname"))
