from dataclasses import dataclass
from typing import Literal, TypeGuard


__TIME_PREFIX = "[time] - "


def is_time_line(line: str) -> bool:
    return line.startswith(__TIME_PREFIX)


CookieLabelType = Literal["(Cookie time)", "(Sleeping)", ""]


def is_cookie_label(val: str) -> TypeGuard[CookieLabelType]:
    return val in ["(Cookie time)", "(Sleeping)", ""]


@dataclass
class TimeLine:
    time_ns: int
    cookie_label: CookieLabelType = ""

    def to_line(self) -> str:
        LABELS_PLACEHOLDER_SUFFIX_LENGTH = 20

        return (
            __TIME_PREFIX
            + str(self.time_ns)
            + self.cookie_label.rjust(LABELS_PLACEHOLDER_SUFFIX_LENGTH, " ")
        )

    @classmethod
    def from_line(cls, line: str):
        assert line.startswith(__TIME_PREFIX), "Line is not a time line"
        time_line_no_prefix = line.removeprefix(__TIME_PREFIX)
        cookie_label = ""
        time_ns = int(time_line_no_prefix.split()[0])
        if (cookie_label_index := time_line_no_prefix.find("(")) != -1:
            cookie_label = time_line_no_prefix[:cookie_label_index]
        assert is_cookie_label(cookie_label), f"Incorrect label: {cookie_label}"
        return cls(time_ns, cookie_label)
