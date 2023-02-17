## 문제 1. 큐를 클래스 사용하여 원형 큐로 구현한다. 클래스 큐를 구현하고 실행한 결과와 같이 되도록 코딩한다. 
## 큐의 초기 크기는 3으로 하고(MAX_SIZE = 3) 큐가 가득 차면 큐의 크기를 2배로 늘려 데이터를 수용하도록 한다.

class CircularQueue :
    def __init__(self) :
        self.MAX_SIZE = 3
        self.items = [None] * self.MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0
    def isEmpty(self) :
        return self.count == 0
    def isFull(self) :
        return self.front == (self.rear+1) % self.MAX_SIZE
    def clear(self) :
        self.front = 0
        self.rear = 0
        self.count = 0
    def enqueue(self, item) :
        if self.isFull() :
            self.resize()
        if not self.isFull() :
            self.rear = (self.rear+1) % self.MAX_SIZE
            self.items[self.rear] = item
            self.count += 1
    def dequeue(self) :
        if not self.isEmpty() :
            self.front = (self.front+1) % self.MAX_SIZE
            print(self.items[self.front])
            self.count -= 1
    def resize(self) :
        newitems = [None] * 2 * self.MAX_SIZE
        scan = (self.front+1) % self.MAX_SIZE
        for i in range(self.count):
            newitems[i+1] = self.items[scan]
            scan = (scan+1) % self.MAX_SIZE
        self.items = newitems
        self.front = 0
        self.rear = self.count
        self.MAX_SIZE = self.MAX_SIZE * 2
    def peek(self) :
        if not self.isEmpty() :
            print(self.items[(self.front+1) % self.MAX_SIZE])
    def size(self) :
        print("size: %d"%(self.count))
    def print(self) :
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        elif self.front == self.rear :
            out = []
        else :
            out = self.items[self.front+1:self.MAX_SIZE] + self.items[0:self.rear+1]
        print(out)

print("Enter a command: e(nqueue), d(equeue), peek, s(size), p(rint), or q(uit)")
s = CircularQueue()
while(1) :
    data = list(input("> ").split())
    if data[0] == 'e' :
        s.enqueue(data[1])
    elif data[0] == 'p' :
        s.print()
    elif data[0] == 'd' :
        s.dequeue()
    elif data[0] == 's' :
        s.size()
    elif data[0] == 'peek' :
        s.peek()
    elif data[0] == 'q' :
        break

## 문제 2. 문제 1에서 만든 클래스 큐를 사용하여 입력 파일 “input.txt”에 있는 데이터를 문자열, 정수, 실수로 분류하여 3개의 큐를 만들어 저장한다. 
## 정수와 실수가 저장된 큐는 데이터 합을 구해 출력한다.

class CircularQueue :
    def __init__(self) :
        self.MAX_SIZE = 3
        self.items = [None] * self.MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0
    def isEmpty(self) :
        return self.count == 0
    def isFull(self) :
        return self.front == (self.rear+1) % self.MAX_SIZE
    def clear(self) :
        self.front = 0
        self.rear = 0
        self.count = 0
    def enqueue(self, item) :
        if self.isFull() :
            self.resize()
        if not self.isFull() :
            self.rear = (self.rear+1) % self.MAX_SIZE
            self.items[self.rear] = item
            self.count += 1
    def dequeue(self) :
        if not self.isEmpty() :
            self.front = (self.front+1) % self.MAX_SIZE
            print(self.items[self.front])
            self.count -= 1
    def resize(self) :
        newitems = [None] * 2 * self.MAX_SIZE
        scan = (self.front+1) % self.MAX_SIZE
        for i in range(self.count):
            newitems[i+1] = self.items[scan]
            scan = (scan+1) % self.MAX_SIZE
        self.items = newitems
        self.front = 0
        self.rear = self.count
        self.MAX_SIZE = self.MAX_SIZE * 2
    def peek(self) :
        if not self.isEmpty() :
            print(self.items[(self.front+1) % self.MAX_SIZE])
    def size(self) :
        print("size: %d"%(self.count))
    def print(self) :
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        elif self.front == self.rear :
            out = []
        else :
            out = self.item[self.front+1:self.MAX_SIZE] + self.items[0:self.rear+1]
        print(out)

