#task1
shopList = ["toblerone", "cheese", "tomatoes", "apples"]
print (shopList)
shopList.append('milk')
print (shopList)

#task2
grades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
result = sum (grades) / len (grades)
print (result)

#task3
names = ["Kel", "Nick", "Cris", "Eve"]
names.sort()
print (names)

#task4
cities = ["Berlin", "Paris", "Bern", "London", "Tokio"]
cities[2] ="Praga"
print(cities[0], cities[-1])

#task5
favouriteBooks = ["Fazbear Frights Into the pit", "Gaming consoles 2.0", "Fallout Cook book"]
print ("lists lenght ",len(favouriteBooks))
del favouriteBooks[0]
favouriteBooks.sort()
print (favouriteBooks)