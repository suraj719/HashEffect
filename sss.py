from random import randint

# Prime number used to define the prime field
px = int(input("Enter prime number to define prime field:"),16)
p = int(px)
# p=int(ph)

# Function to generate a random polynomial of degree `threshold - 1` with the given constant term (the secret)
def generate_random_polynomial(secret, threshold):
    coefficients = [secret] + [randint(1, p - 1) for _ in range(threshold - 1)]
    return coefficients

# Function to evaluate the polynomial at a given x (used to create shares)
def evaluate_polynomial(coefficients, x):
    result = 0
    power_of_x = 1
    for coeff in coefficients:
        result += coeff * power_of_x
        power_of_x = (power_of_x * x) % p
    return result % p

# Function to generate shares from a secret
def generate_shares(secret, num_shares, threshold):
    coefficients = generate_random_polynomial(secret, threshold)
    shares = [list((x, (evaluate_polynomial(coefficients, x)))) for x in range(1, num_shares + 1)]
    for id,share in enumerate(shares):
        print("before: ",share[1])
        shares[id][1] = int(str(share[1]),16)
        # print(share)
    return shares

# Reconstruct the secret using Lagrange interpolation
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

# Example usage:
# The secret to be shared
secret = int(input("Enter secret:"))

# The number of shares to create and the threshold (minimum shares required for reconstruction)
num_shares = int(input("Enter no.of shares:"))
threshold = int(input("Enter threshold:"))

# Generate shares
shares = generate_shares(secret, num_shares, threshold)

# Print the shares
for share in shares:
    print(f"Share {share[0]}: {share[1]}")

# Reconstruct the secret from shares
reconstructed_secret = lagrange_interpolation(shares[:threshold], p)
print("Reconstructed Secret:", reconstructed_secret)