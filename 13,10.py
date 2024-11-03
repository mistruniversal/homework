# import aiohttp
# import asyncio
#
# urls = [
#     "https://filesamples.com/samples/document/txt/sample3.txt",
#     "https://filesamples.com/samples/document/txt/sample2.txt",
#     "https://filesamples.com/samples/document/txt/sample1.txt"
# ]
#
#
# async def download_file(session, url):
#     filename = url.split("/")[-1]
#     async with session.get(url) as response:
#         with open(filename, 'wb') as f:
#             f.write(await response.read())
#         print(f'{filename} загружен')
#
#
# async def download_all_files(urls):
#     async with aiohttp.ClientSession() as session:
#         tasks = [download_file(session, url) for url in urls]
#         await asyncio.gather(*tasks)
#
#
# asyncio.run(download_all_files(urls))













# import asyncio
#
# async def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return await fib(n - 1) + await fib(n - 2)
#
# async def compute_fibonacci(numbers):
#     tasks = [fib(num) for num in numbers]
#     results = await asyncio.gather(*tasks)
#
#     for num, result in zip(numbers, results):
#         print(f"Fibonacci({num}) = {result}")
#
#
#
# numbers = [10, 20, 30]
#
#
# asyncio.run(compute_fibonacci(numbers))
#
#
# 3 Обработка данных (фильтрация списка)
# data = [i for i in range(1, 101)]
#
# def filter_data(data):
#     return [x for x in data if x % 2 == 0]  #
#
# filtered_data = filter_data(data)
# print(f"Отфильтрованные данные: {filtered_data}")