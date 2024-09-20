# решением задачи будут все промежуточные числа, кроме самого результата перемножения
# пример если плитка 3 на 4, значит одним прямым разломом можно будет получить только 3, 6 по горизонтали или 4, 8 по вертикали
# исходя из введенных данных, нужно создать список со всеми возможными комбинациями и смотреть есть ли последнее введенное число в этом списке

w = int(input('введите длину:'))
l = int(input('введите ширину:'))
slice_c = int(input('введите кол-во кусочков'))
slice_p = []
for i in range(1, w):
    slice_p.append(i * l)
for i2 in range(1, l):
    slice_p.append(i2 * w)
# print(slice_p)
if slice_c in slice_p:
    print(True)
else:
    print(False)

# так подажжи..
# или не нужно..
#
# a = int(input('введите длину:'))
# b = int(input('введите ширину:'))
# c = int(input('введите кол-во кусочков:'))
# if c >= a * b:
#     print(False)
# elif c % a == 0:
#     print(True)
# elif c % b == 0:
#     print(True)
# elif c % a != 0:
#     print(False)
# elif c % b != 0:
#     print(False)

