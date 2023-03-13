import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def time_function():
        first_time = time.time()
        function()
        second_time = time.time()
        print(f"{function.__name__} run speed: {second_time - first_time}")

    return time_function


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


if __name__ == "__main__":
    fast_function()
    slow_function()
