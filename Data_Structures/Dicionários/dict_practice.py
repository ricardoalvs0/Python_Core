''' Os dicionários são uma espécie de set, mas com uma estrutura de chave:valor (key:value).
    Para criar um dicionário vazio, é usado o {}.
    '--> a = {}

    Usar a função list() retorna uma lista das chaves dentro do dicionário
    Com a função sorted() retorna as chaves ordenadas
'''

def dict_sintax():
    dicionario_1 = {'value_1': 100, 'value_2': 200, 'value_3': 300}
    valor_1 = dicionario_1['value_1']
    print(valor_1)
    
    dicionario_1['value_4'] = 400       #Isso adiciona a chave 'value_4' e insere o valor 400
    print(dicionario_1)

def dict_list():
    a = dict([('Hello', 123),('World', 456),('Github', 789)])
    print(list(a))
                                # O dict pode receber uma lista de tuplas com a chave e o valor
def dict_sort():                # Se as chaves forem strings, pode somente passar o valor: string=valor
    a = dict(World=45, Of=37, Warcraft=95)
    print(sorted(a))

def dict_comprehensions():              # Quando uma chave é sobrescrita, a antiga é apagada
    dict_test = {str(x): x**2 for x in (2, 3, 4, 5, 6)}
    return print(dict_test)


'''Different ways to write a dictionary'''
# Model: {'one': 1, 'two': 2, 'three': 3}
a = dict(one=1, two=2, three=3)
b = {'one':1,'two':2, 'three':3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('one', 1), ('three', 3), ('two', 2)])
e = dict({'one':1,'two':2, 'three':3})

print('True') if (a == b == c == d == e) else print('False')    # IF|ELSE de uma linha

                                # Para excluir algum elemento, usa-se a função del() com a chave como argumento
if __name__ == '__main__':      # As operações in e not in são usadas com as chaves do dicionário
    dict_sintax()
    dict_list()
    dict_sort()
    dict_comprehensions()