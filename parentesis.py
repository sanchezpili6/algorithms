# Recibes una string conteniendo solo () y []
# Crea un algoritmos para validar que la sintaxis de los corchetes es correcta:
# Ejemplos validos:
# '()'
# '()()()()()()()()()'
# '([])[]()'
# Ejemplos no validos:
# ')'
# '()['
# '(([))]'
# '(((((((((((((((((((((((((((((((((('

VALID_PARENTHESES_STRING = '()()()()()()()()()'
INVALID_PARENTHESES_STRING = '())](())[]'
OPENING_CHARS, CLOSING_CHARS = '([', ')]'


def parentheses(parentheses_string):
    if not parentheses_string:
        return True
    for i, character in enumerate(parentheses_string):
        if character in CLOSING_CHARS:
            index = CLOSING_CHARS.index(character)
            if parentheses_string[i-1] != OPENING_CHARS[index]:
                return False
            return parentheses(parentheses_string[:i-1] + parentheses_string[i+1:])
    return False


parentheses_string = input("Escribe un string de paréntesis y/o llaves: ")
print(parentheses(parentheses_string))