# print('test')
# a = 10
# b = a
# c = b
# print(c)


r = [1, 2, 3, 4, 5, 1, 2, 3]
# print(r.index(3,3))
# print(r.count(3))


choose_from_two = ('A', 'B', 'C')
answer = []
answer.append('A')
answer.append('B')
# print(choose_from_two)
# print(answer)

# x = 10
# if x < 0:
#     print('negative')
# elif x == 0:
#     print('zero')
# elif x == 10:
#     print('10')
# else:
#     print('positive')

# is_ok = 0
# if is_ok:
#     print('OK')
# else:
#     print('NO')

# print(1 is True)
# print(None is None)

# count = 0
# while count < 5:
#     print(count)
#     count+=1

# count = 0
# while True:
#     if count >= 5:
#         break
#     if count == 2:
#         count += 1
#         continue
#
#     print(count)
#     count += 1

# --40--
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('done')

# while count < 5:
#     if count == 3:
#         break
#     print(count)
#     count += 1
# else:
#     print('done')
# ---- #


# -- 41 --
# while True:
#     word = input('Enter:')
#     if int(word) == 100:
#         break
#     else:
#         print('next')
# ---- #


# -- 42 --
some_list = [1,2,3,4,5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# for i in some_list:  # iterator
#     print(i)
#
# for s in 'abcde':
#     print(s)

import pandas
# def g_hello():
#     yield 'hello 1'
#     yield 'hello 2'
#     yield 'hello 3'
# g = g_hello()
# print(next(g))
# print(next(g))
# print(next(g))
def g_hello():
    r = yield 'hello'
    yield r
g = g_hello()
print(next(g))
print(g.send('plus'))



# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# added_list = []
# for i in range(0,len(list1)):
#     added_list.append(list1[i]+list2[i])
# added_list