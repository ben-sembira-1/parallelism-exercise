from typing import List, Optional
import time
import random
from pathlib import Path
from io import TextIOWrapper

if __name__ == "__main__":
    from runtime import cheating_check
else:
    from .runtime import cheating_check


cheating_check(Path(__file__).parent)


def get_time_ns() -> int:
    return time.time_ns()


def random_sleep() -> None:
    _random_less_then__0_05 = 0.01 * random.randrange(0, 6, 1)
    time.sleep(_random_less_then__0_05)


READ_ALL = None
class FileHandle:
    def __init__(self, path: str):
        self.path = path
    
    def _write_single_char(self, position: int, char: str):
        assert len(char) == 1, "Writing only single chars."
        with open(self.path, mode='w') as f:
                f.seek(position)
                f.write(char)
    
    def _read_single_char(self, position: int) -> str:
        with open(self.path, mode='r') as f:
                f.seek(position)
                return f.read(1)
    
    def _len_of_file(self) -> int:
         return len(Path(self.path).read_text())
    
    def write(self, string: str, start_point: Optional[int] = None):
        index = start_point if start_point is not None else self._len_of_file()
        for char in string:
            self._write_single_char(index, char)
            index += 1
    
    def read(self, start_point: int = 0, amount: Optional[int] = READ_ALL) -> str:
        file_size = self._len_of_file()
        return "".join(self._read_single_char(index) for index in range(start_point, file_size))


def is_time_for_cookie(number: int) -> bool:
    import math
    return int(sum(math.cos(n) for n in range(number % 1_500_000))) % 2 == 0


if __name__ == "__main__":
    pass
