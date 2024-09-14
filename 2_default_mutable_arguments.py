def do_something(value, collection = []):
    collection.append(value)
    return collection

result1 = do_something(20)
print(result1)   # [20]

result2 = do_something(69)
print(result2)   # [20, 69]

print(result1 is result2)   # True

# Explanation:
# Obviously, we would expect `result2` to be [69]
# However, the default argument `collection` is created only once in the runtime
# And since it is a mutable object, and we perform mutation over this argument
# We get this strange behaviour 
# When the default argument is intertwined with the previous function call 
