from parallelism_exercise_utils import TextIOWrapper, FileHandle


class Session:
    def __init__(self) -> None:
        self.index = 0
        self.file_handle: TextIOWrapper = FileHandle(f"time.{self.index}.log")
        self.should_terminate = False

    def new_session(self):
        self.index += 1
        self.file_handle = FileHandle(f"time.{self.index}.log")
