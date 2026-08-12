# name = "Sasha"
# age = 99 # целое число
# age1 = "99"  # строка
#
# print(name)
# print(age * 3) # 297
# print(age1 * 3) # 999999
# #  +  -  /   *
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print(a + b)
#
# if a > b:
#     print("А наибольшее число")
# elif a < b:
#     print('B наибольшее число')
# else:
#     print('числа равны')
#
# # Булевый (логический)
# # True - истина  False - ложь
#
# print(77 > 66) # True
# print(77 != 66) # True
# print(77 == 66) # False
#
#

# and - логическо умножение
# or - логическое сложение
# not - смена знака
# True = 1
# False = 0
# print(not (False and True) or (False or True))
# -(0 * 1) + (0 + 1)
#  True  +  True = True

score = 0

# условный цикл while (пока)
while score < 50:
    score = score + 10
    print(score)

result = 0
while True:
    num = int(input('Enter a number: '))
    result = result + num
    if num == 0:
        break
print(result)






