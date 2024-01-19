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
* without time.sleep add to a file named “time.1.log” a new line with the current time in nanoseconds approximately 13 times a second. Format it as follows: `f”[time] - {get_time()}”``
* ⁠without using time.sleep, approximately every 2.7 seconds go over the new lines in the current file, and append to them a tupple of all the prime numbers between 2-30 that are dividers of the time in the row.
* ⁠if the enter key is pressed, append to the end of the file statistics about the file: how many correct odd/even specifiers are out of the total time rows, how many rows still did not get a specifier, what was the pace in which the lines where written (the last minus the first time in the log divided by the number of [time] rows in the log). Then open a new file named “time.X.log” and continue the loop with it.
* ⁠if escape is pressed, shut down the eventloop gracefully (without terminating a task in the middle of its writing). Use exceptions for this.
* ⁠without using time.sleep write to the log approximately every second statistics about the last second (same metrics as above) with the format: f”[stats] in the last {time_passed_from_last_stats_according_to_file} - {correct_odds}/{total_time_rows} were correct, {unhandled} time rows do not have a specifier yet, and the rate of time rows is {rate}”

## The exercise

build a program that runs all of the above tasks in parallel.

### Step 1

1. Write the program logic using **threads**, without using synchronizing mechanisms. How well is the output looking? Is it crashing?
1. Add syncronising mechanisms (Mutex, Semaphore, Event)

### Step 2

1. Write a custom event loop that is capable of running multiple coroutines in parallel.
1. Write the program logic in coroutines. How well is the output looking? Is it crashing?

### Restrictions
- you can open each file for writing and reading only one time along the whole run, and should use the same handle in all your parallel tasks. Use seek for going around.
- ⁠every row that is added to a file, should be appended to the end of it, so each row will not change its index along the run.
- ⁠the only keyboard function you can use is “is_pressed(key)”
- ⁠a long press on a key should be interpreted only once.
- ⁠do not use time.sleep at all, the only function you can use is random_sleep() if you want too.