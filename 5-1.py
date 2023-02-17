class Stack : 
    def __init__(self) :
        self.top = []
    def isEmpty(self) :
        return len(self.top) == 0
    def size(self) :
        return len(self.top)
    def clear(self) :
        self.top = []
    def push(self, item):
        self.top.append(item)
    def pop(self) :
        if not self.isEmpty() :
            return self.top.pop(-1)
    def peek(self) :
        if not self.isEmpty() :
            return self.top[-1]
    def __str__(self) :
        return str(self.top[::-1])
    
def checkBrackets(statement) :
    stack = Stack()
    for ch in statement :
        if ch in ('{[(') :
            stack.push(ch)
        elif ch in ('}])') :
            if stack.isEmpty() :
                return False
            else : 
                left = stack.pop()
                if (ch == '}' and left != '{') or (ch == ']' and left != '[') or (ch == ')' and left != '(') :
                    return False
    return stack.isEmpty()
    
def main() :
    infile = open('input.txt','r')
    infile = infile.readlines()
    print("Enter a command: pop, push, peek, size, empty, p(rint), m(atch), q(uit)")
    s = Stack()
    while(1) :
        data = list(input("> ").split())
        if data[0] == 'push' :
            s.push(data[1])
        if data[0] == 'p' :
            print(s)
        if data[0] == 'peek' :
            print(s.peek())
        if data[0] == 'pop' :
            print(s.pop())
        if data[0] == 'size' :
            print(s.size())
        if data[0] == 'empty' :
            print(s.isEmpty())
        if data[0] == 'm' :
            for i in infile[:] :
                print(i, end="")
                if checkBrackets(i) == True :
                    print("matched")
                else :
                    print("not matched")
        if data[0] == 'q' :
            break

main()