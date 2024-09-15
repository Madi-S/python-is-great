def some_func():
    return 1
    bs[10].where[:-1]("after return") + {}.hi[{}].jo({})


some_func()
# no errors

# Explanation:
# When Python parses this code, it checks for syntax errors
# However, if not valid pythonic code is placed after return
# Meaning before evaluation, it thinks it's fine
# This is good, because at some point in the program
# This code might be valid
# Since Python never reaches after return statement
# There will be no value or attribute errors
# All in all, it is possible due to dynamic interpreter 
# Under the hood of Python
