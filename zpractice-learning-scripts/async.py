import asyncio

async def say_after(delay, message):
    # This coroutine waits for 'delay' seconds before printing the message
    await asyncio.sleep(delay)
    print(message)



async def main():
    print("Start")

    # Create two asynchronous tasks
    task1 = asyncio.create_task(say_after(2, "Hello"))
    task2 = asyncio.create_task(say_after(1, "World"))

    print("Tasks created, now waiting for them to finish...")

    # Wait until both tasks are finished
    await task1
    await task2

    print("End")

# Run the main coroutine
asyncio.run(main())
