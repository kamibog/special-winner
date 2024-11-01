import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование.')

    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач{name} поднял {i} шар.')

    print(f'Силач{name} закончил соревнования.')


async def start_tournament():
    task = []
    task.append(start_strongman('Pasha', 3))
    task.append(start_strongman('Denis', 4))
    task.append(start_strongman('Apollon', 5))

    await asyncio.gather(*task)


asyncio.run(start_tournament())
