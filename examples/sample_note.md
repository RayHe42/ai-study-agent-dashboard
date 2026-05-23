# Python Decorators

A decorator is a function that takes another function and extends its behavior without explicitly modifying it.

## Key Points

- Uses the @syntax above the function definition
- Common examples: @staticmethod, @classmethod, @property
- Can be stacked

## Example

```python
def my_decorator(func):
    def wrapper():
        print("Before the function runs.")
        func()
        print("After the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

## Summary

Decorators wrap functions to add behavior before/after the original function runs.
