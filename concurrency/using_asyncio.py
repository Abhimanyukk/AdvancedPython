import asyncio

async def worker(name, delay):
    for i in range(5):
        await asyncio.sleep(delay)
        print(f"Worker {name}: {i}")

async def main():
    task1 = asyncio.create_task(worker("A", 1))
    task2 = asyncio.create_task(worker("B", 1.5))

    await task1
    await task2

asyncio.run(main())
print(f"Completed")