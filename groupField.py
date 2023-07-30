def mod_exp(base, exponent, prime):
    result = pow(base, exponent, prime)
    return result

g = 3
p = 11
n = 5
group_set = [mod_exp(g, i, p) for i in range(1, n+1)]

print(group_set)                    # Output: [3, 9, 5, 4, 1]
print(mod_exp(g, 3, p))             # Output: 5
print(mod_exp(g, 6, p))             # Output: 3
print(mod_exp(g, -1, p))            # Output: 4
# print(mod_exp(g, 1/3, p))           # Output: 9
