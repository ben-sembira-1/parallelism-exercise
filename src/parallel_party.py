import typing
import threading
try:
    from parallelism_exercise_utils import is_pressed, get_time_ns, random_sleep, is_time_for_cookie
except ImportError:
    raise ImportError("Did you pip install the utils package?")

from interfaces import Session
from thread_runner import threads_pull_same_args
from thread_tasks import time_logger, cookie_updater, statistics_logger, session_switcher, soft_terminator


def main():
    session = Session()
    session.new_session()
    # threads_pull_same_args((time_logger,), session)
    threads_pull_same_args((time_logger, cookie_updater,
                            statistics_logger, session_switcher, soft_terminator), session)
    while True:
        random_sleep()


if __name__ == "__main__":
    main()
