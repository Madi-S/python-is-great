class SomeClass:
    some_attr = "69"    # <- class attribute


s1 = SomeClass()
s2 = SomeClass()
print(s1.some_attr)                     # "69"
print(s2.some_attr)                     # "69"
print(s1.some_attr is s2.some_attr)     # True

SomeClass.some_attr = "xyz"
print(s1.some_attr)                     # "xyz"
print(s2.some_attr)                     # "xyz"

s1.some_attr = "new for s1"
print(s1.some_attr)                     # "new for s1"
print(s2.some_attr)                     # "xyz"
print(SomeClass.some_attr)              # "xyz"
print(s1.some_attr is s2.some_attr)     # False

# Explanation:
# What went wrong here?
# Well, class attributes should not be accessible from class instances
# Initially, class and instances reference the same object for a class attribute
# But, once this attribute is being changed from instance, a chaos arises
