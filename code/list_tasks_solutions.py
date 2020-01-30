from operator import itemgetter

#task 1
x = [10, 20, 30]
y = [40, 50, 60]
x[:0] =y
print(x)

#task 2
l = [(10,20,30), (40,60,20), (20,20,200), (10,70,30), (50,10,100)]

lr1 = sorted(l, key=lambda x: x[1], reverse=True)
print(lr1)

lr2 = sorted(l, key=itemgetter(1), reverse=True)
print(lr2)

#