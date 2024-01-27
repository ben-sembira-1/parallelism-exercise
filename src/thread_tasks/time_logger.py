from typing import Callable
from parallelism_exercise_utils.utils import (
    get_time_ns,
    APPEND_TO_END,
)
from interfaces import Session
from hz_loop import hz_loop
import time_row


def generate_time_logger(session: Session) -> Callable[[], None]:
    def time_logger() -> None:
        def log_time():
            session.file_handle.write(
                time_row.create_line(get_time_ns()), start_point=APPEND_TO_END
            )

        hz_loop(log_time, lambda: False, hz=13)

    return time_logger
