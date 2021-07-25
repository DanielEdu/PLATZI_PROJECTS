


from utils import data 




def filter_list_comprenhension(data):
    """ ejercicio con list comprenhension"""
    all_python_devs = [ worker["name"] for worker in data if worker["language"] == "python" ]
    return all_python_devs


def filter_hof(data, lp):
    """ filtrar y mapear valores de una lista de diccionarios """
    all_python_devs = list( filter(lambda x:  x["language"] == lp, data) )
    all_python_devs = list( map(lambda x: x["name"], all_python_devs))
    return all_python_devs


def add_flag(data):
    """ agregar una nueva llave con un MAP  """
    is_old = list( map(lambda x:x | { "old": x["age"] > 65 }, data) )
    return is_old



def run():
    #for worker in filter_list_comprenhension(data.DATA):
        #print(worker)

    for worker in filter_hof(data.DATA, "java"):
        print(worker)

    for worker in add_flag(data.DATA):
        print(worker)



if __name__ == '__main__':
    run()