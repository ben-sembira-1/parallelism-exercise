try:
    from parallelism_exercise_utils import random_sleep  # type: ignore
except ImportError:
    raise ImportError("Did you pip install the utils package?")

from interfaces import Session
from thread_runner import threads_pull
from thread_tasks import (
    generate_time_logger,
    CookieUpdater,
    SessionSwitcher,
    soft_terminator,
    StatisticsLogger,
)


def main():
    session = Session()
    threads_pull(
        (
            generate_time_logger(session),
            CookieUpdater(session),
            StatisticsLogger(session),
            SessionSwitcher(session),
            # soft_terminator,
        ),
    )
    while True:
        random_sleep()


if __name__ == "__main__":
    main()
