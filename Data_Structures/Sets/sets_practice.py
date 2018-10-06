''' Sets são tipos de dados de coleção desordenado que possuem somente elementos diferentes
    Suportam operações matemáticas como: União, Interseção, Diferença e Diferença simétrica

    Para criar um set, duas formas são possíveis: As chaves e a função set()
    '--> Para criar uma lista vazia, deve ser usado set() e não {} (Criaria um dicionário vazio)
'''

def set_sintax():
    set_1 = {'Hello', 'World', "I'm", 'Here!'}
    print(set_1)        #Quando acontece o print(), os valores são mostrados em ordem aleatória
    
    set_2 = set('Abacadabra')
    set_3 = set('Ricardo Alves Barbosa Filho')
    print(f'{set_2}\n{set_3}')


'''
    Operações Matemáticas:

    União:
    Interseção:
    Diferença:
    Diferença simétrica:
'''

def set_operations():
    a = set('propriedades')
    b = set('ricardo')
    symmetric = a - b   #Pega os elementos que estão em a, mas não estão em b
    union = a | b   #Pega os que estão em a ou b ou nos dois
    intersection = a & b    #Pega os elementos que estão nos dois sets
    xor = a ^ b     #Pega os que tem em a ou em b, mas não nos dois
    
    return print(f'\nSet 1: {a}\nSet 2: {b}\nSimétrico: {symmetric}\nUnião: {union}\nXor: {xor}\nInterseção: {intersection}\n')

def set_comprehension():
    a = {x for x in 'inconstitucional' if x not in 'aeiou'}
    return print(a)


if __name__ == '__main__':
    set_sintax()
    set_operations()
    set_comprehension()