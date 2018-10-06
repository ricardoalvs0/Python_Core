#next()
'''
O next é responsável pela iteração dentro do generator. 
Automatizado pelo for, esse método "entra" no generator e retorna o valor do próximo yield para o 'caller'.
Caso não exista outro valor a ser retornado pelo yield, StopIterator é raised.
'''
def next_example():
    n = 1
    while(n<10):
        yield n
        n+=1
exemplo_next = next_example()
print(next(exemplo_next))   #Output: 1
print(next(exemplo_next))   #Output: 2

#send()
'''
O send é responsável por enviar um valor para o generator e retornar o próximo valor gerado pelo generator.
'''
def send_example(n):
    while(n<10):
        yield n
        n+=1

exemplo_send = send_example(2)  #Esse é o valor base para essa função
print(exemplo_send.send(None))  #Inicialização deve ser sempre None
print(exemplo_send.send(3))     #Não importa o valor passado como parâmetro, pois o generator continua com seu processamento base
print(exemplo_send.send(None))  #--^

#close()
'''
O close dispara o StopIterator num generator.
'''
def close_example():
    n = 1
    while n < 10:
        yield n
        n+= 1

exemplo_close = close_example()
print(next(exemplo_close))
exemplo_close.close()

#throw()
'''
O throw tem o papel de levantar um erro dentro do generator e deixa o generator exhausted.
'''
def throw_example():
    n = 1
    while n < 10:
        yield n
        n+= 1

exemplo_throw = throw_example()
exemplo_throw.throw(TypeError, 'Spam') #Output: Traceback TypeError