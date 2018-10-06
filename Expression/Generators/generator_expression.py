'''
Generators são funções que retornam séries de valores.
Generators e Yield são os responsáveis por isso

Os generators, quando chamador novamente, voltam ao ponto que saíram anteriormente.
'--> Provavelmente, voltam a partir do yield

Se comparados às funções normais, que possuem só um único entry point, os generators podem possuir vários.

Quando uma função possui um yield, ela é um generator, mesmo que possua algum return em seu bloco.

Generator functions create generator iterators
'--> Como são considerados iteradores, possuem o método __next__(), que é responsável por chamar a próxima iteração.
    '--> Podem ser usados em for loops.


'''
#Example 1:
'''def simple_generator_function():
    yield 1
    yield 2
    yield 3

#Two Ways to use that function

#Way 1:
values = simple_generator_function()
print(next(values))
print(next(values))
print(next(values))

#Way 2:
for values in simple_generator_function():
    print(values)'''




from math import sqrt

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def solve_number_10():
    total = 2
    for next_prime in get_primes(3):
        #print(next_prime)
        print(get_primes(3))
        if next_prime < 2000:
            total += next_prime
            print(f'Total + {next_prime} é igual a {total}')
        else:
            print(total)
            return

def get_primes(number):
    while True:
        if is_prime(number):
            yield number            #Ponto de retorno
        print(number)
        number += 1 # <<<<<<<<<<

solve_number_10()


#Another Example:
def print_successive_primes(iterations, base=10):
    prime_generator = get_primes(base)
    prime_generator.send(None)              #Quando for iniciar um generator pela primeira vez com o send, é bom iniciar com None. Caso contrário, o generator não teria nenhum valor anterior para lidar
    for power in range(iterations):
        print(prime_generator.send(base ** power))          #O send tanto envia como retorna o valor "yieldado"