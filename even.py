def power(n):
    if n==0:
        return
    power(n-1)
    if n%2 == 0:
     print(n)

n = int(input())
power(n)



