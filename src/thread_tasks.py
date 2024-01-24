from parallelism_exercise_utils.utils import (
    random_sleep,
    get_time_ns,
    APPEND_TO_END,
    is_time_for_cookie,
)
from interfaces import Session
from hz_loop import hz_loop


def time_logger(session: Session) -> None:
    def log_time():
        session.file_handle.write(
            f"[time] - {get_time_ns()}\n", start_point=APPEND_TO_END
        )

    hz_loop(log_time, lambda: False, hz=13)


def _cookie_update_single_row(
    row: str, index_to_cookie_update: int, session: Session
) -> None:
    if row.startswith("[time]"):
        should_cookie = is_time_for_cookie(int(row.lstrip("[time] - ")))
        should_cookie_label = "Cookie time" if should_cookie else "sleeping"
        session.file_handle.write(
            f" ({should_cookie_label})", start_point=index_to_cookie_update
        )


def cookie_updater(session: Session) -> None:
    NEW_LINE = "\n"
    END_OF_FILE = ""
    index_in_file = 0
    current_row = ""

    def update_cookies() -> None:
        while (
            next_char := session.file_handle.read(start_point=index_in_file, amount=1)
        ) != END_OF_FILE:
            if next_char != NEW_LINE:
                current_row += next_char
            else:
                _cookie_update_single_row(current_row, index_in_file - 1, session)
                current_row = ""

    hz_loop(update_cookies, lambda: False, hz=5)


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
