class DNode :
    def __init__(self, item, prev = None, next = None) :
        self.item = item
        self.prev = prev
        self.next = next
    
class LinkedDeque :
    def __init__(self) :
        self.front = None
        self.rear = None
    
    def isEmpty(self) :
        return self.front == None
    def clear(self) :
        self.front = self.rear = None
    def addFront(self, item) :
        node = DNode(item, None, self.front)
        if self.isEmpty() :
            self.front = self.rear = node
        else :
            self.front.prev = node
            self.front = node

    def addRear(self, item) :
        node = DNode(item, self.rear, None)
        if self.isEmpty() :
            self.front = self.rear = node
        else :
            self.rear.next = node
            self.rear = node
    def deleteFront(self) :
        if self.isEmpty() == False :
            data = self.front.item
            self.front = self.front.next
            if self.front == None :
                self.rear = None
            else :
                self.front.prev = None
            return data
    def deleteRear(self) :
        if self.isEmpty() == False :
            data = self.rear.item
            self.rear = self.rear.prev
            if self.rear == None :
                self.front = None
            else :
                self.rear.next = None 
            return data
    def peekFront(self) :
        data = self.front.item
        return data
    def peekRear(self) :
        data = self.rear.item
        return data
    def size(self):
        count = 0
        if self.isEmpty() == False:
            tmp = self.front
            while(1):
                if tmp !=None :
                    count += 1
                    tmp = tmp.next
                else :
                    break
        return count
    def print(self) :
        if self.isEmpty() == False :
            data = self.front
            while(1) :
                print(data.item, end = " ")
                data = data.next
                if data == None :
                    print("")
                    break
        else :
            print("")
    def revPrint(self) :
        if self.isEmpty() == False :
            data = self.rear
            while(1) :
                print(data.item, end = " ")
                data = data.prev
                if data == None : 
                    print("")
                    break
def main() :
    dq = LinkedDeque()
    print("Enter a command : af(addFront), df(deleteFront), pf(peekFront), s(size)")
    print("ar(addRear), dr(deleteRear), pr(peekRear), rp(reversePrint) or q(uit)")

    while True :
        print("> ", end ="")
        line = input().split()
        command = line[0]
        if command == 'af' :
            item = line[1]
            dq.addFront(item)
        elif command == 'df' :
            print(dq.deleteFront())
        elif command == 'pf' :
            print(dq.peekFront())
        elif command == 'ar' :
            item = line[1]
            dq.addRear(item)
        elif command == 'dr' :
            print(dq.deleteRear())
        elif command == 'pr' :
            print(dq.peekRear())
        elif command == 'p' :
            dq.print()
        elif command == 'rp' :
            dq.revPrint()
        elif command == 's' :
            print("size :", dq.size())
        elif command == 'q' :
            break

main()