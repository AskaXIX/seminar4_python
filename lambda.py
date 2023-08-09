# обычная версия
# list_1 = [1,5,4,8,7,6,21,5,4,8]
# res = list()

# for i in list_1:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)

# версия с лямбда

def select(f, col):
    return [f(x) for x in col]

# фунция select это расписанная версия функции map

def where(f, col):
    return [x for x in col if f(x)]

# функция where это расписанная версия функции filter

list_1 = [1,5,4,8,7]
res = select(int, list_1)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)