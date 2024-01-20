
from typing import Iterable, TypeVar
from threading import Thread

TArgs = TypeVar('TArgs')


def threads_pull_same_args(thread_tasks: Iterable[callable[[TArgs], None]], args: TArgs) -> Iterable[Thread]:
    tasks = (Thread(target=task, args=args, daemon=True)
             for task in thread_tasks)
    for task in tasks:
        task.start()
    return tasks
