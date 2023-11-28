########################## ARGS & KWARGS ############################

# Gives unlimited arguments.
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

calc1 = add(1, 2, 3, 4)
print(calc1)

# Gives unlimited key word arguments.
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += value
    print(n)
    

calculate(2, add=3, multiply=5)


# Using **kwargs in a class.
# Using .get() to avoid crash/error.
class Car:

    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw.get('model')

my_car = Car(make='Nissan')

print(my_car.make)
print(my_car.model)
