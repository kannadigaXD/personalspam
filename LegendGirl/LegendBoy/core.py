import datetime
import os
import sys
import time

from LegendBS.get_time import get_time
from pyrogram import Client, filters
from pyrogram.types import Message

from LegendGirl import start_time
from LegendGirl.Config import *

from .. import sudos
from ..core.clients import *


@Client.on_message(filters.user(sudos) & filters.command(["ping"], prefixes=HANDLER))
async def ping(_, e: Message):
    start = datetime.datetime.now()
    uptime = get_time((time.time() - start_time))
    a = await e.reply_text("Pong")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await a.delete()
    ping_temp = f"𝗧𝗘𝗔𝗠 𝗔𝗚𝗢𝗥𝗔 𝗦𝗣𝗔𝗠 𝗕𝗢𝗧𝗦\n\n👀 𝘿 𝘼 𝘿 𝘿 𝙔  👅: {ms}\n👀 𝙇 𝙄 𝙁 𝙏  🥵 𝙈 𝙀: {uptime}"
    for i in range(1, 26):
        lol = globals()[f"Client{i}"]
        if lol is not None:
            if ".jpg" in PING_PIC or ".png" in PING_PIC:
                await lol.send_photo(e.chat.id, PING_PIC, caption=ping_temp)
            elif ".mp4" in PING_PIC.lower():
                await lol.send_video(e.chat.id, PING_PIC, caption=ping_temp)
            else:
                await lol.send_message(e.chat.id, ping_temp)


@Client.on_message(
    filters.user(sudos) & filters.command(["restart", "reboot"], prefixes=HANDLER)
)
async def restarter(Legend: Client, message: Message):
    await message.reply_text(
        f"**Bot Is Restarting**\n\n Please Wait 5 min till bot is restart.\nAfter 5 Min Type {HANDLER}ping"
    )
    try:
        await Legend.stop()
    except Exception as error:
        print(str(error))

    args = [sys.executable, "-m", "LegendGirl"]
    os.execl(sys.executable, *args)
    quit()
