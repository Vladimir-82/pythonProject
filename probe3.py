def dig_pow(n, p):
    sum = 0
    for i in str(n):
        sum += int(i) ** p
        p += 1
    res = divmod(sum, n)
    return res[0] if not res[1] else -1

print(dig_pow(89, 1))