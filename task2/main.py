import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\b\d+\.\d+\b'
    for item in re.finditer(pattern, text):
        yield float(item.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))