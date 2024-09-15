def some_func():
    for x in range(5):
        if x == 3:
            print(x, ": for x inside loop")
    print(x, ": for x outside loop")


def some_other_func():
    even_nums = [x for x in range(11) if not x % 2]
    print(x, ": for x outside loop")

some_func()
# 3 : for x inside loop
# 4 : for x outside loop

some_other_func()
# NameError: name 'x' is not defined
# Whoops?

# Explanation:
# In case of for loops, iterating variable is availabe after loop ends
# In case of list comprehensions, iterating variable is not available ;(
# Because list comprehensions have their own scopes
