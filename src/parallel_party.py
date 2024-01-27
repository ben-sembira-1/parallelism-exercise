try:
    from parallelism_exercise_utils import (  # type: ignore
        random_sleep,
    )
except ImportError:
    raise ImportError("Did you pip install the utils package?")

from interfaces import Session
from thread_runner import threads_pull
from thread_tasks import (
    generate_time_logger,
    CookieUpdater,
    session_switcher,
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
            # session_switcher,
            # soft_terminator,
        ),
    )
    while True:
        random_sleep()


if __name__ == "__main__":
    main()
