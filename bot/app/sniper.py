import asyncio
import json

import aiofiles

from requests_html import AsyncHTMLSession
from bot.misc.util import api_url


async def get_data_by_api(url: str) -> str:
    session = AsyncHTMLSession()
    try:
        response = await session.get(url)
        await response.html.arender(sleep=60)
        html = response.html.raw_html
        await session.close()

        return html

    except Exception as e:
        print(f"Err: {e}")


async def repeat_request() -> None:
    while True:
        data = await get_data_by_api(api_url)
        if data:
            async with aiofiles.open('bot/app/open.json', mode='w', encoding='utf-8') as file:
                json_data = json.dumps(data)
                await file.write(json_data)

        await asyncio.sleep(10)
