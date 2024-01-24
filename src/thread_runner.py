from typing import Callable, Iterable, TypeVar
from threading import Thread


def threads_pull(thread_tasks: Iterable[Callable[[], None]]) -> Iterable[Thread]:
    tasks = (Thread(target=task, daemon=True) for task in thread_tasks)
    for task in tasks:
        task.start()
    return tasks
