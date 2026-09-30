#1.2.4

# i = 5
# while i >= 5 and i < 20:
#     print(i * 2)
#     i += 1

#1.2.6
def factor(n):
    if n == 0 or n == 1:
        res = 1
    else:
        res = n * factor(n - 1)
    return res

def combination(n, m):
    c = factor(n) / ( factor(n - m) * factor(m) )
    return c

# print(combination(4,2))

#1.2.7
def binomial_expand_minus(n):
    for k in range(0, n+1):
        coeff = combination(n, k)
        if k % 2 == 0:
            sign = 1
        final_coeff = coeff * sign
        print(f"{final_coeff}x^{k}")

binomial_expand_minus(4)