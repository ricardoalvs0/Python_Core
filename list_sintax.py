class List_Comprehension:
    
    def list_generator(self, n_elements):
        from random import randint
        final_list = []
        for _ in range(n_elements):
            random_number = randint(0, 1000)
            final_list.append(random_number)
        return final_list

    def list_sintax(self):
        lista = []
        lista0 = self.list_generator(5)
        return print(f'lista [] =  {lista}\nlista = [{lista0[0]},{lista0[1]},{lista0[2]},{lista0[3]},{lista0[4]}] = {lista0}')

    def list_copy_clone(self):
        model = [1, 2, 3, "Hell'o World"]
        lista = model[:]
        print(f'\n{model} <-- Lista inicial\n{lista}<-- Lista Clone')
        model[0] = 100      #A lista está recebendo um clone da lista 'model', e portanto, não refencia ao mesmo endereço.
        return print(f'Lista Inicial[0] = 100\n\tLista clone = {lista}\tLista inicial = {model}')

    def list_copy(self):
        model = self.list_generator(4)
        lista = model       #Aqui está sendo passado o endereço da lista, e não os seus valores.
        print(f'\nLista inicial = {model}\tLista Clone = {lista}')
        model[0] = 'Hello World'
        return print(f'Após a mudança: Lista inicial = {model}\tLista Clone = {lista}')

if __name__ == '__main__':
    practice = List_Comprehension()
    practice.list_sintax()
    practice.list_copy_clone()
    practice.list_copy()