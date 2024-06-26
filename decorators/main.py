import time

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

@execution_time_decorator
def some_function(x):
    time.sleep(x)  # Simulate a time-consuming task
    return f"Function completed after sleeping for {x} seconds"

# Call the decorated function
result = some_function(2)
print(result)
