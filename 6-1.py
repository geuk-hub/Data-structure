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