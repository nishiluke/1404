
def calculate_pyramid(n):
    if n <= 0:
        return 0
    return n + calculate_pyramid(n - 1)


print(calculate_pyramid(6))