# .........................Basic Decorator.........................#

def decorator(function):

    def wrapper():
        print("Before Function")
        function()
        print("After Function")

    return wrapper


@decorator
def hello():
    print("Hello Python")


hello()


# .........................Decorator with Function.........................#

def decorator(function):

    def wrapper():
        print("Function Started")
        function()
        print("Function Completed")

    return wrapper


@decorator
def message():
    print("Welcome to Python")


message()


# .........................Decorator with Parameters.........................#

def decorator(function):

    def wrapper(a, b):
        print("Addition Started")
        function(a, b)
        print("Addition Completed")

    return wrapper


@decorator
def add(a, b):
    print(a + b)


add(10, 20)


# .........................Decorator with Return Value.........................#

def decorator(function):

    def wrapper(a, b):
        result = function(a, b)
        return result


    return wrapper


@decorator
def add(a, b):
    return a + b


result = add(10, 20)

print(result)


# .........................Decorator with String.........................#

def decorator(function):

    def wrapper(name):
        return function(name).upper()

    return wrapper


@decorator
def greeting(name):
    return f"Hello {name}"


print(greeting("Rahul"))


# .........................Decorator with if else.........................#

def check_age(function):

    def wrapper(age):

        if age >= 18:
            function(age)
        else:
            print("You are not eligible")

    return wrapper


@check_age
def vote(age):
    print("You can vote")


vote(20)
vote(16)


# .........................Multiple Decorators.........................#

def first(function):

    def wrapper():
        print("First Decorator")
        function()

    return wrapper


def second(function):

    def wrapper():
        print("Second Decorator")
        function()

    return wrapper


@first
@second
def hello():
    print("Hello Python")


hello()


# .........................Decorator with *args.........................#

def decorator(function):

    def wrapper(*args):
        print("Arguments:", args)
        return function(*args)

    return wrapper


@decorator
def add(a, b, c):
    return a + b + c


print(add(10, 20, 30))


# .........................Decorator with **kwargs.........................#

def decorator(function):

    def wrapper(**kwargs):
        print("Data:", kwargs)
        return function(**kwargs)

    return wrapper


@decorator
def student(name, age):
    print(name, age)


student(name="Aman", age=20)


# .........................Practical Example.........................#

def login_required(function):

    def wrapper(username):

        if username == "admin":
            function(username)
        else:
            print("Access Denied")

    return wrapper


@login_required
def dashboard(username):
    print("Welcome to Dashboard")


dashboard("admin")
dashboard("user")
