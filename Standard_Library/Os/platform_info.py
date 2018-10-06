import platform

#Saber o sistema operacional:
print('Sistema Operacional: '+ platform.system())

#Saber a arquitetura do processador:
print('Processador: ' + platform.machine())

#Saber a Rede, ou o nome do computador:
print('Rede: '+ platform.node())

#Exibir algumas informações sobre o Windows:
print('Windows: '+ platform.platform())

#Versão do Python:
print('Python: '+platform.python_version())