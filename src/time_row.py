__PREFIX = "[time] - "
__SUFFIX = f"{' ' * 20}\n"

def is_time_line(line: str) -> bool:
    return line.startswith(__PREFIX)

def create_line(time_ns: int) -> str:
    return __PREFIX + str(time_ns) + __SUFFIX


def extract_time(line: str) -> int:
    assert is_time_line(line), "Line is not a time line"
    return int(line.removeprefix(__PREFIX).removesuffix(__SUFFIX))
