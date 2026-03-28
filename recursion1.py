def power(n):
    if n == 0:
        return
    power(n - 1)
    print(n)

n = int(input())
power(n)