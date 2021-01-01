# 求x,y的最大公约数
def divisor(x, y) -> object:
    if x == y:
        return x
    elif x > y:
        reduce = y
    else:
        reduce = x

    while reduce >= 1:
        if x % reduce == 0 and y % reduce == 0:
            return reduce
        reduce -= 1


print(divisor(64, 16))


# 最小公倍数
def T1(x, y):
    increat = 0
    if x == y:
        return x
    elif x > y:
        increat = x
    else:
        increat = y
    while increat:
        if increat % x == 0 and increat % y == 0:
            return increat
        else:
            increat += 1


print(T1(2, 3))


# 闰年问题
def runYear(y, true='True', false='False'):
    if y % 4 == 0 and y % 100 != 0:
        return true
    elif y % 400 == 0:
        return true
    else:
        return false


print(runYear(2000))
