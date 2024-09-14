class Animal:
    def say_hi(self):
        raise NotImplementedError("Subclasses must implement this method")


class MouthlessDog:
    def say_hi(self):
        return NotImplemented


# Explanation:
# Use `NotImplementedError` (exception), when method or function is required
# But not yet written out (implemented), useful in base classes
# `NotImplemented` it is a special return value, which implies that
# The behaviour of this function/method is not defined or/and cannot be implemented
