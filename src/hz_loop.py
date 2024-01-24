from parallelism_exercise_utils import get_time_ns, random_sleep

from typing import Callable


def hz_loop(
    callable: Callable[[], None], should_stop: Callable[[], bool], *, hz: float
):
    assert hz > 0, "hz should be greater then zero"
    period_time_ns = 1e9 / hz
    next_loop_time = get_time_ns()
    while not should_stop():
        if get_time_ns() >= next_loop_time:
            print("Acting!")
            next_loop_time += period_time_ns
            callable()
        print(".", end="")
        random_sleep()
