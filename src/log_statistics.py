from dataclasses import dataclass
from typing import Iterable

@dataclass
class LogStatistics:
    cookies_eaten: int
    cookies_missed: int
    time_lines_count: int
    time_lines_frequency_hz: int
    
    @property
    def potential_cookies_updated(self) -> int:
        return self.time_lines_count - self.cookies_eaten - self.cookies_missed



def statistics(time_lines: Iterable[str]) -> LogStatistics:
    return LogStatistics(
        cookies_eaten=len(list(filter(lambda time_line: time_line.endswith("(Cookie time)"), time_lines)))
    )
