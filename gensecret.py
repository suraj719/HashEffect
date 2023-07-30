def lagrange_interpolation(shares, prime):
    def interpolate_lagrange(x, shares, prime):
        result = 0
        for i in range(len(shares)):
            xi, yi = shares[i]
            numerator, denominator = 1, 1
            for j in range(len(shares)):
                if i != j:
                    xj, yj = shares[j]
                    numerator = (numerator * (x - xj)) % prime
                    denominator = (denominator * (xi - xj)) % prime
            result = (result + (numerator * pow(denominator, -1, prime) * yi)) % prime
        return result

    return interpolate_lagrange(0, shares, prime)

def crack_secret_from_shares(shares, prime):
    return lagrange_interpolation(shares, prime)

def get_shares_from_user():
    shares = []
    while True:
        try:
            x = int(input("Enter x-coordinate of the share (or any non-integer value to stop): "))
            y = int(input("Enter y-coordinate of the share: "),16)
            shares.append((x, y))
        except ValueError:
            break
    return shares

# Example usage:
p = int(input("Enter the prime number:"),16)  # Prime number defining the prime field

# Get shares from the user
print("Enter the shares. Enter any non-integer value for x to stop.")
shares = get_shares_from_user()

# Cracking the secret
reconstructed_secret = crack_secret_from_shares(shares, p)
print("Reconstructed Secret:", reconstructed_secret)