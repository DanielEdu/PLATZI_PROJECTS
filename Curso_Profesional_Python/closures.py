'''
 * Closure
'''


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puede utilizar cadenas de texto'
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    repeat_10 = make_repeater_of(10)
    
    print(repeat_5('Daniel '))
    print(repeat_10('Valen '))
    

if __name__ == '__main__':
    run()
    
