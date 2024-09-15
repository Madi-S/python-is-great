def get_one():
    return 1

print(f())      # 1
a = [1, 2, 3]
b = a           # b is now a reference to a
print(id(a))    # 2740551561664
print(id(b))    # 2740551561664
a += [4]
print(a)        # [1, 2, 3, 4]
print(b)        # [1, 2, 3, 4]      nothing fancy, as we expected

s = "hello"
t = s           # t is now a reference to s
print(id(s))    # 2740555941872
print(id(t))    # 2740555941872
s += " world"
print(id(s))    # 2740555943344
print(id(t))    # 2740555941872
print(t)        # 'hello'
print(s)        # 'hello world'     obscure, right?

# Explanation:
# The references in last example have changed, this is because
# When you modify immutable objects (e.g., string)
# It results in new objects creation
# And leaving original reference unaffected
# When modifying mutable objects (e.g., lists)
# It affects all references to the lists
