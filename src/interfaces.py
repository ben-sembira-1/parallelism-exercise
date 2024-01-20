
from typing import Callable, Optional

from parallelism_exercise_utils import TextIOWrapper, open_once


class Session:
    def __init__(self):
        self.index = 0
        self.file_handle: Optional[TextIOWrapper] = None
        self.should_terminate = False

    def new_session(self):
        self.file_handle.close()
        self.index += 1
        self.file_handle = open_once(f"time.{self.index}.log")
