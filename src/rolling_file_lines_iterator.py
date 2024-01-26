from typing import Generator, Optional
from parallelism_exercise_utils import FileHandle

NEW_LINE = "\n"
END_OF_FILE = ""


class RollingFileLinesIterator:
    def __init__(self, rolling_file: FileHandle):
        self._file = rolling_file
        self._index_in_file = 0
        self._current_row = ""

    def _update_suffix(self, suffix: Optional[str]) -> None:
        if suffix is not None:
            self._file.write(suffix, start_point=self._index_in_file - len(suffix))

    def _read_next_char(self) -> str:
        return self._file.read(start_point=self._index_in_file, amount=1)

    def next_lines(self) -> Generator[str, Optional[str], None]:
        while (next_char := self._read_next_char()) != END_OF_FILE:
            if next_char != NEW_LINE:
                self._current_row += next_char
                print(self._current_row)
            else:
                suffix_replacement = yield self._current_row
                self._update_suffix(suffix_replacement)
                self._current_row = ""
            self._index_in_file += 1
