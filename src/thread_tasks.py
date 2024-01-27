from typing import Callable
from parallelism_exercise_utils.utils import (
    random_sleep,
    get_time_ns,
    APPEND_TO_END,
    is_time_for_cookie,
)
from interfaces import Session
from hz_loop import hz_loop
from rolling_file_lines_iterator import RollingFileLinesIterator
import time_row


def generate_time_logger(session: Session) -> Callable[[], None]:
    def time_logger() -> None:
        def log_time():
            session.file_handle.write(
                time_row.create_line(get_time_ns()), start_point=APPEND_TO_END
            )

        hz_loop(log_time, lambda: False, hz=13)

    return time_logger


def _cookie_label(line: str) -> str:
    NO_LABEL = ""
    if not time_row.is_time_line(line):
        return NO_LABEL

    should_cookie = is_time_for_cookie(time_row.extract_time(line))
    should_cookie_label = "Cookie time" if should_cookie else "sleeping"
    return f"({should_cookie_label})"


class CookieUpdater:
    NEW_LINE = "\n"
    END_OF_FILE = ""

    def __init__(self, session: Session):
        self._session = session
        self._index_in_file = 0
        self._current_row = ""
        self._file_lines = RollingFileLinesIterator(self._session.file_handle)

    def update_cookies(self) -> None:
        next_lines_generator = self._file_lines.next_lines()
        try:
            current_line = next(next_lines_generator)
            while True:
                current_line = next_lines_generator.send(
                    _cookie_label(current_line))
        except StopIteration:
            pass

    def __call__(self) -> None:
        hz_loop(self.update_cookies, lambda: False, hz=5)


def statistics_logger(session: Session) -> None:
    while True:
        session.file_handle.write("statistics_logger\n")
        random_sleep()


def session_switcher(session: Session) -> None:
    while True:
        session.file_handle.write("session_switcher\n")
        random_sleep()


def soft_terminator(session: Session) -> None:
    while True:
        session.file_handle.write("soft_terminator\n")
        random_sleep()
