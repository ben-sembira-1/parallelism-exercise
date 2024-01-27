from interfaces import Session
from hz_loop import hz_loop


def statistics_logger(session: Session) -> None:
    hz_loop(lambda: session.file_handle.write("statistics_logger\n"), hz=1)


def session_switcher(session: Session) -> None:
    hz_loop(lambda: session.file_handle.write("session_switcher\n"), hz=1)


def soft_terminator(session: Session) -> None:
    hz_loop(lambda: session.file_handle.write("soft_terminator\n"), hz=1)
