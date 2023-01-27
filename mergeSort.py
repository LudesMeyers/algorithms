def mrgsrt(inlst):

	lstOut = []

	flst = len(inlst) // 2
	elst = len(inlst) - flst

	print("Front ")
	print(inlst[:flst])
	print("End ")
	print(inlst[elst:])

	if len(inlst) == 1:
		print("list length is one " + inlst)


	for i in range(len(inlst)):
		print(inlst[i])

def main():

	
	nelements = input("Enter a number ")
	nelements = int(nelements)
	elements = []
	for i in range(nelements):
		elements.insert(i, i)
	mrgsrt(elements)

main()