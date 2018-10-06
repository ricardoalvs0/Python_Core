def matriz_transposta():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],          #Pode ser feito de outra forma
        [7, 8, 9]
    ]
    transposta = [[row[i] for row in matriz] for i in range(3)]
    return print(transposta)

def zip_list():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],          
        [7, 8, 9]
    ]                               # A diferença é que este retorn uma tupla
    lista = list(zip(*matriz))      # O asterisco é usado pra denotar quando a variável passada deve ser expandida em um iterável
    return print(lista)

if __name__ == '__main__':
    matriz_transposta()
    zip_list()