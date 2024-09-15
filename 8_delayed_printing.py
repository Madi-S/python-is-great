import time


def say_hi():
    print("Hi there", end="_")
    time.sleep(3)


def say_hi_with_flush():
    print("Hi there", end="_", flush=True)
    time.sleep(3)


say_hi()
# waits 3 seconds, then prints "Hi there_"

say_hi_with_flush()
# normal behaviour as expected, "Hi there_", then 3 seconds sleep


# Explanation:
# By changing the end character, it delays the output
# Because the buffer if not flushed until a new line is encountered
# Or program ends (in our case, none of these happens)
