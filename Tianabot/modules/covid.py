from Tianabot import pbot as app
from Tianabot.pyrogramee.errors import capture_err
from Tianabot.pyrogramee.json_prettify import json_prettify
from Tianabot.pyrogramee.fetch import fetch
from pyrogram import filters


@app.on_message(filters.command("covid") & ~filters.edited)
@capture_err
async def covid(_, message):
    if len(message.command) == 1:
        data = await fetch("https://corona.lmao.ninja/v2/all")
        data = await json_prettify(data)
        await app.send_message(message.chat.id, text=data)
        return
    country = message.text.split(None, 1)[1].strip()
    country = country.replace(" ", "")
    data = await fetch(f"https://corona.lmao.ninja/v2/countries/{country}")
    data = await json_prettify(data)
    await app.send_message(message.chat.id, text=data)
    return
