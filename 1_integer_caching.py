a = int("256")
b = int("256")
print(a is b)   # True

c = int("257")
d = int("257")
print(c is d)   # False

# Explanation:
# Python caches small integer numbers till 256
# However, if integers are specified implicitly, like:
# c = 257
# d = 257
# a is d    -> True
# Integers will be cached anyways
