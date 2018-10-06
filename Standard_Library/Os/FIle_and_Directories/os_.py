import os
'''
The os module is responsible for manipulate, handle and create files/directories by working with the operational system

Todos lançam OSError caso exista algum problema com o comando, argumento ou acesso aos arquivos e diretórios
'''

#Files And Directories

#os.access(path, mode)      Verifica se o usuário tem permissão para acessar o path existente
'''
O parâmetro mode pode ser escrito de 4 maneiras:
    os.F_OK : Verifica se o caminho existe
    os.R_OK : Verifica se é possível ler algo do path
    os.W_OK : Verifica se é possível escrever algo no path
    os.X_OK : Verifica se algo é executável
'''
os.access('Desktop', os.W_OK)       #Output: True

'''
os.chdir(path)  Muda o diretório atual para o path
--> Caso o path seja o mesmo que o atual, WinError será levantado
--> * No Windows, o path deve ser escrito da forma 'C:\\directory\\directory1' com a separação feita por duas contra-barras
'''
os.chdir('c:\\Users\\RICARDO')

#os.getcwd() Retorna o path do diretório atual
os.getcwd()

'''
os.listdir(path='.')    Retorna todas as entradas disponíveis no diretório apresentado
                        Caso não seja passado nada como parâmetro, o diretório usado será o atual
                        Se a entrada for do tipo bytes, as saídas serão do tipo bytes
                        *Para mudar o encoding de str pra bytes, fsencode() deve ser usado
'''
os.listdir()
os.replace()
#os.mkdir(path) Cria um diretório com o nome do path
# Pode ser passado o caminho onde deve ser criado esse diretório
os.mkdir('Teste_os')
# Existe o makedirs(), que serve como uma opção recursiva do mkdir(), mas aceita a criação de mais de um diretório (family directories).

'''
os.remove(path) Remove o arquivo com o nome path
--> Possui o mesmo significado semântico que a função os.unlink()

--> Para deletar diretórios, deve ser usado os.rmdir()
'''

#os.removedirs(name) : Remove múltiplos diretórios
#os.rmdir() : Remove um diretório
os.rmdir('Teste_os')

#os.scandir()   : Retorna um iterável com todos os entries do diretório atual
#Os diretórios serão do tipo DirEntry
#'--> Para trabalhar com eles, é bom usar o atributo name, que o transforma em string