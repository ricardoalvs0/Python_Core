from list_sintax import List_Comprehension
class List_method_practice(List_Comprehension):
    def list_extensor(self):
        model = super().list_generator(5)   #a sintaxe de herança é super()
        print(model)
        lista = ['a', 'b', 'c']
        model.extend(lista)         #Output: [elements, 'a', 'b', 'c']
        return print(model, end='\n\n')

    def list_insert(self):
        model = super().list_generator(5)
        print(model)
        lista = super().list_generator(5)
        model.insert(2, lista) #O insert dá a liberdade de escolha para o índice a ser guardado o segundo argumento
        return print(model)

    def list_remove(self):
        model = super().list_generator(5)
        print(model)            #Remove o primeiro elemento com o valor passado
        model.remove(model[0])         #Se o valor não existir, ValueError é levantado.
        return print(model)

    def list_popper(self):
        lista = super().list_generator(5)
        print(lista)                    #Remove o valor que está no endereço passado e retorna o valor.
        return print(lista.pop(2))

    def list_index(self):
        lista = super().list_generator(5)
        return print(lista.index(lista[4]))     #Retorna o endereço que o elemento está sendo passado.

    def list_sort(self):
        lista = super().list_generator(5)
        print(lista)
        lista.sort()        #Ordena as listas de acordo com o valor ou em ordem alfabética
        print(lista)
        return

if __name__ == '__main__':
    method_practice = List_method_practice()
    method_practice.list_extensor()
    method_practice.list_insert()
    method_practice.list_remove()
    method_practice.list_popper()
    method_practice.list_index()
    method_practice.list_sort()