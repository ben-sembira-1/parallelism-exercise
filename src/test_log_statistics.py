import pytest

import log_statistics


def test_time_lines_hz():
    time_rows = [
        "[time] - 1708179025196872904          (Sleeping)",
        "[time] - 1708179025302902059       (Cookie time)",
        "[time] - 1708179025389353660       (Cookie time)",
        "[time] - 1708179025435546667          (Sleeping)",
    ]

    assert 16.759 < log_statistics.extract_frequency_hz(time_rows) < 16.760
