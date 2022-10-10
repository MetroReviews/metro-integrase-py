# To allow example to just be runnable without pypi
import sys
sys.path.append(".")

from metro_integrase import Metro, Bot
from fastapi import FastAPI

app = FastAPI()

metro = Metro(domain="https://example.com", list_id="a", secret_key="b", app=app)

# @metro.claim defines a new claim API endpoint, and vice versa for the other @metro.unclaim/approve/deny
@metro.claim()
async def claim(bot: Bot):
    print("Claiming", bot)

@metro.unclaim()
async def unclaim(bot: Bot):
    print("Unclaiming", bot)

@metro.approve()
async def approve(bot: Bot):
    print("Approving", bot)

@metro.deny()
async def deny(bot: Bot):
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

    # Finally setup the API endpoints, this must be done after all the @metro.* decorators to ensure they are registered with Metro Reviews
    await metro.register_api_urls()

# More things you can do
# 
# metro.http.add_bot(...)
# metro.http.approve_bot(...)
# metro.http.deny_bot(...)
# etc.