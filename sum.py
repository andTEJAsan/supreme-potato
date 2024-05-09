# Ok so the input is going to ax^2 + bx + c = 0, but we are going to get a list 
# consisting of the coefficients [a, b, c] and we need to return the sum of the nth
# powers of the roots of the equation


# So Lets call T_n = alpha^n + beta^n where alpha and beta are the roots of the equation
# T_0 = 2
# T_1 = -b/a 
# We are going to use the rational library of python to get exact answers

# If we multiply the equation by x^n-2 what do we get ? 
# a*x^n + b*x^(n-1) + c*x^(n-2) = 0
# Both alpha and beta satisfy this equation so what do we get now by substituting both alpha and beta into it ? 
# a*alpha^n + b*alpha^(n-1) + c*alpha^(n-2) = 0
# a*beta^n + b*beta^(n-1) + c*beta^(n-2) = 0
# Now if we add the two equations we get

# T[n] = alpha^n + beta^n
# a*(alpha^n + beta^n) + b*(alpha^(n-1) + beta^(n-1)) + c*(alpha^(n-2) + beta^(n-2)) = 0
# a*T_n + b*T_(n-1) + c*T_(n-2) = 0
# a*T[n] +b*T[n-1] + c*T[n-2] = 0
# If we want to calculate T[n], T[n-1] and T[n-2] should have been calculated already, and if they are
# Then T[n] = -b/a*T[n-1] - c/a*T[n-2], now we can calculate T[n+1] and so on , as T[n] and T[n-1] have been calcualted


from fractions import Fraction
# im assuming that coeff is a list of length 3 a,b,c, n

def sum_roots(coef, n):
	# coef = [1,2,3]
	a = coef[0]
	b = coef[1]
	c = coef[2]
	a = Fraction(a)
	b = Fraction(b)
	c = Fraction(c)
	# T[n] = alpha^n + beta^n
	# list T would be of size n+1 , because then the last index would be equal to n T[n]
	T = [Fraction(0)]*(n+1)
	# T = []
	# for i in range(n+1):
	# 	T.append(Fraction(0))
	T[0] = Fraction(2)
	T[1] = Fraction(-b/a)
	i = 2
	while i <= n:
		T[i] = Fraction(-b/a)*T[i-1] - Fraction(c/a)*T[i-2]
		i += 1

	return T


# Take input from the user

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
n = int(input("Enter the value of n: "))
coef = [a,b,c]
T = sum_roots(coef, n)

print(f"The sum of the nth powers of the roots of the equation is {T[n]}")
for i,x in enumerate(T):
	print(f"alpha^{i} + beta^{i} = {x}")



