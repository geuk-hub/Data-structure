## 문제 1. 클래스를 사용하여 스택을 구현한다. 클래스 Stack을 구현하고 실행한 결과처럼 되도록 코딩한다. 
## 명령 프롬프트에서 m을 입력하면 파일 “input.txt”에 있는 문장을 한 라인씩 읽어 괄호 쌍을 검사한다.

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

## 문제 2. 문제 1에서 만든 클래스 Stack을 사용하여 십진수를 이진수로 변환하는 함수를 만들어 테스트한다. 십진수를 입력하면 이진수로 바꾸어 출력하되 -1을 입력하면 종료한다.
## 십진수를 이진수로 변환하는 방법은 다음과 같이 스택을 사용하여 변환한다. 
## 예를 들면 십진수 11을 이진수로 나타내면 1011이 된다. 
## 십진수 11을 2로 나눈 나머지 1을 스택에 저장하고 몫 5를 다시 2로 나누어 나머지 1을 스택에 저장하고 또 몫 2를 2로 나누어 나머지 0을 스택에 저장한다.
## 이 과정을 반복해서 2미만이 된 몫을 스택에 저장한 후 스택에 저장된 숫자를 pop하여 출력하면 원하는 이진수를 얻게 된다.

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

def check(number) :
    s = Stack()
    number2 = number
    while(1) :
        if number // 2 == 1 :
            if number % 2 == 1 or number % 2 == 0 :
                s.push(number%2)
            s.push(number//2)
            break
        if number % 2 == 1 or number % 2 == 0 :
            s.push(number%2)
            number = number // 2
    
    print("{0} ==> ".format(number2), end = "")
    for i in range(0, len(s.top)) :
        print(s.pop(), end="")
    print("")

def main() :
    while(1) :
        a = int(input("Enter a decimal number: "))
        if a == -1 :
            break
        check(a)
        
main()

## 문제 3. 주어진 파일(“maze.txt”)에 미로가 그려져 있다. 
## ‘1’은 통과 할 수 없는 블록을 나타내며 ‘0’은 통과 할 수 있는 통로를 나타낸다. ‘E’는 탈출할 수 있는 위치를 나타낸다. 첫 줄은 미로의 행과 열의 수를 나타낸다. 
## 입력 파일 (“input1.txt”)에 처음 시작 위치를 나타내는 행, 열이 주어져 있다. 첫 행과 첫 열은 1로 나타낸다 (교과서는 0로 나타냄). 
## 각 줄의 시작 위치에서 미로를 탈출할 수 있는지 판단한다.

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

def isValidPos(x,y) :
    if x < 0 or y < 0 or x >= MAZE_LENGTH or y >= MAZE_WIDTH :
        return False
    else :
        return map[x][y] == '0' or map[x][y] == 'E'

def DFS(index) :
    stack =Stack()
    stack.push(index)

    while not stack.isEmpty() :
        here = stack.pop()
        (x,y) = here
        if (map[x][y] == 'E') :
            break
        else : 
            map[x][y] = '.'
            if isValidPos(x, y - 1) :
                stack.push((x, y-1))
            if isValidPos(x, y + 1) :
                stack.push((x, y + 1))
            if isValidPos(x - 1, y) :
                stack.push((x - 1, y))
            if isValidPos(x + 1, y) :
                stack.push((x+1, y))
    if map[x][y] == 'E' :
        return True
    else :
        return False

inputfile = open('input1.txt', 'r')
start_location = inputfile.readlines()

for i in range(0, len(start_location)) :
    mazefile = open('maze.txt', 'r')
    mazefile = mazefile.readlines()
    map = []
    for j in range(1,len(mazefile)) :
        map.append(list(mazefile[j][:20]))
    
    maze_size = mazefile[0].split()
    MAZE_LENGTH = int(maze_size[0])
    MAZE_WIDTH = int(maze_size[1])
    
    index = start_location[i].split()
    index_2 = [0,0]
    index_2 = int(index[0]), int(index[1])
    index[0], index[1] = int(index[0])-1 , int(index[1])-1
    index = tuple(index)
    result = DFS(index)
    
    if result == False :
        print("{0} 에서 출발 ==>\tX, 실패".format(index_2))
    if result == True :
        print("{0} 에서 출발 ==>\t0, 성공".format(index_2))

