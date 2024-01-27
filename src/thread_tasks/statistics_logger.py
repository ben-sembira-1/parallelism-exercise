from interfaces import Session
from hz_loop import hz_loop
from rolling_file_lines_iterator import RollingFileLinesIterator


PERIOD_4_SECONDS_IN_HZ = 1 / 4


class StatisticsLogger:
    def __init__(self, session: Session):
        self._session = session
        self._file_lines = RollingFileLinesIterator(self._session.file_handle)

    def __call__(self) -> None:
        hz_loop(
            lambda: self._session.file_handle.write("statistics_logger\n"),
            lambda: False,
            hz=PERIOD_4_SECONDS_IN_HZ,
        )
