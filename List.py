
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', "Karen", 'Jim', "Oscar", "Oscar", "Toby"]
friends2 = friends.copy()

print(friends)
#print(friends[1:4])
#friends.insert(1, "Kelly")
#friends.extend(lucky_numbers)
#friends.append("Creed")
#friends.pop()

friends.sort()
lucky_numbers.reverse()
print(friends)
print(lucky_numbers)
print(friends.index('Jim'))
print(friends.count('Oscar'))





