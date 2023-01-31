d = int(input())
x, y = map(int, input().split())

if not (x + y > d or x < 0 or y < 0):
    print(0)

else:
    half_d = round(d / 2, 2)
    if half_d >= x and half_d >= y:
        print(1)
    if y + x >= half_d and x > half_d:
        print(2)
    if x + y < half_d < y:
        print(3)
