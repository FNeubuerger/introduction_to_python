from operator import itemgetter

#task 1
print('Task 1')
x = [10, 20, 30]
y = [40, 50, 60]
x[:0] =y
print(x)
print('end Task 1')


#task 2
l = [(10,20,30), (40,60,20), (20,20,200), (10,70,30), (50,10,100)]

lr1 = sorted(l, key=lambda x: x[1], reverse=True)
print(lr1)

lr2 = sorted(l, key=itemgetter(1), reverse=True)
print(lr2)

#task 3
x1 = [x**2 for x in range(1,11)]
print(x1)

#task 4

m = [[1,2], [3,4], [5,6], [7,8]]
res= [(row[1]*row[1],row[0]) for row in m]
print(res)

#task 5
m = [[1,2,3,4], [3,4,5,6], [5,6,7,8], [7,8,9,10]]
res= [row[3:]+row[:3] for row in m]
print(res)

