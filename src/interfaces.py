
from typing import Callable, Optional

from parallelism_exercise_utils import TextIOWrapper, FileHandle


class Session:
    def __init__(self):
        self.index = 0
        self.file_handle: Optional[TextIOWrapper] = None
        self.should_terminate = False

    def new_session(self):
        self.index += 1
        self.file_handle = FileHandle(f"time.{self.index}.log")
