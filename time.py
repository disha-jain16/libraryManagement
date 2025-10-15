import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")
        return result
    return wrapper

@time_it
def slow_function():
    time.sleep(2)
    return "Done"

# Test
print(slow_function())  # Output: Done + time taken
