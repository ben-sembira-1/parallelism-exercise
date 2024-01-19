__all__ = ['get_time_ns', 'random_sleep', 'open_file_for_read_and_write']

from io import TextIOWrapper
from pathlib import Path
import random
import time
from typing import List

def get_time_ns() -> int:
    return time.time_ns()

def random_sleep() -> None:
    _random_less_then__0_05 = 0.01 * random.randrange(0, 6, 1)
    time.sleep(_random_less_then__0_05)

__OPENED_FILES: List[Path] = []
def open_file_for_read_and_write(file_path: str) -> TextIOWrapper:
    full_path = Path(file_path).absolute()
    if full_path in __OPENED_FILES:
        raise RuntimeError("The rules do not allow opening the same file twice.")
    __OPENED_FILES.append(full_path)
    return open(full_path, mode='w+')
    

if __name__ == "__main__":
    for i in range(10):
        print(time.time())
        random_sleep()
    with open_file_for_read_and_write("test1"):
        print(1)
    with open_file_for_read_and_write("test2"):
        print(2)
    with open_file_for_read_and_write("/home/ben/clones/parallelism-exercise/test1"):
        print(3)
