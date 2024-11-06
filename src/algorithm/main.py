def rec_int_mult(x: int, y: int) -> int:
    """Compute product of two terms recursively

    Usage examples:
    >>> rec_int_mult(0, 2)
    0
    >>> rec_int_mult(2, 0)
    0
    >>> rec_int_mult(1, 2)
    2
    >>> rec_int_mult(2, 1)
    2
    >>> rec_int_mult(10, 1)
    10
    >>> rec_int_mult(1, 10)
    10
    >>> rec_int_mult(10, 10)
    100
    >>> rec_int_mult(100, 100)
    10000
    """
    prod = 0

    if x == 0 or y == 0:
        return x * y
    if x == 1 or y == 1:
        return x * y

    n = max(len(str(x)), len(str(y)))
    if n % 2:
        
        xpad = (n + 1) - len(str(x))
        ypad = (n + 1) - len(str(y))
        x = "0" * xpad + str(x)
        y = "0" * ypad + str(y)
        a = int(x[0:len(x)//2])
        b = int(x[len(x)//2:])
        c = int(y[0:len(y)//2])
        d = int(y[len(y)//2:])
        ac = rec_int_mult(a, c)
        ad = rec_int_mult(a, d)
        bc = rec_int_mult(b, c)
        bd = rec_int_mult(b, d)        

        n = n + 1
        prod = int((10**n * ac) + 10**(int(n/2)) * (ad + bc) + bd)        
        return prod
        # print(n, len(str(x)), len(str(y)), xpad, ypad, x, y, a, b, c, d)

    
# if __name__ == "__main__":
    # x = 0
    # y = 20
    # rec_int_mult(x, y)

    # x = 100
    # y = 20
    # rec_int_mult(x, y)

    # x = 20
    # y = 100
    # rec_int_mult(x, y)

    # x = 100
    # y = 10
    # prod = rec_int_mult(x, y)
    # print(prod)

    # x = 100
    # y = 100
    # prod = rec_int_mult(x, y)
    # print(prod)

    # x = 10000
    # y = 10000
    # prod = rec_int_mult(x, y)
    # print(prod)

# n_x = len(str(x))
#     n_y = len(str(y))

#     if (n_x == 1 and n_y == 1):
#         return x * y

#     # n = max(n_x, n_y)
#     # mid = int(n / 2)    
#     xstr = str(x)
#     ystr = str(y)    
#     xmid = int(n_x/2)
#     ymid = int(n_y/2)
#     if n_x == 2:
#         a = int(xstr[0:1])
#         b = int(xstr[1:])
#     else:
#         a = int(xstr[:xmid+1])
#         b = int(xstr[xmid:])
#     if n_y == 2:
#         c = int(ystr[0:1])
#         d = int(ystr[1:])
#     else:
#         c = int(ystr[:ymid+1])
#         d = int(ystr[ymid:])

#     # print(a, b, c, d)
#     ac = rec_int_mult(a, c)
#     ad = rec_int_mult(a, d)
#     bc = rec_int_mult(b, c)
#     bd = rec_int_mult(b, d)
#     print(ac, ad, bc, bd)
#     prod = int((10**n_x * ac) + 10**(int(n_x/2)) * (ad + bc) + bd)