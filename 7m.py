# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#print (len(it_companies) )

it_companies.add('Twitter')
#print (len(it_companies) )

it_comes={'google', 'microsoft', 'apple'}
it_companies.update(it_comes)
#print (len(it_companies) )

C=A.union(B)
#print(C)

D=A.intersection(B)
#print(D)

#print(A.issubset(B))

#print(A.isdisjoint(B))

E=A.symmetric_difference(B)
#print(E)
