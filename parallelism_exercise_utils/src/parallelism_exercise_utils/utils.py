from typing import List, Optional
import time
import random
from pathlib import Path
from io import TextIOWrapper

if __name__ == "__main__":
    from runtime import cheating_check
else:
    from .runtime import cheating_check


# cheating_check(Path(__file__).parent)


def get_time_ns() -> int:
    return time.time_ns()


def random_sleep() -> None:
    _random_less_then__0_05 = 0.01 * random.randrange(0, 6, 1)
    time.sleep(_random_less_then__0_05)


READ_ALL = None
APPEND_TO_END = None


class FileHandle:
    def __init__(self, path: str):
        self.__path = Path(path)
        self.__path.unlink(missing_ok=True)

    def _write_single_char(self, position: int, char: str):
        time.sleep(1e-4)
        assert len(char) == 1, "Writing only single chars."
        with open(self.__path, mode="r+") as f:
            f.seek(position)
            f.write(char)

    def _read_single_char(self, position: int) -> str:
        time.sleep(1e-4)
        with open(self.__path, mode="r") as f:
            f.seek(position)
            return f.read(1)

    def _len_of_file(self) -> int:
        return len(self.__path.read_text()) if self.__path.exists() else 0

    def write(self, string: str, start_point: Optional[int] = APPEND_TO_END):
        self.__path.touch()
        index = start_point if start_point is not APPEND_TO_END else self._len_of_file()
        for char in string:
            self._write_single_char(index, char)
            index += 1

    def read(self, start_point: int = 0, amount: Optional[int] = READ_ALL) -> str:
        read_until = self._len_of_file() if amount == READ_ALL else start_point + amount
        response = "".join(
            self._read_single_char(index) for index in range(start_point, read_until)
        )
        return response


def is_time_for_cookie(number: int) -> bool:
    import math

    return int(sum(math.cos(n) for n in range(number % 1_500_000))) % 2 == 0


if __name__ == "__main__":
    pass
