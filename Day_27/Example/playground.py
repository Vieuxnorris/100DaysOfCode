def add(*args):
    return sum(number for number in args)

def calculate(n, **kwargs):
    label = [key for (key, arg) in kwargs.items()]
    if "add" in label:
        n += kwargs["add"]
    elif "multiply" in label:
        n *= kwargs["multiply"]
    return n

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")

final = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
final2 = calculate(2, multiply=5)
print(final2)
print(my_car.model)
