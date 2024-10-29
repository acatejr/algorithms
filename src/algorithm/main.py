def rec_int_mult(x: int, y: int) -> int:
    
    prod = 0
    n = len(str(x))

    if (n % 2) == 0:
        mid = int(n / 2)
        xstr = str(x)
        ystr = str(y)
        a = int(xstr[:1])
        b = int(xstr[1:])
        c = int(ystr[:1])
        d = int(ystr[1:])
        ac = rec_int_mult(a, c)
        ad = rec_int_mult(a, d)
        bc = rec_int_mult(b, c)
        bd = rec_int_mult(b, d)
        prod = (10**n * ac) + 10**(n/2) * (ad + bc) + bd
        
    elif n == 1:
        prod = x * y
    else:
        prod = None

    return(prod)