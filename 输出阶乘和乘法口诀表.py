# 输出x的阶乘。0的阶乘为1
def factorial(x) -> object:
    m = 1
    if x == 0:
        return 1
    for i in range(1, x + 1):
        m *= i
    return m


print(factorial(0))
print(factorial(10))


# 输出乘法口诀表
def chenfakj(i) -> object:
    """

    :rtype: object
    """
    for m in range(1, i + 1):
        for j in range(1, m + 1):
            print("%d * %d = %d" % (j, m, j * m), end=' ')
        print('')


chenfakj(8)



