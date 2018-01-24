import math 

a = 1
b = -3
c = 2

'''
x = -b +/- sqrt(b^2 - 4ac)
	----------------------
			2a

'''
discriminant = b*b - 4 * a * c
sqrt = math.sqrt(discriminant)

root1 = (-b + sqrt)/(2 * a * c)
root2 = (-b - sqrt)/(2 * a * c)

print(root1) 
print(root2)