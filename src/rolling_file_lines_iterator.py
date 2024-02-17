from typing import Callable, Generator, Optional
from parallelism_exercise_utils import FileHandle  # type: ignore

NEW_LINE = "\n"
END_OF_FILE = ""


class RollingFileLinesIterator:
    def __init__(
        self,
        rolling_file: FileHandle,
        lines_filter: Callable[[str], bool] = lambda _: True,
    ):
        self._file = rolling_file
        self._index_in_file = 0
        self._current_row = ""
        self._filter = lines_filter

    def _update_suffix(self, suffix: Optional[str]) -> None:
        NEW_LINE_CHARACTER_LENGTH = 1
        if suffix is not None:
            self._file.write(
                suffix,
                start_point=self._index_in_file
                - len(suffix)
                - NEW_LINE_CHARACTER_LENGTH,
            )

    def _read_next_char(self) -> str:
        try:
            return self._file.read(start_point=self._index_in_file, amount=1)
        except FileNotFoundError:
            print("File not found, not reading anything.")
            return END_OF_FILE

    def next_lines(self) -> Generator[str, Optional[str], None]:
        while (next_char := self._read_next_char()) != END_OF_FILE:
            self._index_in_file += 1
            if next_char != NEW_LINE:
                self._current_row += next_char
                continue
            if self._filter(self._current_row):
                suffix_replacement = yield self._current_row
                self._update_suffix(suffix_replacement)
            self._current_row = ""

    def update_rolling_file(self, rolling_file: FileHandle):
        if self._file is not rolling_file:
            self._file = rolling_file
            self._index_in_file = 0
            self._current_row = ""
