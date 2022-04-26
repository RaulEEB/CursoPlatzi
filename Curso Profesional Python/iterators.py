import time 

class FiboIter():
    
    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.count = 0
        return self

    def __next__(self):
        if self.count == 0:
            self.count += 1
            return self.n1
        elif self.count == 1:
            self.count += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            #self.n1 = self.n2
            #self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            if self.aux >= self.max:
                raise StopIteration
            return self.aux
        

if __name__ == '__main__':
    fibo = FiboIter(100)
    for element in fibo:
        print(element)
        time.sleep(0.5)
