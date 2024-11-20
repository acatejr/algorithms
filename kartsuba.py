def karatsuba(x: int, y: int) -> int:
    if len(str(x)) == 1 and len(str(y)) == 1:
        return int(x) * int(y)
    else:
        split = len(str(x)) // 2
        a, b = int(str(x)[0:split]), int(str(x)[split:])
        c, d = int(str(y)[0:split]), int(str(y)[split:])
        p = a + b
        q = c + d
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        pq = karatsuba(p, q)
        adbc = pq - ac - bd

        n = len(str(x))
        return (10 ** n) * ac + 10 ** (n/2) * adbc +bd
        


if __name__ == "__main__":
    res = karatsuba(0, 0)
    assert res == 0

    res = karatsuba(1, 0)
    assert res == 0

    res = karatsuba(1, 1)
    assert res == 1

    res = karatsuba(5, 9)
    assert res == 45

    res = karatsuba(10, 10)
    assert res == 100

    res = karatsuba(30, 10)
    assert res == 300
