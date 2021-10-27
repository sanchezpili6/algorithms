# Given an integer, convert it to roman numeral

roman_values = [(1000, 'M'),
                (900, 'CM'),
                (500, 'D'),
                (400, 'CD'),
                (100, 'C'),
                (90, 'XC'),
                (50, 'L'),
                (40, 'XL'),
                (10, 'X'),
                (9, 'IX'),
                (5, 'V'),
                (4, 'IV'),
                (1, 'I')]


def int_to_roman(num):
    roman_value = ''
    for key, value in roman_values:
        d, num = divmod(num, key)
        roman_value += value * d
    return roman_value


number = input('Escribe un número entero: ')
print(int_to_roman(int(number)))
