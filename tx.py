# import time
# from functools import wraps
#
#
# def timing_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
#         return result
#
#     return wrapper
#
#
# # Example usage:
# @timing_decorator
# def example_function(x):
#     time.sleep(x)
#     return x * x
#
#
# # Call the decorated function
# result = example_function(2)
# print(f"Result: {result}")


# mutble_datatype = list, set, dict
# contex manager


class A:
    def a(self, num):
        print(num)

    def a(self, nums):
        print(nums + 1)


a = A()

print(a.a(3))
