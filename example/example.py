# To allow example to just be runnable without pypi
import sys
sys.path.append(".")

from metro_integrase import Metro, BotPost
from fastapi import FastAPI

app = FastAPI()

metro = Metro(domain="https://example.com", list_id="a", secret_key="b", app=app)

@metro.claim()
async def claim(bot: BotPost):
    print("Claiming", bot)

@metro.unclaim()
async def unclaim(bot: BotPost):
    print("Unclaiming", bot)

@metro.approve()
async def approve(bot: BotPost):
    print("Approving", bot)

@metro.deny()
async def deny(bot: BotPost):
    print("Denying", bot)

print(metro._urls)

@app.on_event("startup")
async def setup():
    lists = await metro.http.get_all_lists()

    # Showcase the API by fetching the first list
    list_1 = await metro.http.get_list(lists[0].id)

    print(list_1, lists[0], list_1 == lists[0])

    bots = await metro.http.get_all_bots()

    bot_1 = await metro.http.get_bot(bots[0].bot_id)

    print(bot_1, bots[0], bot_1 == bots[0])

    print("Getting paginated actions")

    async for act in metro.paginate(metro.http.get_actions):
        print(act)

    # Finally setup the API endpoints
    await metro.register_api_urls()