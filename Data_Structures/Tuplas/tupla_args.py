# Estudo sobre tuplas e suas propriedades

def tupla_sem_parentese():
    tupla1 = 1, 2, 3
    return print(f'Tupla sem parêntese {tupla1}')           # As tuplas podem ser escritas somente por vírgulas, sem necessidade dos parênteses

def tupla_com_parentese():
    t = (1, 2, 3)
    return print(f'Tupla com parêntese {t}')

def tupla_com_argumento():
    tupla = "Hello", "World", "34", 47
    return print(f'Tupla com argumento {tupla}')

def tupla_aninhada():
    t = "Tuple", "Data Structure", tupla_generica()
    return print(f'Tupla aninhada {t}')
def tupla_generica():
    return 7, 8, 9


if __name__ == '__main__':
    tupla_com_argumento()
    tupla_sem_parentese()
    tupla_com_parentese()
    tupla_aninhada()