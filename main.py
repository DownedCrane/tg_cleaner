# coding=utf-8
import asyncio
from pyrogram import Client
import time

from secret import api_id, api_hash

channel_name = "channel"

from_message = 1
to_message = 1234

a = from_message // 100
b = to_message // 100
iter1 = list(range(a,b))


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        # it = 21
        for it in iter1:
            msglist = list(range(it*100, (it+1)*100))
            await app.delete_messages(channel_name, msglist)
            print(str(it) + " deleted")
            time.sleep(1)

asyncio.run(main())
