import os, os.path

#os.path.abspath(path)
# Retorna uma forma normalizada com o path atual e o path passado
# Equivalente a: join(os.getcwd(), path)
print(os.path.abspath('Desktop'))   #Output: 'C:\\Users\\RICARDO\\Desktop'

#os.path.basename(path)
# Irá retornar a base do pathname, que é o segundo elemento no path
# Será o segundo diretório no caso de se passar o path em um split
print(os.path.basename(os.getcwd()))    #Output: 'RICARDO'

#os.path.commonpath(paths)
#Retorna a maior parte de path em comum entre uma lista de paths
a = os.getcwd()
b = os.path.abspath('Desktop')
print(os.path.commonpath([a, b]))   #Output: 'C:\\Users\\RICARDO'

#os.path.commonprefix(list)
#Retorna o maior prefixo no path, caractere por caractere
print(os.path.commonprefix(['user\\RICARDO\\local', 'user\\RICARDO\\lib']))
#'--> Output: 'user\\RICARDO\l'

#os.path.dirname(path)
#Análogo ao basename, este retorna o primeiro diretório do split do path atual
print(os.path.dirname(os.getcwd()))

#os.path.exists(path)
#Retorna True ou False caso o diretório exista
#Retornará False caso o usuário não tenha permissão de acesso, mesmo que o diretório exista
print(os.path.exists(os.getcwd()))
#Existe o lexists(), que possui a mesma função

#os.path.getatime(path) : Retorna o tempo desde o último acesso
#os.path.getmtime(path) : Retorna o tempo desde a última modificação
#os.path.getctime(path) : Retorna o tempo desde a criação
#'--> Todos retornam o tempo desde 1 Jan de 1970

#os.path.getsize(path)  : Retorna o tamanho, em bytes, do path.
#'--> Raises a OSError if the file not exist or is inacessible.

'''
os.path.isabs(path) : Retorna True se o path for um absolute pathname, que é a forma "normalizada"
os.path.isfile(path): Retorna True se for um arquivo ou um link simbólico.
os.path.isdir(path) : Retorna True se for um diretório ou um link simbólico.
os.path.islink(path): Retorna True se for um link simbólico, e retorna False se o link não for suportado pelo Python runtime.
os.path.ismount(path): ???
'''

#os.path.join(path,*paths)
#Junta de forma formatada o path passado com o ou os paths passados no segundo argumento.
#Deve ter cuidado na hora de juntar o drive letter, pois as duas contra-barras não serão adicionadas
a = ['Desktop', 'Python_Core']
os.path.join(os.getcwd(),*a)

#os.path.normcase(path)
#Esta é a função que traduz o path para o path normalizado de acordo com o sistema operacional
os.path.normcase('C:/User/Ricardo/Desktop') #Output: 'c:\\user\\ricardo\\desktop'
#Retorna tudo em minúsculo

#os.path.normpath(path)
#Vai tirar as separações redundantes
#Pode mudar o significado de um path que contém links simbólicos
os.path.normpath('desktop/python_core/Os//')    #Output: 'desktop\\python_core\\Os'

#os.path.relpath(path, start=os.curdir)
#Retorna o path relativo em relação ao start, que primáriamente é o diretório atual.

#os.path.realpath(path)
#Retorna o path sem links simbólicos

'''
os.path.samefile(path1, path2)  : Retorna True se os argumentos se referem ao mesmo arquivo ou diretório.
os.path.sameopenfile(fp1, fp2)  : Retorna True se o descritores fp1 e fp2 apontam para o mesmo arquivo
'''

#os.path.split(path)
#Retorna uma tupla com dois objetos, em que o primeiro é o path até o penúltimo diretório e o segundo é o último diretório
os.path.split('C:\\Users\\RICARDO') #Output: ('C:\\Users','RICARDO')

#os.path.splitdrive(path)
#Retorna a drive letter
os.path.splitdrive('C:\\Users') #Output: ('C:','\\Users')

os.path.supports_unicode_filenames
#Retorna True se os diretórios puderem ser nomeados com caracteres Unicode