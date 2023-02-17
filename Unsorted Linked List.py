## 문제 1. 스택을 연결 구조를 사용하여 구현한다. 클래스 Stack을 구현하고 실행한 결과와 같이 되도록 코딩한다. 

class Node :
    def __init__(self, item, next = None) :
        self.item = item
        self.next = next

class LinkedStack : 
    def __init__(self) :
        self.top = None
    def isEmpty(self) :
        return self.top == None
    def size(self) :
        node = self.top
        count = 0
        while not node == None :
            node =  node.next
            count += 1
        return count
    def clear(self) :
        self.top = None
    def push(self, item) :
        n = Node(item, self.top)
        self.top = n
    def pop(self) :
        if not self.isEmpty() :
            n = self.top
            self.top = n.next
            return n.item
    def peek(self) :
        if not self.isEmpty() :
            return self.top.item
    def print(self) :
        node = self.top
        while not node == None :
            print(node.item, end = ' ')
            node = node.next

def main() :
    stack = LinkedStack()
    print("Enter a command : pop, push, peek, size, empty, p(rint), m(atch), q(uit)")
    while True :
        print("> ", end = "")
        line = input().split()
        command = line[0]
        if command == 'push' :
            item = line[1]
            stack.push(item)
        elif command == 'pop' :
            print(stack.pop())
        elif command == "peek" :
            print(stack.peek())
        elif command == "empty" :
            print(stack.isEmpty())
        elif command == "size" :
            print(stack.size())
        elif command == "p" :
            stack.print()
            print("")
        elif command == "q" :
            break

main()


## 문제 2. 정렬되지 않은 리스트를 연결 구조를 사용하여 구현한다. 클래스 UnsortedLinkedList를 구현하고 실행한 결과와 같이 되도록 코딩한다.

class Node :
    def __init__(self, it, nt = None) :
        self.item = it
        self.next = nt

class UnsortedLinkedList :
    def __init__(self) :
        self.head = None
        self.count = 0
    def isEmpty(self) :
        return self.head == None
    def clear(self) :
        self.head = None
        self.count = 0
    def insertFirst(self, data) :
        newNode = Node(data, self.head)
        self.head = newNode
        self.count += 1
    def insertLast(self, data) :
        if self.head == None :
            self.head = Node(data, self.head)
            self.count += 1
        else :
            tmp = self.head
            while tmp.next != None :
                tmp = tmp.next
            tmp.next = Node(data)
            self.count += 1
    def remove(self, data) :
        if self.isEmpty() :
            raise Exception("List is empty")
        prev = None
        curr = self.head
        while curr != None :
            if curr.item == data :
                break
            prev = curr
            curr = curr.next
        if curr is None :
            return False
        elif prev is None :
            self.head = self.head.next
            self.count -= 1
        else :
            prev.next = curr.next
            self.count -= 1
        return True
    def find(self, data) :
        if self.isEmpty() :
            raise Exception("List is empty")
        curr = self.head
        while curr != None :
            if curr.item == data :
                break
            curr = curr.next
        try :
            if curr.item == data :
                return True
            else :
                return False    
        except :
            return False
    def size(self) :
        return self.count
    def print(self) :
        node = self.head
        while node != None :
            print(node.item, end = " ")
            node = node.next
        print()

def main() :
    lst = UnsortedLinkedList()
    print("Enter a command : inf(insertFisrt), inl(insertLast), e(mpty), c(lear),")
    print("r(emove), f(ind), p(rint): ")
    while True :
        print("> ", end = "")
        line = input().split()
        command = line[0]
        if command == 'inf' :
            lst.insertFirst(line[1])
        elif command == 'inl' :
            lst.insertLast(line[1])
        elif command == 'e' :
            print(lst.isEmpty())
        elif command == 'c' :
            lst.clear()
        elif command == 'p' :
            lst.print()
        elif command == 's' :
            print(lst.size())
        elif command == 'r':
            elem = line[1]
            try :
                if lst.remove(elem) :
                    print(elem, " removed")
                else :
                    print("No such element")
            except Exception as e:
                print(e)
        elif command == 'f' :
            elem = line[1]
            try :
                if lst.find(elem) :
                    print(elem, " found")
                else :
                    print("No such element")
            except Exception as e :
                print(e)
        elif command == 'q' :
            break

main()
