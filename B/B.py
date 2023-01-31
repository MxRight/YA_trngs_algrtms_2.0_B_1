n, a, b = map(int, input().split())
v1 = abs(b - a) - 1
v2 = n - v1 - 2
print(min(v1, v2))
