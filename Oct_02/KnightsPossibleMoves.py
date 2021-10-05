print("Enter coordinates of knight, entered numbers must be integers from the interval [1,8]")
px = int(input("x = "))
py = int(input("y = "))

if px-2 > 0:
    if py-1 > 0:
        print("({0},{1})".format(px-2, py-1))
    if py+1 < 9:
        print("({0},{1})".format(px-2, py+1))

if px-1 > 0:
    if py-2 > 0:
        print("({0},{1})".format(px-1, py-2))
    if py+2 < 9:
        print("({0},{1})".format(px-1, py+2))

if px+1 < 9:
    if py-2 > 0:
        print("({0},{1})".format(px+1, py-2))
    if py+2 < 9:
        print("({0},{1})".format(px+1, py+2))

if px+2 < 9:
    if py-1 > 0:
        print("({0},{1})".format(px+2, py-1))
    if py+1 < 9:
        print("({0},{1})".format(px+2, py+1))
