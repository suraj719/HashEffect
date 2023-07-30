def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mod_in_field(number, modulus):
    mapped_number = number % modulus
    if mapped_number < 0:
        mapped_number += modulus
    return mapped_number

def verify_shares(shares, prime, num_shares, g):
    if not is_prime(prime):
        return False

    for x, y in shares:
        if not (0 < x <= num_shares) or not (0 <= y < prime):
            return False

    # Verify commitments
    for i in range(len(shares)):
        x, y = shares[i]
        commitment = pow(g, x, prime)
        if commitment != y:
            return False

    return True

def generate_g(prime):
    for g in range(2, prime):
        if all(pow(g, powers, prime) != 1 for powers in range(1, prime)):
            return g
    return None

def main():
    try:
        # Input prime number (in hexadecimal format)
        prime = int(input("Enter prime number: "), 16)

        # The number of shares (n)
        num_shares = int(input("Enter the number of shares: "))

        # Generate g for the group
        g = generate_g(prime)
        if g is None:
            print("No generator found for the given prime. Please choose a different prime.")
            return

        # Input share values (in the format 'x1 y1; x2 y2; ... xn yn')
        shares_input = input(f"Enter {num_shares} shares (in the format 'x1 y1; x2 y2; ... xn yn'): ")
        shares = [(int(x), int(y, 16)) for x, y in [share.split() for share in shares_input.split(';')]]

        # Verify shares using g
        if verify_shares(shares, prime, num_shares, g):
            print("All shares are valid and lie within the prime field.")
        else:
            print("Invalid shares detected.")

    except ValueError:
        print("Invalid input. Please make sure the prime number, number of shares, and shares are correctly formatted.")
main()
# if _name_ == "_main_":
#     main()