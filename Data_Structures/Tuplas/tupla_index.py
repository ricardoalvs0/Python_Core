class Tuplas_indexed:

    def tuple_generator(self):      #Gera tupla com 5 números aleatórios
        from random import randint
        a = []
        for i in range(5):
            x = randint(0, 200)
            a.append(x)
        return tuple(a)

    def tuple_indexer(self):
        t = self.tuple_generator()
        print(f'\t{t}')
        print(f't[0]:{t[0]} t[1]:{t[1]} t[2]:{t[2]} t[3]:{t[3]} t[4]:{t[4]}',end='\n\n')

    def tuple_operators(self):
        t = (1, 2, 3, 1, 4, 5)
        rep = t.count(1)
        ind = t.index(1)
        return print(f'\t{t}\nA contagem de valores igual a 1 é: {rep}\nO endereço primário do valor 1 é: {ind}')

    def tuple_in_or_not(self):
        t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
        response = 3 in t
        not_response = 45 not in t      #As tuplas suportam expressões booleanas in|not in
        return print(f'\t{t}\n\t3 in t? {response}\n\t45 in t? {not_response}')

    def tuple_slice(self):
        t = (99, 11, 22, 33, 44)
        t_ = t[:3]      #A tupla t_ adquire os valores do endereço 0 ao endereço anterior ao 3
        return print(f'\n\tSlice\n\tt {t} t_ == t[:3]\n\tt_ {t_}')

    def tuple_concat(self):
        t = self.tuple_generator()
        t_ = t, 'Hello World' ,t[1:4]
        return print(f'\t{t}\n{t_}')

    def tuple_nest(self):
        t1 = self.tuple_generator()
        t2 = self.tuple_generator()
        t3 = t1 , t2
        print(f'\n\t{t1}\n\t{t2}\n{t3}\n')          #As tuplas podem ser multidimensionais, suportando x[1][2][3][4][5][6][7][8][9][10]
        for j in range(len(t3)):
            for i in range(len(t3[0])):
                print(f'\t\tt[{j}][{i}]: {t3[j][i]}')
        return

    def tuple_2(self):
        import math
        for x, y in ((-3, 4), (1, 2), (3, 4), (9, 12)):
            print(math.hypot(x, y))
        return

if __name__ == '__main__':
    tupla = Tuplas_indexed()
    tupla.tuple_generator()
    tupla.tuple_indexer()
    tupla.tuple_operators()
    tupla.tuple_in_or_not()
    tupla.tuple_slice()
    tupla.tuple_concat()
    tupla.tuple_nest()
    tupla.tuple_2()