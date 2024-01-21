from parallelism_exercise_utils import random_sleep, get_time_ns
from interfaces import Session

def time_logger(session: Session) -> None:

    while True:
        session.file_handle.write("time_logger\n")
        random_sleep()


def cookie_updater(session: Session) -> None:
    while True:
        session.file_handle.write("cookie_updater\n")
        random_sleep()


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
