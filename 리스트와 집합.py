## 문제 1. 클래스를 사용하여 리스트를 구현한다.
## > a 22 (add 멤버 함수에 해당) => ‘33’ 데이터를 리스트의 맨 끝에 삽입한다. 
## > remove 33 => ‘33’ 데이터를 리스트에서 삭제한다. ‘33’ 데이터가 없으면 없다는 메시지 보낸다.
## > search 33 => ‘33’ 데이터를 리스트에서 탐색한다. ‘33’ 데이터가 없으면 없다는 메시지 보낸다.
## > m 2 3 4 8 1 9 => m은 merge(합병)를 의미하며 m 다음의 임의의 데이터는 리스트로 받아들여 합병한다.
## > dup => 중복된 요소를 제거한다.

class ArrayList :
    def __init__(self) :
        self.items = []
    def add(self, elem) :
        self.items.append(elem)
    def remove(self, elem) :
        if self.items.count(elem) == 0 :
            print("No such element")
        else : 
            self.items.remove(elem)
            print(elem, "removed")
    def insert(self, pos, elem) :
        self.items.insert(int(pos), elem)
    def delete(self, pos) :
        self.items.pop(pos)
    def isEmpty(self) :
        if len(self.items) == 0 :
            print("True")
        else :
            print("False")
    def getEntry(self, pos) :
        print(self.items[int(pos)])
    def size(self) :
        return len(self.items)
    def clear(self) :
        self.items = []
    def find(self, item) :
        return self.items.index(item)
    def replace(self, pos, elem) :
        self.items[int(pos)] = elem
    def sort(self) :
        self.items.sort()
    def print(self, msg = "ArrayList") :
        print(msg, self.size(), self.items)
        print("")
    def search(self,elem):
        check = elem
        while True :
            if check in self.items:
                print(check, "found")
                break
            else:
                print("No such element")
                break
    def dup(self):
        a = []
        for i in self.items :
            if i not in a :
                a.append(i)
        self.items = a
    def merge(self, lst) :
        self.items.extend(lst)

s=ArrayList()
print("Enter a command:i(nsert),d(elete),e(mpty),g(etEntry),c(lear),a(dd),dup,remove,search,f(ind),r(eplace),s(ort),m(erge),p(rint):")
while(1):
    data=list(input("> ").split())
    if data[0]=='i' :
        s.insert(data[1],data[2])
    if data[0]=='d' :
        s.delete(data[1])
    if data[0]=='e' :
        s.isEmpty()
    if data[0]=='g' :
        s.getEntry(data[1])
    if data[0]=='c' :
        s.clear()
    if data[0]=='a' :
        s.add(data[1])
    if data[0]=='dup' :
        s.dup()
    if data[0]=='remove':
        s.remove(data[1])
    if data[0]=='search':
        s.search(data[1])
    if data[0]=='f':
        s.find(data[1])
    if data[0]=='r':
        s.replace(data[1],data[2])
    if data[0]=='s':
        s.sort()
    if data[0]=='m':
        s.merge(data[1:])
    if data[0]=='p':
        s.print()
    if data[0]=='q':
        break

## 문제 2. 파일 “input.txt”을 읽어 라인 번호와 함께 화면에 출력한다. 문제 1에서 만든 클래스 ArrayList를 사용하며 다음과 같은 명령어를 실행하도록 한다.
## > i 16
## 그에게로 가서 나도
## 그의 꽃이 되고 싶다.
## *
## => i 16은 라인 번호 16에 그 다음의 문장을 ‘*’를 만난 때까지 한 줄 한 줄 삽입되도록 한다.
## > d 14 15 => 라인 번호 14에서 15까지의 문장을 삭제한다. ‘> d 14 14’이면 라인 번호 14만 삭제한다.
## > r 19
## 잊혀지지 않는 하나의 의미가 되고 싶다.
## =>라인 번호 19에 다음에 있는 문장으로 대체한다.

class ArrayList:
    def __init__(self):
        self.items= []
    def insert(self, pos, msg):
        self.items.insert(int(pos), msg+"\n")
    def delete(self,pos, elem):
        for i in range(elem-1,pos-2, -1) :
            self.items.pop(i) 
    def replace(self,pos,msg):
        for i in msg :
            self.items[pos-1] = i
    def print(self):
        count = 1
        for i in self.items[:] :
            print("{0}> {1}".format(count, i), end ="")
            count += 1
        print("")

def main() :
    inFile = open("input.txt","r")
    line = inFile.readlines()
    count = 1
    for i in line[:] :
        print("{0}> {1}".format(count, i), end = "")
        count += 1
    print("")
    s = ArrayList()
    s.items = line
    print("")
    while True:
        data=list(input("> ").split())
        if data[0]=='i' :
            a = []
            while (1):
                b = input()
                if b == '*' :
                    break
                a.append(b)
            a.reverse()
            for i in a[:] :
                s.insert(int(data[1])-1, i)
        if data[0]=='d' :
            s.delete(int(data[1]), int(data[2]))
        if data[0]=='p' :
            s.print()
        if data[0]=='r' :
            c = []
            d = input()
            c.append(d)
            s.replace(int(data[1]),c)
        if data[0]=='q' :
            break
    
main()

## 문제 3. 클래스를 사용하여 집합을 구현한다. 교과서에 주어진 멤버 함수 외에 다음과 같은 새로운 멤버 함수를 사용하여 실행한다. 
## __eq__(): 두 개의 집합이 같은지 판단, 이것을 구현하면 두 집합 사이에 ‘==’ 연산자 사용하여 같은지 판단할 수 있다.
## isSubstring(): 부분 집합 (subset) 여부 판단
## isProperSubstring(): 진부분 집합(proper subset) 여부 판단
## 필요하면 멤버 함수와 일반 함수 추가하여 사용한다. 

class Set:
    def __init__(self) :
        self.items=[]
    def __eq__(self, setB) :
        return self.items == setB.items
    def insert(self,elem) :
        if elem not in self.items :
            self.items.append(elem)
    def delete(self,elem) :
        if elem in self.items :
            self.items.remove(elem)
    def union(self,setB) : 
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items :
            if elem not in self.items :
                setC.items.append(elem)
        return setC.items
    def intersect(self,setB) :
        setC = Set()
        for elem in setB.items :
            if elem in self.items :
                setC.items.append(elem)
        return setC.items
    def difference(self,setB) :
        setC = Set()
        for elem in self.items :
            if elem not in setB.items :
                setC.items.append(elem)
        return setC.items
    def isSubset(self, setB) :
        return set(self.items).issubset(set(setB.items))
    def isProperSubset(self, setB) :
        return set(self.items) < set(setB.items)
    def size(self) :
        return len(self.items)
    def print(self,msg) :
        print(msg)

def test(setA, setB) :
    print("SetA: ", setA.items)
    print("SetB: ", setB.items)
    if setA == setB :
        print("A equal B: True")
    else :
        print("A equal B: False")
    print("A subset B: ", setA.isSubset(setB))
    print("A proper subset B: ", setA.isProperSubset(setB))
    print("A union B: ",setA.union(setB))
    print("A intersect B: ", setA.intersect(setB))
    print("A difference B: ", setA.difference(setB))
    print("")

def main() :
    setA = Set()
    setA.insert(2)
    setA.insert(3)
    setA.insert(4)
    
    setB = Set()
    setB.insert(2)
    setB.insert(3)
    setB.insert(4)

    setC = Set()
    setC.insert(2)
    setC.insert(3)
    setC.insert(4)
    setC.delete(4)

    test(setA, setB)
    test(setA, setC)
    test(setC, setA)

main()
