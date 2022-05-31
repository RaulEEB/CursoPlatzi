
class TwoWayNode(object):

    def __init__(self,data = None, next=None,previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self,data):
        new_nodo = TwoWayNode(data,None,None)
        if self.head is None:
            self.head = new_nodo
            self.tail = self.head
        else:
            new_nodo.previous = self.tail
            self.tail.next =  new_nodo
            self.tail = new_nodo

        self.count += 1

    def dequeue(self):
        current = self.head
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1

        return current.data
    
if __name__ == '__main__':
    food = Queue()
    food.enqueue('eggs')
    food.enqueue('ham')
    food.enqueue('spam')
    print(food.head.data)
    print(food.head.next.data)
    print(food.tail.data)
    print(food.tail.previous.data)
    print(food.dequeue())
    print(food.head.data)
