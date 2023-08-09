# функция filter

data = [1,5,4,78,5,232,15,45,8,6]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)