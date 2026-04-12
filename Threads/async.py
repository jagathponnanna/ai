import asyncio

async def fetch(name):
    print(f"Fetching {name}")
    await asyncio.sleep(2)   # simulate I/O
    print(f"Done {name}")
    return name

async def main():
    start = asyncio.get_event_loop().time()

    results = await asyncio.gather(
        fetch("A"),
        fetch("B"),
        fetch("C")
    )

    print("Results:", results)
    print("Time:", asyncio.get_event_loop().time() - start)

asyncio.run(main())