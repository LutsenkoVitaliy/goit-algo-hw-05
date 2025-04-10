# Перше завдання 

# def caching_fibonachi():
#   cache = {}
#   def fibonachi(n):
#     if n <= 0:
#       return 0
#     elif n == 1:
#       return 1
#     elif n in cache:
#       return cache[n]
#     else:
#       cache[n] = fibonachi(n-1) + fibonachi(n-2)
#       return cache[n]
#   return fibonachi

# fibo = caching_fibonachi()
# print(fibo(10))
# print(fibo(15))

# Друге завдання

# import re
# from typing import Callable, Generator

# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# def generator_numbers(text: str) -> Generator[float, None, None]:
#     for num in re.findall(r"\d+(?:\.\d+)", text):
#         yield float(num)

# def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
#     return sum(func(text))

# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")

# Третє завдання
