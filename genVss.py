from random import randint
px = int(input("Enter prime number to define prime field:"),16)
p = int(px)
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
        # print("before: ",share[1])
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
def createCommitments(shares,g):
    commitments = []
    for i in range(0,11):
        x,y = shares[i]
        print(commitments)
        commitments.append(pow(g,y)%p)
    return commitments

# secret = int(input("Enter secret:"))
secret = 457
# The number of shares to create and the threshold (minimum shares required for reconstruction)
# num_shares = int(input("Enter no.of shares:"))
num_shares = 10
# threshold = int(input("Enter threshold:"))
threshold = 7
generator = 3
shares = generate_shares(secret, num_shares, threshold)
print(shares)
commitments = createCommitments(shares,generator)
print(commitments)