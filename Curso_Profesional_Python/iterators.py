import time


class FiboIter():
    def __init__(self):
        pass
    
    
    def __iter__(self):
        '''Elementos necesarios'''
        self.n1, self.n2 = 0, 1
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
    
def main():
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.3)

            
if __name__ == '__main__':
    main()
    