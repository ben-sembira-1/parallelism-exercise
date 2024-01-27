from parallelism_exercise_utils import keyboard  # type: ignore
from interfaces import Session
from log_statistics import generate_statistics_from_time_lines
from rolling_file_lines_iterator import RollingFileLinesIterator
from time_row import is_time_line


class SessionSwitcher:
    def __init__(self, session: Session):
        self._session = session
        self._time_lines_iterator = RollingFileLinesIterator(
            self._session.file_handle, is_time_line
        )
        self._keyboard_listener = keyboard.Listener(on_press=self.switch_on_enter)

    def _write_statistics(self):
        new_lines = list(self._time_lines_iterator.next_lines())
        statistics = generate_statistics_from_time_lines(new_lines)
        self._session.file_handle.write(statistics.to_line())

    def switch_on_enter(self, key: keyboard.Key) -> None:
        self._time_lines_iterator.update_rolling_file(self._session.file_handle)
        if key == keyboard.Key.enter:
            self._write_statistics()
            self._session.new_session()

    def __call__(self) -> None:
        self._keyboard_listener.start()
