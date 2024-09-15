if 1:
    print("1 is True")

print(1 == True)                    # True
print(0 == False)                   # True
print(1 + True)                     # 2
print(True + True)                  # 2
print(50 * (True + True))           # 100
print((True + 2) ** (False + 4))    # 81

# Explanation:
# In Python, `True` and `False` are actually subclasses of integers
# And they have the values of 1 or 0 respectively
# And that's why you can perform math operations with `True` and `False`
# It is not that unique of a behaviour, same things happen in C for example
# In Python, everything is an object and a subclass of something
