import pytest

import time_row


@pytest.mark.parametrize(
    "time_ns,expected_line",
    [
        (123456789, "[time] - 123456789                    \n"),
        (123456789123456789,
         "[time] - 123456789123456789                    \n"),
        (-123456789, "[time] - -123456789                    \n"),
        (0, "[time] - 0                    \n"),
    ],
)
def test_time_row(time_ns: int, expected_line: str):
    assert time_row.create_line(time_ns) == expected_line
    assert time_row.extract_time_nanoseconds(expected_line) == time_ns
