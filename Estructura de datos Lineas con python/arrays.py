
class Arrays:

    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    
    def __len__(self):
        return len(self.items)

    def __string__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self,index, new_item):
        self.items[index] = new_item

if __name__ == '__main__':
    array = Arrays(capacity=5)
    for i in range(len(array)):
        array[i] = i + 1
    print(array.__getitem__(3))
    print(array[1])

    #len(array)
    #print(array)
    