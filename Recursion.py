def power(base, exponent):
    if not exponent:
        return 1

    return (base * power(base, exponent - 1))


# print(power(5, 2))


def factorial(num):
    if num is 1:
        return 1
    return num * factorial(num - 1)


# print(factorial(3))


def productOfArray(arr):
    if not arr:
        return 1
    return arr[0] * productOfArray(arr[1:])

#print(productOfArray([5, 5, 4]))


def recursiveRange(num):
    if num is 0:
        return 0

    if num > 0:
        return num + recursiveRange(num - 1)
    else:
        return num + recursiveRange(num + 1)

# print(recursiveRange(6))
