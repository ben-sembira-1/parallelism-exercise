from typing import Callable
from parallelism_exercise_utils.utils import (
    random_sleep,
    get_time_ns,
    APPEND_TO_END,
    is_time_for_cookie,
)
from interfaces import Session
from hz_loop import hz_loop


def generate_time_logger(session: Session) -> Callable[[], None]:
    def time_logger() -> None:
        def log_time():
            session.file_handle.write(
                f"[time] - {get_time_ns()}\n", start_point=APPEND_TO_END
            )

        hz_loop(log_time, lambda: False, hz=13)

    return time_logger


class CookieUpdater:
    NEW_LINE = "\n"
    END_OF_FILE = ""

    def __init__(self, session: Session):
        self._session = session
        self._index_in_file = 0
        self._current_row = ""

    @staticmethod
    def _cookie_update_single_row(
        row: str, index_to_cookie_update: int, session: Session
    ) -> None:
        if row.startswith("[time]"):
            print(f"Good row!, {index_to_cookie_update=}")
            should_cookie = is_time_for_cookie(int(row.lstrip("[time] - ")))
            should_cookie_label = "Cookie time" if should_cookie else "sleeping"
            session.file_handle.write(
                f" ({should_cookie_label})", start_point=index_to_cookie_update
            )

    def update_cookies(self) -> None:
        while (
            next_char := self._session.file_handle.read(
                start_point=self._index_in_file, amount=1
            )
        ) != CookieUpdater.END_OF_FILE:
            if next_char != CookieUpdater.NEW_LINE:
                self._current_row += next_char
                print(self._current_row)
            else:
                CookieUpdater._cookie_update_single_row(
                    self._current_row, self._index_in_file, self._session
                )
                self._current_row = ""
            self._index_in_file += 1

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
