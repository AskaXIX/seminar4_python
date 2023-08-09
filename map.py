# фунция map

# list_1 = [1,2,3,4,5,6,7,8,9,10]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# еще один пример

# data = "1 2 3 4 5 7 8 9 1 5"
# print(data)

# data = data.split()
# print(data)

# упрощенный способ

data = "1 2 3 4 5 7 8 9 1 5"
data = list(map(int, data.split()))
print(data)