test_dict = dict(t1=1, t2=2, t3=3, t4=4)

#len(dict) mostra quantos elementos (key:value) existem no dicionário
print(len(test_dict))

#d[key] retorna o valor da chave. Caso não exista, KeyError é levantado
'''
    Caso uma subclasse de dict queira agir de outra maneira com o fato de não existir key correspondente,
    esta deve declarar o método __missing__, que será chamado ao invés de KeyError.

    Ex.:
    class Dict_son(dict):
        def __missing__(self, key):
            return 0
'''
print(test_dict['t1'])

'''
    d[key] = value : Muda ou cria o valor da chave key para value
    del d[key] : Exclui a key:value do dicionário. Raise a KeyError if key is not in the map
    key in d | key not in d : Membership Test
    clear() : Limpa o dicionário
    copy() : Retorna uma cópia do dicionário. fromkeys() é um método que retorna um novo dicionário, mas com os valores None
    iter(dict) : Transforma as chaves do dicionário em um iterável
    get(key) : Retorna o valor da chave. Nunca retorna KeyError, e sim None caso não exista a chave passada
    items() : Retorna um modo de visualização dos itens do dicionário
    keys() : Retorna as chaves do dicionário
    pop() : Deleta o item e retorna o valor da chave passada. Raises a KeyError
    popitem() : Deleta e retorna o item (key:value). Also raises a KeyError
    setdefault() : Se a chave estiver no dicionário, retorna o valor. Caso a chave não exista, o método cria uma chave e atribui valor None a ela
    update([other]) : Atualiza o dicionário com o que for passado. Retorna None. Aceita kwargs também
    values() : Retorna a visualização dos valores no dicionário.
'''
print(list(iter(test_dict)))
print(test_dict.get('t3'))
print(test_dict.items())
print(test_dict.keys())
print(test_dict.pop('t3'))
print(test_dict.setdefault('t1'))
test_dict.setdefault('t5')
print(test_dict.items())