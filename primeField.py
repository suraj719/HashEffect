def mod_inverse(a, m):
    """
    Calculate the modular inverse of 'a' with respect to modulus 'm'.
    """
    if m == 1:
        return 0

    m0 = m
    x0, x1 = 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += m0

    return x1

def field_prime_value(a, b, p):
    """
    Calculate the field prime value of the fractional number (a/b) with respect to modulus 'p'.
    """
    if p <= 1 or b == 0:
        raise ValueError("Invalid prime modulus or denominator")

    # Calculate the modular inverse of 'b' with respect to 'p'
    b_inverse = mod_inverse(b, p)

    # Calculate the field prime value of (a/b)
    result = (a * b_inverse) % p

    return result

# Example usage:
a = 1
b = 3
p = 11

field_prime_val = field_prime_value(a,b,p)
print(f"Field prime value of {a}/{b} with respect to {p} is: {field_prime_val}")