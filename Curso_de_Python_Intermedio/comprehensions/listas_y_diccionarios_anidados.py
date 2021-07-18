
import pandas as pd

#####################
my_list = [1, "Hello", True, 4.5]
my_dict = {
    "firstname": "Daniel",
    "lasname": "Portugal"
}

SUPER_LIST = [
    {"firstname": "Daniel", "lasname": "Portugal"},
    {"firstname": "Daniel", "lasname": "Portugal"},
    {"firstname": "Daniel", "lasname": "Portugal"},
    {"firstname": "Daniel", "lasname": "Portugal"}
]

SUPER_DICT = {
    "natural_numbers": [1, 2, 3, 4, 5],
    "integer_numbers": [-1, -2, 0, 1, 2, 3],
    "floating_numbers": [-1.1, -2.4, 2.5, 3.75],
}

# FIXME 
def run():
    for key, value in SUPER_DICT.items():
        print(key, '-', value)

    for i in SUPER_LIST:
        print(i)


if __name__ == '__main__':
    run()