__all__ = ['get_time_ns', 'random_sleep', 'open_once', 'is_pressed', 'is_time_for_cookie']

from typing import List
import time
import random
from pathlib import Path
from io import TextIOWrapper

from keyboard import is_pressed

from parallelism_exercise_utils.runtime import cheating_check


cheating_check(Path(__file__).parent)


def get_time_ns() -> int:
    return time.time_ns()


def random_sleep() -> None:
    _random_less_then__0_05 = 0.01 * random.randrange(0, 6, 1)
    time.sleep(_random_less_then__0_05)


__OPENED_FILES: List[Path] = []
def open_once(file_path: str) -> TextIOWrapper:
    full_path = Path(file_path).absolute()
    if full_path in __OPENED_FILES:
        raise RuntimeError("The rules do not allow opening the same file twice.")
    __OPENED_FILES.append(full_path)
    return open(full_path, mode='w+')


def is_time_for_cookie(number: int) -> bool:
    import math
    return int(sum(math.cos(n) for n in range(number % 1_500_000))) % 2 == 0


if __name__ == "__main__":
    start=time.time()
    for i in range(39):
        print(is_time_for_cookie(time.time_ns()))
    print(time.time()-start)
