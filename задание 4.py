num1 = int(input('введите число'))
roman_dict = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C'}
keys = list(roman_dict)
symbols = list(roman_dict.values())
i = 8
num2 = ""
while num1 != 0:
    if keys[i] <= num1:
        num2 += symbols[i]
        num1 -= keys[i]
    else:
        i -= 1
print('ваше число:',num2)