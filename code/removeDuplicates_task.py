
listA = [10, 20, 50, 70]
listB = [10, 20, 60, 80]

def removeDuplicates1(l1, l2):
	for elem in l1:
		if elem in l2:
			l1.remove(elem)
	return(l1)			


def removeDuplicates2(l1, l2):
	l3 = l1[:]
	for elem in l3:
		if elem in l2:
			l1.remove(elem)

	return(l1)			

print(removeDuplicates1(listA, listB))
print(removeDuplicates2(listA, listB))	