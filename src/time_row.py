__TIME_PREFIX = "[time] - "
__LABELS_PLACEHOLDER_SUFFIX = f"{' ' * 20}\n"


def is_time_line(line: str) -> bool:
    return line.startswith(__TIME_PREFIX)


def create_line(time_ns: int) -> str:
    return __TIME_PREFIX + str(time_ns) + __LABELS_PLACEHOLDER_SUFFIX


def extract_time(line: str) -> int:
    assert is_time_line(line), "Line is not a time line"
    return int(line.removeprefix(__TIME_PREFIX).removesuffix(__LABELS_PLACEHOLDER_SUFFIX))
