from dataclasses import dataclass
from typing import Iterable, List
from cookies import COOKIE_TIME_LABEL, SLEEPING_LABEL

from time_row import extract_time_nanoseconds


@dataclass
class LogStatistics:
    cookies_eaten: int
    cookies_missed: int
    time_lines_count: int
    time_lines_frequency_hz: float

    @property
    def pending_cookies(self) -> int:
        return self.time_lines_count - self.cookies_eaten - self.cookies_missed

    def to_line(self):
        return (
            "------"
            "\n"
            f"[statistics] - "
            f"cookies eaten: {self.cookies_eaten}, "
            f"cookies missed: {self.cookies_missed}, "
            f"cookies pending: {self.pending_cookies}, "
            f"time rows rate: {self.time_lines_frequency_hz}"
            "\n"
            "------"
            "\n"
        )


def extract_frequency_hz(time_lines: List[str]) -> float:
    times_nanoseconds = [extract_time_nanoseconds(time_line)
                         for time_line in time_lines]
    times_seconds = [nanoseconds / 1e9 for nanoseconds in times_nanoseconds]
    return len(times_seconds) / (times_seconds[-1] - times_seconds[0])


def generate_statistics_from_time_lines(
    time_lines: List[str],
) -> LogStatistics:
    cookies_eaten_list = list(
        filter(lambda line: COOKIE_TIME_LABEL in line, time_lines)
    )
    cookies_missed_list = list(
        filter(lambda line: SLEEPING_LABEL in line, time_lines))
    if len(cookies_eaten_list) == 0:
        return LogStatistics(0, 0, 0, 0)
    return LogStatistics(
        cookies_eaten=len(cookies_eaten_list),
        cookies_missed=len(cookies_missed_list),
        time_lines_count=len(time_lines),
        time_lines_frequency_hz=extract_frequency_hz(time_lines),
    )
