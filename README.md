# parallelism-exercise
An excersize for learning the concepts of parallelism, including threads and event-loops

## Instructions

1. Activate the venv (https://docs.python.org/3/library/venv.html for help)
2. Install the utils package: 
```bash
pip install ./parallelism_exercise_utils
```
3. Run your program:
```bash
python3 src/parallel_party.py
```

## The program
The program includes multiple parallel tasks:
* 13 times a second: Add to a file named “time.1.log” a new line with the current time in nanoseconds. Format it as follows: `f”[time] - {get_time_ns()}”``
* 5 times a second: Go over the new lines in the current file, use the `is_time_for_cookie(number: int) -> bool` function on each one, and append `"(Cookie time)"` or `"(sleeping)"` to the end of the time row according to the value returend from the function. Example: `[time] - 1705707133875248900 (Cookie time)`
* Every 4 seconds: Write to the log statistics (see below) about the new lines from the last statistics log.
* ⁠If the enter key is pressed, append to the end of the file statistics (see below) about the whole session (file) and then open a new session (file) named “time.{prev+1}.log” and continue the loop with it. 
* ⁠If escape is pressed, shut down the eventloop gracefully (without terminating a task in the middle of its writing).

### Statistics

Statistics include:
* How many cookies where eaten?
* Out of how many?
* How many rows still did not get a cookie update?
* What was the rate in which the time rows where written (the last minus the first time in the given rows devided by the amount of time rows).

The format should be:
```python
f"[statistics] - {generate_statistics()}"
```

## The exercise

build a program that runs all of the above tasks in parallel.

### Step 1

Read about:

1. Threads
1. Context switch
1. ⁠Threads synchronizing mechanisms (mutex, semaphore, event)

Code:

1. Write the program logic using **threads**, without using synchronizing mechanisms. How well is the output looking? Is it crashing?
1. Add syncronising mechanisms (Mutex, Semaphore, Event)

### Step 2

Read about:

1. ⁠Event loops (tasks, queue, await)
1. ⁠AsyncIO

Code:

1. Write the program logic using **asyncIO**, without using synchronizing mechanisms. How well is the output looking? Is it crashing?

### Step 3

Read about:

1. ⁠Generators in python (yield, yield from, next)
1. ⁠Coroutines

Code:

1. Write a custom event loop that is capable of running multiple coroutines in parallel.
1. Write the program logic in coroutines. How well is the output looking? Is it crashing?

### Restrictions
- You can open each file for writing and reading only one time along the whole run.
- Every row that is added to a file, should be appended to the end of it, so each row will not change its index along the run.
- ⁠A long press on a key should be interpreted only once.
- You are limited to import only from the exercise utils, and typing.
    - Do not change the utils package, and import only from `parallel_exercise_utils`.
    - From the utils import only: `is_pressed, get_time_ns, random_sleep, open_once, is_time_for_cookie`