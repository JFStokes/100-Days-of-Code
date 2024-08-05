# Python Decorators

def decorator_function(function):
    print("--> This is the Decorator Function.")
    def wrapper_function():
        print("--> This is the Wrapper Function")
        function()
        function()
    return wrapper_function

@decorator_function
def say_hello():
    print("--> Hello")

@decorator_function
def say_bye():
    print("--> Bye")

say_hello()

say_bye()
