#1.2.4

# i = 5
# while i >= 5 and i < 20:
#     print(i * 2)
#     i += 1

#1.2.6
# def factor(n):
#     if n == 0 or n == 1:
#         res = 1
#     else:
#         res = n * factor(n - 1)
#     return res

# def combination(n, m):
#     c = factor(n) / ( factor(n - m) * factor(m) )
#     return c

# print(combination(4,2))

#1.2.7
# def binomial_expand_minus(n):
#     for k in range(0, n+1):
#         coeff = combination(n, k)
#         if k % 2 == 0:
#             sign = 1
#         final_coeff = coeff * sign
#         print(f"{final_coeff}x^{k}")

# binomial_expand_minus(4)

#1.3.5
# import random
# num = random.randint(2, 2000)
# def square_root_3():
#     c = num
#     g = c / 2
#     i = 0
#     while abs(g*g - c) > 0.00000000001:
#         g = (g + c/g) / 2
#         i = i + 1
#         print("%d: %.13f" % (i,g))

# square_root_3()

#1.3.6
# 有影响，影响精度，除数越大，精度越高，因而达到所要求的精度所需的次数更少，效率更高。