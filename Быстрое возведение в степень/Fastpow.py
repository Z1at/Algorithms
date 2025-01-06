def fastpow(a: int, n: int, mod: int):
    if n == 0:
        return 1
    if n % 2 == 1:
        return (a * fastpow(a, n - 1, mod)) % mod
    temp = fastpow(a, n // 2, mod)
    return (temp * temp) % mod
