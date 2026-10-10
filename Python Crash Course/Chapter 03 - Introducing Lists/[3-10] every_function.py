countries = ['brazil', 'america', 'korea', 'japan', 'france', 'spain', 'england']
print(countries)
print(countries[0])

countries[0] = 'canada'
print(countries)

countries.append('malaysia')
print(countries)

countries.insert(0, 'china')
print(countries)

del countries[0]
print(countries)

popped_country = countries.pop()
print(popped_country)
print(countries)

countries.remove('japan')
print(countries)

countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)

print(sorted(countries))
print(countries)

countries.reverse()
print(countries)

print(len(countries))

#This exercise wants you to use every function shown in this chapter, but there are a lot. I may have missed some.