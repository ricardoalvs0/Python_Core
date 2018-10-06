# Study of the del statement in list comprehensions
def del_practice():
    example = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    del example[2:4]
    return print(example)           #Deleta as fatias que são passadas ao argumento

if __name__ == '__main__':
    del_practice()