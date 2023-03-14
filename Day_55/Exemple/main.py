# Create the logging_decorator() function 👇
def logging_decorator(function):
    def log(*args):
        print(f"You called {function.__name__}({args[0]}, {args[1]}, {args[2]})")
        function(args[0], args[1], args[2])
    return log


# Use the decorator 👇
@logging_decorator
def a_function(a:int,b:int,c:int):
    print(f"It returned: {a+b+c}")

a_function(1,2,3)