infile = open("input.txt", "r")
infile = infile.readlines()
str_set = CircularQueue()
int_set = CircularQueue()
float_set = CircularQueue()

for i in infile[:] :
    for j in i.split() :
        try :
            int(j)
            int_set.enqueue(j)
        except :
            try :
                float(j)
                float_set.enqueue(j)
            except :
                str_set.enqueue(j)


print("String data: ", end = "")
str_set.print()
print("Integer data: ", end = "")
int_set.print()
print("Float data: ", end = "")
float_set.print()

sum1 = 0
for i in int_set.items[:] :
    try :
        sum1 += int(i)
    except : 
        pass
print("Sum of integer data: ", sum1)

sum2 = 0
for i in float_set.items[:] :
    try :
        sum2 += float(i)
    except :
        pass
print("Sum of float data: ", sum2)

## 문제 3. 문제 1에서 만든 원형 큐를 상속하여 덱을 구현한다. 클래스 덱을 구현하고 실행한 결과와 같이 되도록 코딩 한다. 
## 덱의 초기 크기는 3으로 하고(MAX_SIZE = 3) 덱이 가득 차면 덱의 크기를 2배로 늘려 데이터를 수용하도록 한다.

class CircularQueue :
    def __init__(self) :
        self.MAX_SIZE = 3
        self.items = [None] * self.MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0
    def isEmpty(self) :
        return self.count == 0
    def isFull(self) :
        return self.front == (self.rear+1) % self.MAX_SIZE
    def clear(self) :
        self.front = 0
        self.rear = 0
        self.count = 0
    def enqueue(self, item) :
        if self.isFull() :
            self.resize()
        if not self.isFull() :
            self.rear = (self.rear+1) % self.MAX_SIZE
            self.items[self.rear] = item
            self.count += 1
    def dequeue(self) :
        if not self.isEmpty() :
            self.front = (self.front+1) % self.MAX_SIZE
            print(self.items[self.front])
            self.count -= 1
    def resize(self) :
        newitems = [None] * 2 * self.MAX_SIZE
        scan = (self.front+1) % self.MAX_SIZE
        for i in range(self.count):
            newitems[i+1] = self.items[scan]
            scan = (scan+1) % self.MAX_SIZE
        self.items = newitems
        self.front = 0
        self.rear = self.count
        self.MAX_SIZE = self.MAX_SIZE * 2
    def peek(self) :
        if not self.isEmpty() :
            print(self.items[(self.front+1) % self.MAX_SIZE])
    def size(self) :
        print("size: %d"%(self.count))
    def print(self) :
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        elif self.front == self.rear :
            out = []
        else :
            out = self.items[self.front+1:self.MAX_SIZE] + self.items[0:self.rear+1]
        print(out)

class CircularDeque(CircularQueue) :
    def __init__(self) :
        super().__init__()
    def addRear(self, item) :
        self.enqueue(item)
    def deleteFront(self) :
        return self.dequeue()
    def getFront(self) :
        return self.peek()
    def addFront(self, item) :
        if self.isFull() :
            self.resize()
        if not self.isFull() :
            self.items[self.front] = item
            self.front = self.front - 1
            self.count += 1
            if self.front < 0 :
                self.front = self.MAX_SIZE - 1
    def deleteRear(self) :
        if not self.isEmpty() :
            item = self.items[self.rear]
            self.rear = self.rear - 1
            self.count -= 1
            if self.rear < 0 :
                self.rear = self.MAX_SIZE - 1
            print(item)
    def getRear(self) :
        print(self.items[self.rear])

print("Enter a command: af(addFront), df(deleteFront), gf(getFront), s(ize)")
print("ar(addRear), dr(deleteRear), gr(getRear), p(rint) or q(uit)")
s = CircularDeque()
while(1) :
    data = list(input("> ").split())
    if data[0] == "ar" :
        s.addRear(data[1])
    if data[0] == "af" :
        s.addFront(data[1])
    if data[0] == "p" :
        s.print()
    if data[0] == "s" :
        s.size()
    if data[0] == "gf" :
        s.getFront()
    if data[0] == "gr" :
        s.getRear()
    if data[0] == "dr" :
        s.deleteRear()
    if data[0] == "df" :
        s.deleteFront()
    if data[0] == "q" :
        break

