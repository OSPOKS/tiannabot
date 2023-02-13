# credits @RoseLoverX
from Tianabot import telethn as tbot
from Tianabot.events import register
import os
import asyncio
import os
import time
from datetime import datetime
from Tianabot import OWNER_ID
from Tianabot import TEMP_DOWNLOAD_DIRECTORY as path
from Tianabot import TEMP_DOWNLOAD_DIRECTORY
from datetime import datetime
water = './Tianabot/resources/IMG_20210215_151841_124.jpg'
client = tbot

@register(pattern=r"^/send ?(.*)")
async def Prof(event):
    if event.sender_id != OWNER_ID:
        return
    thumb = water
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = f"./Tianabot/modules/{input_str}.py"
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
             force_document=True,
             allow_cache=False,
             thumb=thumb,
             reply_to=message_id,
         )
    else:
        await event.reply("No File Found!")


from Tianabot.events import load_module
import asyncio
import os
from datetime import datetime
from pathlib import Path

@register(pattern="^/install")
async def install(event):
    if event.fwd_from:
        return
    if event.sender_id != OWNER_ID:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "Tianabot/modules/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.reply(
                    f"Installed.... 👍\n `{os.path.basename(downloaded_file_name)}`"
                )
            else:
                os.remove(downloaded_file_name)
                k = await event.reply("**Error!**\n⚠️Cannot Install! \n📂 File not supported \n Or Pre Installed Maybe..😁",
                )
                await asyncio.sleep(2)
                await k.delete()
        except Exception as e:  # pylint:disable=C0103,W0703
            j = await event.reply(str(e))
            await asyncio.sleep(3)
            await j.delete()
            os.remove(downloaded_file_name)
    await asyncio.sleep(3)
    await event.delete()

from Tianabot import telethn as tbot, OWNER_ID, DEV_USERS
from Tianabot.events import register
import os
import asyncio
import os
import time
from datetime import datetime
from Tianabot import TEMP_DOWNLOAD_DIRECTORY as path
from Tianabot import TEMP_DOWNLOAD_DIRECTORY
from datetime import datetime
import asyncio
import os
import time
from datetime import datetime as dt
opn = []

@register(pattern="/open")
async def _(event):
    xx = await event.reply("Processing...")
    if not event.reply_to_msg_id:
        return await event.reply("Reply to a readable file")
    a = await event.get_reply_message()
    if not a.media:
        return await event.reply("Reply to a readable file")
    b = await a.download_media()
    with open(b, "r") as c:
        d = c.read()
    n = 4096
    for bkl in range(0, len(d), n):
        opn.append(d[bkl : bkl + n])
    for bc in opn:
        await event.client.send_message(
            event.chat_id,
            f"{bc}",
            reply_to=event.reply_to_msg_id,
        )
    await event.delete()
    opn.clear()
    os.remove(b)
    await xx.delete()

client = tbot
import time
from io import BytesIO
from pathlib import Path
from Tianabot import telethn as borg
from telethon import functions, types
from telethon.errors import PhotoInvalidDimensionsError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import SendMediaRequest


@register(pattern="^/make ?(.*)")
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.reply("reply to text message as `.ttf <file name>`")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.reply("reply to text message as `.ttf <file name>`")
