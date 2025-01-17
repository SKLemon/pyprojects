# The below is an example of multiple positional arguments inside a function
def add(*args):
    list = [number for number in args]
    total = sum(list)
    return total


"""
? Best solution is:

# def add(*args):
    # return sum(args)

? This is because *args stores the input as a tuple... and a tuple is iterable with sum()
"""

add(2, 3, 5)


# The below is an example of multiple keyword arguments inside a function
def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    # for key, value in kwargs.items():
    #     print(key)
    #     value += 1


calculator(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs) -> None:
        # Square bracket method. Will result in an error if not called when class is created
        self.make_car = kwargs["make"]
        self.model_car = kwargs["model"]
        # .get() method. Will return None if not called when class is created
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(
    make="Nissan", model="GT-R"
)  # Note how the keyword arguments are not visible by hovering over the class created
print(my_car.model_car)
