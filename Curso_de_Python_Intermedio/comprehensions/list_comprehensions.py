"""
Creado listas con list comprehensions
[element for element in iterable if condition]
"""

def list_squares():
    my_list = [ x**2 for x in range(1, 11)]  # elevar al cuadrado una lista
    return my_list

# cuadrado de numeros no divisibles entre 3
def list_squares_three():
    my_list = [ i**2 for i in range(1, 11) if i % 3 != 0]
    return my_list


def list_challenge():
    my_list = [ i for i in range(1,10000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    return my_list


def run():
    # print(list_squares())
    # print(list_squares_three())
    print(list_challenge())

if __name__ == '__main__':
    run()