
#tuples
t = ()

t1 = (1,2,3)
t2 = ('a', 'b')
t3 = (10, 'name', 2.0)

print(t3[2])

print('id of t2' + str(id(t2)))

t2 += ('c', 'd')

print('id of t2' + str(id(t2)))

print('slicing a tuple: ' + str(t2[2:3]))

def returnAllFromModulo(i, j):

	res = i//j
	rem = i%j

	return (res, rem)

print(returnAllFromModulo(10,7))	

a = 100
b = 200

(b,a) = (a,b)

print(a)
print(b)


#lists

l = []
l = [1, 2, 3, 'this', ('a', 'b'), [1, 2]]

s = l[4]
print(id(s))
print(id(l[4]))

l1 = [1, 2, 3, 4]
print(id(l1))

l1[0] = 10
print(id(l1))

l1.append(5)
print(id(l1))


#operations on lists

l2 = [5, 6, 7, 8]

l3 = l1 + l2 #concatenation via +

l1.extend([5, 6, 7, 8])

print(l3)
print(l1)


print(l1)
del(l1[2]) #remove with index
print(l1)

l1.pop() #remove and return last element
print(l1)

r = l1.pop(2) #remove and return indexed element 
print(l1)
print(r)

print(list('splitIt!'))
print('this, is a string'.split(','))

l4 = ['more', 'words', 'here']
print('_'.join(l4))

l5 = [3, 6, 1, 9, 5, 3]
rL = sorted(l5)
print(rL)
l5.sort()
print(l5)
l5.reverse()
print(l5)


words = ['some', 'words', 'appear']
print (words)
moreWords = words
moreWords.insert(1, 'more')

print (words)


# nested lists

listA = ['data', 'science']
listB = ['machine']

newList = [listA]

print (newList)

newList.append(listB)

print (newList)

listB.append('learning')
print (listB)
print (newList)


