def string(s):
    if s == "" or len(s) == 1:
        return s
    return string(s[1:]) + s[0]

s = (input())
print(string(s))


