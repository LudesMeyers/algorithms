#!/usr/bin/env python3
import pdb

def karaMultiply(x, y):
	
	xl = len(str(x))
	yl = len(str(y))
		
	n = max(xl, yl)

	if (n % 2 == 1) and (n != 1):
		

	n_by_2 = n//2

	if n==1:
		return(x*y)

	else:
		a = x // 10**n_by_2
		b = x %  10**n_by_2
		c = y // 10**n_by_2
		d = y %  10**n_by_2

		
		ac = karaMultiply(a, c)
		
		bd = karaMultiply(b, d)
		
		abcd = karaMultiply((a + b), (c + d)) - ac - bd
		
	if ((xl % 2 == 1) and (xl > 1)) or ((yl > 1) and (yl % 2 == 1)):
			print(xl % 2, yl % 2)
			print(xl, yl)
			print("x ", x, "y ", y)
			print("ac", a, c, ac)
			print("bd", b, d, bd)
			print("abcd", karaMultiply((a + b), (c + d)))
			input("pause")


	final = (10**n)*ac + (10**(n//2))*abcd + bd
	return(final)

def main():
	
	print("In main")	

	x = input("Enter first integer (x)")

	y = input("Enter second integer (y)")

	print(karaMultiply(x,y))


main()
