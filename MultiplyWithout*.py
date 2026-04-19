def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)

a = int(input())
b = int(input())

result = multiply(a, b)

print(result)
