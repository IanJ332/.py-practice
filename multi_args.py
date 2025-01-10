# args => arguments Any numbers of arguments
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4, 5))

def print_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_all(name="John", age=30)