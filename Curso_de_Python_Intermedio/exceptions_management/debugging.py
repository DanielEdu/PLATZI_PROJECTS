"""
1. Go to Run and Debug on the code editor
2. Python file
3. Put a Breakpoint
"""



def divisor(num):
    divisor = []
    for i in range(1, num+1):
        if num % i == 1:
            divisor.append(i)
    return divisor

def run():
    num = int(input('write a number \n'))
    print(divisor(num))



if __name__ == '__main__':
    run()