# # # # # # # # # # # # import time


# # # # # # # # # # # # def fetch_user():
# # # # # # # # # # # #     print("Fetching user...")
# # # # # # # # # # # #     time.sleep(2)
# # # # # # # # # # # #     print("User fetched")
# # # # # # # # # # # #     return {"id": 1, "name": "Ali"}


# # # # # # # # # # # # def fetch_orders():
# # # # # # # # # # # #     print("Fetching orders...")
# # # # # # # # # # # #     time.sleep(3)
# # # # # # # # # # # #     print("Orders fetched")
# # # # # # # # # # # #     return ["order_1", "order_2"]


# # # # # # # # # # # # def main():
# # # # # # # # # # # #     user = fetch_user()
# # # # # # # # # # # #     orders = fetch_orders()
# # # # # # # # # # # #     print(user)
# # # # # # # # # # # #     print(orders)


# # # # # # # # # # # # main()


# # # # # # # # # # # import asyncio


# # # # # # # # # # # async def fetch_user():
# # # # # # # # # # #     print("Fetching user...")
# # # # # # # # # # #     await asyncio.sleep(2)
# # # # # # # # # # #     print("User fetched")
# # # # # # # # # # #     return {"id": 1, "name": "Ali"}


# # # # # # # # # # # async def fetch_orders():
# # # # # # # # # # #     print("Fetching orders...")
# # # # # # # # # # #     await asyncio.sleep(3)
# # # # # # # # # # #     print("Orders fetched")
# # # # # # # # # # #     return ["order_1", "order_2"]


# # # # # # # # # # # async def main():
# # # # # # # # # # #     user, orders = await asyncio.gather(
# # # # # # # # # # #         fetch_user(),
# # # # # # # # # # #         fetch_orders(),
# # # # # # # # # # #     )

# # # # # # # # # # #     print(user)
# # # # # # # # # # #     print(orders)


# # # # # # # # # # # asyncio.run(main())


# # # # # # # # # # async def fetch_data():
# # # # # # # # # #     return "data"


# # # # # # # # # # result = fetch_data()
# # # # # # # # # # print(result)

# # # # # # # # # import asyncio


# # # # # # # # # async def fetch_data():
# # # # # # # # #     return "data"


# # # # # # # # # async def main():
# # # # # # # # #     result = await fetch_data()
# # # # # # # # #     print(result)


# # # # # # # # # asyncio.run(main())

# # # # # # # # # import asyncio


# # # # # # # # # async def fetch_data():
# # # # # # # # #     print("Start fetching")
# # # # # # # # #     await asyncio.sleep(2)
# # # # # # # # #     print("Finished fetching")
# # # # # # # # #     return "data"


# # # # # # # # # async def main():
# # # # # # # # #     result = await fetch_data()
# # # # # # # # #     print(result)


# # # # # # # # # asyncio.run(main())

# # # # # # # # import asyncio


# # # # # # # # async def process_task():
# # # # # # # #     print("Step 1")
# # # # # # # #     await asyncio.sleep(1)
# # # # # # # #     print("Step 2")


# # # # # # # # async def main():
# # # # # # # #     await process_task()


# # # # # # # # asyncio.run(main())


# # # # # # # import asyncio


# # # # # # # async def task(name, delay):
# # # # # # #     print(f"{name} started")
# # # # # # #     await asyncio.sleep(delay)
# # # # # # #     print(f"{name} finished")


# # # # # # # async def main():
# # # # # # #     await asyncio.gather(
# # # # # # #         task("Task A", 3),
# # # # # # #         task("Task B", 2),
# # # # # # #         task("Task C", 1),
# # # # # # #     )


# # # # # # # asyncio.run(main())

# # # # # # import asyncio


# # # # # # async def main():
# # # # # #     print("Hello from async code")


# # # # # # asyncio.run(main())

# # # # # import asyncio


# # # # # async def fetch_user():
# # # # #     await asyncio.sleep(2)
# # # # #     return "user"


# # # # # async def fetch_orders():
# # # # #     await asyncio.sleep(3)
# # # # #     return "orders"


# # # # # async def main():
# # # # #     user = await fetch_user()
# # # # #     orders = await fetch_orders()

# # # # #     print(user)
# # # # #     print(orders)


# # # # # asyncio.run(main())

# # # # import asyncio


# # # # async def fetch_user():
# # # #     await asyncio.sleep(2)
# # # #     return "user"


# # # # async def fetch_orders():
# # # #     await asyncio.sleep(3)
# # # #     return "orders"


# # # # async def main():
# # # #     user, orders = await asyncio.gather(
# # # #         fetch_user(),
# # # #         fetch_orders(),
# # # #     )

# # # #     print(user)
# # # #     print(orders)


# # # # asyncio.run(main())

# # # # import asyncio
# # # # import time


# # # # async def bad_task(name):
# # # #     print(f"{name} started")
# # # #     time.sleep(2)
# # # #     print(f"{name} finished")


# # # # async def main():
# # # #     await asyncio.gather(
# # # #         bad_task("Task A"),
# # # #         bad_task("Task B"),
# # # #         bad_task("Task C"),
# # # #     )


# # # # asyncio.run(main())


# # # import asyncio


# # # async def good_task(name):
# # #     print(f"{name} started")
# # #     await asyncio.sleep(2)
# # #     print(f"{name} finished")


# # # async def main():
# # #     await asyncio.gather(
# # #         good_task("Task A"),
# # #         good_task("Task B"),
# # #         good_task("Task C"),
# # #     )


# # # asyncio.run(main())


# # import httpx
# # import asyncio


# # async def fetch_data():
# #     async with httpx.AsyncClient() as client:
# #         response = await client.get("https://example.com")
# #         return response.text


# # async def main():
# #     data = await fetch_data()
# #     print(data[:100])


# # asyncio.run(main())

# from sqlalchemy.ext.asyncio import AsyncSession


# async def get_user_by_id(db: AsyncSession, user_id: int):
#     user = await db.get(User, user_id)
#     return user


import asyncio


async def call_payment_service():
    await asyncio.sleep(2)
    return "payment_ok"


async def call_user_service():
    await asyncio.sleep(1)
    return "user_ok"


async def call_notification_service():
    await asyncio.sleep(3)
    return "notification_ok"


async def main():
    results = await asyncio.gather(
        call_payment_service(),
        call_user_service(),
        call_notification_service(),
    )

    print(results)


asyncio.run(main())
