try:
    from parallelism_exercise_utils import (
        random_sleep,
    )
except ImportError:
    raise ImportError("Did you pip install the utils package?")

from interfaces import Session
from thread_runner import threads_pull
from thread_tasks import (
    generate_time_logger,
    CookieUpdater,
    statistics_logger,
    session_switcher,
    soft_terminator,
)


def main():
    session = Session()
    threads_pull(
        (
            # generate_time_logger(session),
            CookieUpdater(session),
            # statistics_logger,
            # session_switcher,
            # soft_terminator,
        ),
    )
    while True:
        random_sleep()


if __name__ == "__main__":
    main()
