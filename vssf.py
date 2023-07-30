
def field_prime_value(num, p):
    return num % p

def validate(index, value, commitments, g, p, p1):
    val_value = pow(g, value, p1)
    product = 1

    for i, j in enumerate(commitments):
        j = int(j,16)
        product = (product * pow(j, index ** i, p1)) % p1

    val_value = field_prime_value(val_value, p1)
    product = field_prime_value(product, p1)

    print(val_value, product)
    return val_value == product

# if __name__ == "__main__":
index = int(input("enter index: "),16)
value = int(input("enter share value: "),16)
commitments = ["a3aeb90e8c923a8e","ce61d471f2407582","cabd8df162e95fc9","12025314455daf5e","afa04b74927de8dc","8b851d262c36b4b8","8231c3e402cda935"]
g = int(input("enter generator: "))
p = int(input("enter p: "),16)
p1 = int(input("enter p1: "),16)
is_valid = validate(index, value, commitments, g, p, p1)
print("Is Valid:", is_valid)