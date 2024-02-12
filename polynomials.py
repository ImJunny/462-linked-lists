class Node:
    def __init__(self, coeff, deg):
        self.coeff = coeff
        self.deg = deg
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coeff, deg):
        newNode = Node(coeff,deg)
        if self.head is None: self.head = newNode
        else:
            current = self.head
            while current.next: current = current.next
            current.next = newNode

    def add(self,poly):
        p1 = self.head
        p2 = poly.head
        result = Polynomial()

        while p1 is not None and p2 is not None:
            if p1.deg > p2.deg:
                result.insert(p1.coeff, p1.deg)
                p1 = p1.next
            elif p1.deg < p2.deg:
                result.insert(p2.coeff, p2.deg)
                p2 = p2.next
            else:
                result.insert(p1.coeff+p2.coeff, p1.deg)
                p1 = p1.next
                p2 = p2.next

        while p1 is not None:
            result.insert(p1.coeff, p1.deg)
            p1 = p1.next

        while p2 is not None:
            result.insert(p2.coeff, p2.deg)
            p2 = p2.next

        return result
    
    def output(self):
        current = self.head
        while current is not None:
            print(f"{current.coeff}x^{current.deg}", end="")
            if current.next is not None: print(" + ",end="")
            current = current.next
        print()

def main():
    # x^2 + 5x + 1
    p1 = Polynomial()
    p1.insert(3,4)
    p1.insert(1,2)
    p1.insert(5,1)
    p1.insert(1,0)

    # 2x^4 + 4
    p2 = Polynomial()
    p2.insert(2,4)
    p2.insert(4,0)

    # add them
    p3 = p1.add(p2)
    p3.output()

if __name__ == "__main__": main()
    