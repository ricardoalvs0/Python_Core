'''
    Existem alguns métodos de comparação entre sets:
        x in set
        x not in set
        issubset()
        issuperset()
        isdisjoint()
'''

#isdisjoint(other_set) : Retorna True se um set não tiver elementos do outro set (Somente se a interseção for um conjunto vazio).
a = set('Hello World')
b = {'Hello', 'World'}
print(a.isdisjoint(b))      # Output: True, because the a set is a set that have just letters inside. Otherwise, the b set have the words 'Hello' and 'World'.

#issubset(other_set)
test_sub = set('aeiou')
test = set('abcdefghijklmnopqrstuvxz')
print(test_sub.issubset(test))

#issuperset(other_set)
print(test.issuperset(test_sub))

#Para melhorar a escrita e operações com os sets, temos expressões literais para cada expressão

# O método union() reúne os dados de dois ou mais sets
c = set('abcd')
print(a.union(b.union(c)))      # Concatenação de union()

# intersection() junta os elementos de dois ou mais sets
print(a.intersection(c))        # Output: {'d'}

#difference()
print(a.difference(c))      # Retorna um set com elementos que estão somente em um set e não estão no outro

#symmetric_difference() É o mesmo que o difference, mas faz o processo para os dois lados
print(a.symmetric_difference(c))

# copy() retorna uma cópia do set chamado
test_copy = a.copy()
print(test_copy)

'''
    Outro tipo de set é o frozenset, que é um tipo que não aceita alterações (immutable)
    *Obs.: Em operações binárias, o retorno depende do tipo que for escrito primeiro --> frozenset('abc') | set('abc') will return a frozenset type
'''

_frozen = frozenset(['Hello', 'World'])
for _ in _frozen:
    print(_)

''' Alguns métodos são disponíveis somente para os sets e não para frozensets'''
a.update([1, 2, 3])     # Adiciona os elementos passados como argumento no set
print(a)

a.intersection_update(['a', 'b', 'e', 1, 2, 3])     #Atualiza o set para que contenha somente os valores que estiverem no set original e no argumento
print(a)

a.difference_update({1, 2, 3, 'W'})           # Tanto esse como o symmetric_difference_update() atualizam o set com o funcionamento similar ao da função primária
print(a)

''' Outros métodos:
    --> add()
    --> pop() Remove e retorna o elemento   \ ____ Ambos levantam Key Error caso o elemento não esteja no set
    --> remove() Remove o elemento          /
    --> discard() Remove o elemento caso esteja presente
    --> clear(): Limpa o set
'''