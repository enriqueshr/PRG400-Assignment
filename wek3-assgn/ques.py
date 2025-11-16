import asyncio
import time

async def print_numbers():
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)

async def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        await asyncio.sleep(1.5)

async def main():
    start_time = time.time()
    await asyncio.gather(print_numbers(), print_letters())
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())