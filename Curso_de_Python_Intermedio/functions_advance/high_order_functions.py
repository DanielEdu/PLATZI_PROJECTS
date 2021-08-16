"""
SUMMARY.

--------
* Tittle: 
    High order functions (hof).
* Description:
    A function that receives another function like a parameter and can execution it
    las funciones de orden superior retornan un iterador, se aplica list() para convertirlo a lista
    resiven un iterable, como una lista por ejemplo
"""
from functools import reduce

MY_LIST = [1,2,3,4,5,7,8,10,14,17,19]


def filter_list(my_list):
    odd = [ i for i in my_list if i%2 != 0]
    return odd


def filter_hof(my_list):
    odd = list( filter(lambda x: x%2 !=0, my_list))
    return odd


def square_hof(my_list):
    odd = list( map(lambda x: x**2, my_list))
    return odd


def reduce_hof(my_list):
    odd = reduce(lambda a, b: a*b, my_list)
    return odd


def run():
    print(reduce_hof(MY_LIST))

if __name__ == '__main__':
    run()