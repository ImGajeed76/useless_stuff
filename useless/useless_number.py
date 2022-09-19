def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def base_to_number(digits, b):
    n = 0
    for d in digits:
        n = n * b + d
    return n
