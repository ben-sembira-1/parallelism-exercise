from interfaces import Session
from hz_loop import hz_loop


def soft_terminator(session: Session) -> None:
    hz_loop(lambda: session.file_handle.write("soft_terminator\n"), lambda: False, hz=1)
