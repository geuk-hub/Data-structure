## 문제 1. 덱을 이중 연결 구조 사용하여 구현한다. 클래스 LinkedDeque를 구현하고 실행한 결과와 같이 되도록 코딩한다. 

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

## 문제 2. 원형 이중 연결 리스트를 구현한다. 클래스 CircularDoublyLinkedList를 구현하고 실행한 결과와 같이 되도록 코딩한다.

class DNode :
    def __init__(self, item, prev = None, next = None) :
        self.item = item
        self.prev = prev
        self.next = next

class CircularDoublyLinkedList :
    def __init__(self) :
        self.head = None
    def isEmpty(self) :
        return self.head == None
    def clear(self) :
        self.head = None
    def addFront(self, item) :
        node = DNode(item)
        if self.isEmpty() :
            self.head = node
            self.head.prev = node
            self.head.next = node
        else :
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev.next = node
            self.head.prev = node
            self.head = node

    def addRear(self, item) :
        node = DNode(item)
        if self.isEmpty() :
            self.head = node
            self.head.prev = node
            self.head.next = node
        else :
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev.next = node
            self.head.prev = node
    
    def deleteFront(self) :
        if self.isEmpty() == False :
            data = self.head.item
            count = self.size()
            if count == 1 :
                self.head = None
            else :
                self.head.next.prev = self.head.prev
                self.head.prev.next = self.head.next
                self.head = self.head.next
            return data
    def deleteRear(self) :
        if self.isEmpty() == False :
            data = self.head.prev.item
            count = self.size()
            if count == 1 :
                self.head = None
            else :
                self.head.prev.prev.next = self.head
                self.head.prev = self.head.prev.prev
            return data
    def peekFront(self) :
        if self.isEmpty() == False :
            return self.head.item
    def peekRear(self) :
        if self.isEmpty() == False :
            return self.head.prev.item
    
    def size(self) :
        tmp = self.head
        count = 0
        if self.isEmpty() == False :
            while(1) :
                count += 1
                tmp = tmp.next
                if tmp == self.head :
                    break
        return count
    def print(self) :
        if self.isEmpty() == False :
            data = self.head
            while(1) :
                print(data.item, end = " ")
                data = data.next
                if data == self.head :
                    print("")
                    break
        else :
            print("")

    def revPrint(self) :
        if self.isEmpty() == False :
            data = self.head.prev
            while(1) :
                print(data.item, end = " ")
                data = data.prev
                if data == self.head.prev :
                    print("")
                    break
        else :
            print("")

def main() :
    dq = CircularDoublyLinkedList()
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

## 문제 3. 문제 2에서 구현한 원형 이중 연결 리스트를 사용하여 요세푸스 문제를 해결한다.
	
## 요세푸스 문제 (Josephus Problem)

## n 명의 사람 중에서 한 사람을 선택하려고 한다. 
## 선택 방법은 n 명의 사람이 삥 둘러 앉아 있을 때 임의의 숫자 k가 주어지면 매번 k번째 사람은 선택 후보 중에서 탈락을 시켜 최종 한 사람 남을 때까지 진행한다. 
## 마지막 남은 한 사람이 선택된다. 

## 예를 들면 n = 10 (번호는 1부터 10까지 가정), k = 3 일 때 다음과 같이 진행한다. 괄호는 탈락

## 1st round: 1, 2, (3), 4, 5, (6), 7, 8, (9), 10
## 2nd round: 1, (2), 4, 5, (7), 8, 10 
## 3rd round: (1), 4, 5, (8), 10
## 4th round: 4, (5), 10
## 5th round: 4, (10)

## 최종 선택은 4번째 사람이다.

## 요세푸스 문제는 j 프롬프트 추가하여 사용한다. j 다음의 숫자 k는 탈락시킬 k번째를 의미한다.

class DNode :
    def __init__(self, item, prev = None, next = None) :
        self.item = item
        self.prev = prev
        self.next = next

class CircularDoublyLinkedList :
    def __init__(self) :
        self.head = None
    def isEmpty(self) :
        return self.head == None
    def clear(self) :
        self.head = None
    def addFront(self, item) :
        node = DNode(item)
        if self.isEmpty() :
            self.head = node
            self.head.prev = node
            self.head.next = node
        else :
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev.next = node
            self.head.prev = node
            self.head = node

    def addRear(self, item) :
        node = DNode(item)
        if self.isEmpty() :
            self.head = node
            self.head.prev = node
            self.head.next = node
        else :
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev.next = node
            self.head.prev = node
    
    def deleteFront(self) :
        if self.isEmpty() == False :
            data = self.head.item
            count = self.size()
            if count == 1 :
                self.head = None
            else :
                self.head.next.prev = self.head.prev
                self.head.prev.next = self.head.next
                self.head = self.head.next
            return data
    def deleteRear(self) :
        if self.isEmpty() == False :
            data = self.head.prev.item
            count = self.size()
            if count == 1 :
                self.head = None
            else :
                self.head.prev.prev.next = self.head
                self.head.prev = self.head.prev.prev
            return data
    def peekFront(self) :
        if self.isEmpty() == False :
            return self.head.item
    def peekRear(self) :
        if self.isEmpty() == False :
            return self.head.prev.item
    
    def size(self) :
        tmp = self.head
        count = 0
        if self.isEmpty() == False :
            while(1) :
                count += 1
                tmp = tmp.next
                if tmp == self.head :
                    break
        return count
    def print(self) :
        if self.isEmpty() == False :
            data = self.head
            while(1) :
                print(data.item, end = " ")
                data = data.next
                if data == self.head :
                    print("")
                    break
        else :
            print("")

    def revPrint(self) :
        if self.isEmpty() == False :
            data = self.head.prev
            while(1) :
                print(data.item, end = " ")
                data = data.prev
                if data == self.head.prev :
                    print("")
                    break
        else :
            print("")

    def josephus(self, number) :
        if self.isEmpty() == False :
            data = self.head
            for i in range(number - 1) :
                data = data.next
            data.next.prev = data.prev
            data.prev.next = data.next
            for i in range(self.size()) :
                if self.size() == 1 :
                    break
                for i in range(number) :
                    data = data.next
                if data == self.head :
                    self.head = data.next
                    data.next.prev = data.prev
                    data.prev.next = data.next
                else :
                    data.next.prev = data.prev
                    data.prev.next = data.next
            return self.head.item

def main() :
    dq = CircularDoublyLinkedList()
    print("Enter a command : af(addFront), df(deleteFront), pf(peekFront), s(size)")
    print("ar(addRear), dr(deleteRear), pr(peekRear), rp(reversePrint)")
    print("j(josephus problem - enter kth number to be out : ), or q(uit)")

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
        elif command == 'j' :
            number = int(line[1])
            print(dq.josephus(number), "is alive")
        elif command == 'q' :
            break

main()