## 문제 4. Palindrome(회문)은 앞뒤 어느 쪽을 읽어도 같은 단어, 문장을 의미한다. 예를 들어 “level”, “2002”는 palindrome이다. 
## 파일 “input1.txt”에 있는 문장을 읽어 palindrome인지 아닌지 판단하는 프로그램을 작성한다. 
## Palindrome을 판단하는 방법은 여러가지 있으나 여기서는 한 줄의 각 문자를 덱에 저장한 후, 덱의 양쪽 끝에서 데이터의 중간까지 삭제하여 비교하는 방법을 사용한다. 
## 덱은 문제 3에서 만든 것을 사용한다. 문장 중에 알파벳 문자는 대/소문자 구분하지 않고 검사한다.

class CircularQueue :
    def __init__(self) :
        self.MAX_SIZE = 3
        self.items = [None] * self.MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0
    def isEmpty(self) :
        return self.count == 0
    def isFull(self) :
        return self.front == (self.rear+1) % self.MAX_SIZE
    def clear(self) :
        self.front = 0
        self.rear = 0
        self.count = 0
    def enqueue(self, item) :
        if self.isFull() :
            self.resize()
        if not self.isFull() :
            self.rear = (self.rear+1) % self.MAX_SIZE
            self.items[self.rear] = item
            self.count += 1
    def dequeue(self) :
        if not self.isEmpty() :
            self.items = self.items[self.front : ]
            self.count -= 1
            self.rear -= 1
            
    def resize(self) :
        newitems = [None] * 2 * self.MAX_SIZE
        scan = (self.front+1) % self.MAX_SIZE
        for i in range(self.count):
            newitems[i+1] = self.items[scan]
            scan = (scan+1) % self.MAX_SIZE
        self.items = newitems
        self.front = 0
        self.rear = self.count
        self.MAX_SIZE = self.MAX_SIZE * 2

    def peek(self) :
        if not self.isEmpty() :
            return self.items[(self.front-1) % self.MAX_SIZE]
    def size(self) :
        return self.count
    def print(self) :
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        elif self.front == self.rear :
            out = []
        else :
            out = self.items[self.front+1:self.MAX_SIZE] + self.items[0:self.rear+1]
        print(out)

class CircularDeque(CircularQueue) :
    def __init__(self) :
        super().__init__()
    def addRear(self, item) :
        self.enqueue(item)
    def deleteFront(self) :
        self.dequeue()
    def getFront(self) :
        return self.peek()
    def addFront(self, item) :
        if self.isFull() :
            self.resize()
        if not self.isFull() :
            self.items[self.front] = item
            self.front = self.front - 1
            self.count += 1
            if self.front < 0 :
                self.front = self.MAX_SIZE - 1
    def deleteRear(self) :
        if not self.isEmpty() :
            self.items = self.items[self.front-1 : self.rear]
            self.rear = self.rear - 1
            self.count -= 1
            if self.rear < 0 :
                self.rear = self.MAX_SIZE - 1
    def getRear(self) :
        return self.items[self.rear]

infile = open('input1.txt')
infile = infile.readlines()

for i in infile[:] :
    s = CircularDeque()
    q = CircularDeque()    
    for j in i[:-1] :
        q.enqueue(j)
    for j in i[:-1] :       
        s.enqueue(j.lower())
    s.items.pop(0)
    s.front += 1
    s.rear -= 1
    a = ""
    for i in q.items :
        if i == None :
            continue
        a += str(i)
    while(1) :
        if s.getFront() == s.getRear() :
            s.deleteFront()
            s.deleteRear()
            if s.size() == 1 or s.size() == 0 :
                print(a)
                print(" ==> palindrome")
                break
        elif s.getFront() != s.getRear() :
            print(a)
            print(" ==> not palindrome")
            break


