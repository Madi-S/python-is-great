data = (101, 42)
print(data)     # (101, 42)

data = ([101], 42)
print(data)     # ([101], 42)

try:
    data[0] += [5]
except TypeError:
    print("Tuple cannot be changed!")
print(data)     # ([101, 5], 42) weird, right?

# Explanation:
# data[0] += [5] is obviously a syntax sugar, we can rewrite it to:
# data[0] = data[0] + [5]
# `data[0] =` part obviously cannot executed, since tuple is immutable
# However, the right part `data[0] + [5]` list mutation is being executed
# Therefore, we get an error and the result we kind of expected
