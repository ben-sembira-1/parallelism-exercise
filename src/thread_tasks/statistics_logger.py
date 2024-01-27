from cookies import COOKIE_TIME_LABEL, SLEEPING_LABEL
from interfaces import Session
from hz_loop import hz_loop
from log_statistics import LogStatistics, generate_statistics_from_time_lines
from rolling_file_lines_iterator import RollingFileLinesIterator
from time_row import extract_time, is_time_line


PERIOD_4_SECONDS_IN_HZ = 1 / 4


class StatisticsLogger:
    def __init__(self, session: Session):
        self._session = session
        self._time_lines_iterator = RollingFileLinesIterator(
            self._session.file_handle, is_time_line
        )

    def update_statistics(self):
        self._time_lines_iterator.update_rolling_file(self._session.file_handle)
        new_lines = list(self._time_lines_iterator.next_lines())
        statistics = generate_statistics_from_time_lines(new_lines)
        self._session.file_handle.write(statistics.to_line())

    def __call__(self) -> None:
        hz_loop(self.update_statistics, lambda: False, hz=PERIOD_4_SECONDS_IN_HZ)
