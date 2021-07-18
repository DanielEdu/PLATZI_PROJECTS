"""
SUMMARY.

--------
* Description:
    creando diccionarios con comprehensions
    {key: element for element in iterable if condition}
"""

from math import sqrt
import json

def dictionary_challenge():
    my_list = { i: i**3 for i in range(1,11) if i % 3 !=0 }
    return my_list


def dictionary_sqrt():
    # my_dict = {i : round(i**0.5,3) for i in  range(1,1001)}
    my_dict = {i : round(sqrt(i),3) for i in  range(1,1001)}
    return my_dict


def run():
    print(dictionary_challenge())
    print(json.dumps(dictionary_sqrt(), indent=2))


if __name__ == '__main__':
    run()