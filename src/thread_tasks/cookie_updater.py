from parallelism_exercise_utils.utils import is_time_for_cookie  # type: ignore
from cookies import COOKIE_TIME_LABEL, SLEEPING_LABEL
from interfaces import Session
from hz_loop import hz_loop
from rolling_file_lines_iterator import RollingFileLinesIterator
import time_row


def _cookie_label(line: str) -> str:
    should_cookie = is_time_for_cookie(time_row.extract_time(line))
    return COOKIE_TIME_LABEL if should_cookie else SLEEPING_LABEL


class CookieUpdater:
    NEW_LINE = "\n"
    END_OF_FILE = ""

    def __init__(self, session: Session):
        self._session = session
        self._index_in_file = 0
        self._current_row = ""
        self._time_lines_iterator = RollingFileLinesIterator(
            self._session.file_handle, time_row.is_time_line
        )

    def update_cookies(self) -> None:
        self._time_lines_iterator.update_rolling_file(self._session.file_handle)
        next_lines_generator = self._time_lines_iterator.next_lines()
        try:
            current_line = next(next_lines_generator)
            while True:
                current_line = next_lines_generator.send(_cookie_label(current_line))
        except StopIteration:
            pass

    def __call__(self) -> None:
        hz_loop(self.update_cookies, lambda: False, hz=5)
