class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,value):
        newNode = Node(value)
        if self.head is None: self.head = newNode
        else:
            current = self.head
            while current.next: current = current.next
            current.next = newNode
            newNode.prev = current
    
    def reverse(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp: self.head = temp.prev

    def output(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

def main():
    # make double linked list
    list = DoubleLinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    list.insert(4)
    list.insert(5)
    # 1 2 3 4 5
    list.output()
    list.reverse()
    # 5 4 3 2 1
    list.output()

if __name__ == "__main__": main()