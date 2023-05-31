import asyncio

async def my_async_function():
    # your async function code here
    print("This is my async function.")

async def call_async_function_every_minute():
    while True:
        await my_async_function()
        await asyncio.sleep(60)  # wait for 60 seconds (1 minute)

#asyncio.run(call_async_function_every_minute())

import dictionaries

for subject in dictionaries.dict_subject:
    print((type(subject)))