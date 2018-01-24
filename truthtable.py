a = True
b = False

# !A || (A && B)
answer = not(a) or (a and b)
print("A: ", + a)
print("B: ", + a)
print("!A || (A && B) = ", + answer)