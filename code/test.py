from operator import itemgetter
from operator import attrgetter, methodcaller

a = [[20,30], [30,40],[10,10]]

f = itemgetter(1)
for e in a:
	print(f(e))

print(sorted(a, key=f))

print(sorted(a, key = lambda x: x[1]))

class Place:
    def __init__(self, name, population, state, area):
	    self.name = name
	    self.population = population
	    self.state = state
	    self.area = area
    def __repr__(self):
        return repr((self.name, self.population, self.state, self.area))
    def avg_density(self):
    	return (self.population/self.area)


places = [
	Place('Berlin', 3600000, 'Germany', 892.0),
	Place('Hamburg', 1800000, 'Germany',  716.0),
	Place('Helsinki', 648000, 'Finland', 755.0)
]

places_tuples = [
				('Berlin', 3600000, 'Germany', 892.0),
				('Hamburg', 1800000, 'Germany', 716.0),
				('Helsinki', 648000, 'Finland', 755.0)
]

#print(sorted(places, key= lambda place: place.population))
print(sorted(places_tuples, key= itemgetter(1)))
print(sorted(places, key= attrgetter('population')))

#first by value at index 1, then by 2
print(sorted(places_tuples, key= itemgetter(1,2)))
#same as above, with attributes
print(sorted(places, key= attrgetter('population', 'state')))

print([(Place.name,Place.avg_density()) for Place in places])
print(sorted(places, key= methodcaller('avg_density')))


