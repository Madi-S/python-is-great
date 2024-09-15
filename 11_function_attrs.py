def do_something():
    pass


def do_something_else():
    do_something.some_attr = 42
    do_something.some_attr += 1
    print(do_something.some_attr)


do_something_else()   # 43

# Explanation:
# Like said before, everything in Python is a subclass/object
# So functions are objects as well, so we can as well attributes
# To functions too, but it does not really make sense, tho it's possible
