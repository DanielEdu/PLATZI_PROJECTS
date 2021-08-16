

def divisor(num):
    divisor = []
    for i in range(1, num+1):
        if num % i == 0:
            divisor.append(i)
    return divisor

def run():
    num = input('write a number \n')
    assert num.isnumeric(), "debes ingresar un número"   #eleva una exception
    print(divisor(int(num)))



if __name__ == '__main__':
    run()