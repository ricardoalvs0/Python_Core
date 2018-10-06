#Exemplos do uso dos generators e do yield

generator1 = (i for i in 'hello world') #Gera um generator object com os caracteres de 'hello world'.

def gerador():
    for i in range(10):
        yield i*2

