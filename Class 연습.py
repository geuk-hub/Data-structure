## 문제 1. 가방속 물건과 물건 갯수, 지갑 유무, 손수건 유무를 알 수 있는 Bag 클래스를 구현하라.

class Bag:
    def __init__(self):
        self.items = []
    def contains(self, e):
        return e in self.items
    def insert(self, e):
        self.items.append(e)
    def remove(self, e):
        self.items.remove(e)
    def count(self):
        return len(self.items)
    def __str__(self):
        return "%s"%(self.items)

myBag = Bag()
myBag.insert("휴대폰")
myBag.insert("지갑")
myBag.insert("손수건")
myBag.insert('빗')
myBag.insert('연필')
print("가방속 물건: ", myBag)

myBag.insert('빗')
myBag.remove('손수건')
myBag.insert('자료 구조 책')
print("가방속 물건: ", myBag)
print("가방속 물건 갯수: %d" %myBag.count())
print("가방속 지갑 유무: %s" %myBag.contains('지갑'))
print("가방속 손수건 유무: %s" %myBag.contains('손수건'))

## 문제 2. 파일 "input.txt"에 있는 년, 월, 일로 주어진 날짜를 읽어 출력하고 가장 오래된 날짜와 가장 늦은 날짜를 출력하도록 한다.

class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def __gt__(self, rhs):
        return (self.year,self.month,self.day)>(rhs.year,rhs.month,rhs.day)
    def __lt__(self, rhs):
        return (self.year, self.month, self.day) < (rhs.year, rhs.month, rhs.day)
    def __str__(self):
        return "%d/%d/%d"%(self.year,self.month,self.day)

def findMinMax(lst):
    min=lst[0]
    max=lst[0]
    for i in range(1,len(lst)):
        if max<lst[i]:max=lst[i]
        if min>lst[i]: min = lst[i]
    return min,max

def main():
    inFile = open("input.txt",'r')
    lst=[]
    while True:
        line=inFile.readline()
        if line=="":
            break
        date=[int(i) for i in line.split()]
        lst.append(Date(date[0],date[1],date[2]))
    for i in range(len(lst)):
        print(lst[i])
    min,max=findMinMax(lst)
    print()
    print("earlist date:",min)
    print("latest data:",max)
    inFile.close()

main()

## 문제 3. 파일 "input2.txt"에는 한 줄에 기준 날짜와 날짜 수가 주어진다. 기준 날짜에 날짜 수만큼 진행한 후의 날짜를 출력한다.

class Date:
    def __init__(self,year,month,day,increase):
        self.year=year
        self.month=month
        self.day=day
        self.increase=increase

    def lastDayOfTheMonth(self):
        if self.month == 2:
            if (self.year % 4 == 0 and self.year % 100 != 0) or self.year%400 == 0:
                return 29
            else:
                return 28
        elif self.month == 4 or self.month ==6 or self.month ==9 or self.month ==11:
            return 30
        else:
            return 31

    def increment(self):
        if self.day == self.lastDayOfTheMonth():
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1
        return self

    def __str__(self):
        return "%d/%d/%d"%(self.year,self.month,self.day)



def main():
    inFile=open("input2.txt",'r')
    lst=[]
    num=0
    while True:
        line=inFile.readline()
        if line=="":
            break
        date=[int(i) for i in line.split()]
        lst.append(Date(date[0],date[1],date[2],date[3]))
        print("%d/%d/%d\t%5d일 후 ==>\t"%(date[0],date[1],date[2],date[3]),end="")
        for i in range(date[3]):
            Date.increment(lst[num])
        print(lst[num])
        num+=1
    inFile.close()

main()

## 문제 4. 파일 "input3.txt"에는 한 줄에 기준 날짜 두 개가 주어진다. 첫 번째 주어진 날짜에서 두 번째 날짜까지 경과한 날짜 수를 계산하여 출력한다.

class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    def lastDayOfTheMonth(self):
        if self.month == 2:
            if self.year % 4 == 0 and self.year % 100 != 0 or self.year%400 == 0:
                return 29
            else:
                return 28
        elif self.month == 4 or self.month ==6 or self.month ==9 or self.month ==11:
            return 30
        else:
            return 31

    def increment(self):
        if self.day == self.lastDayOfTheMonth():
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        else:
            self.day += 1
        return self

    def __str__(self):
        return "%d/%d/%d"%(self.year,self.month,self.day)

    def __eq__(self, other):
        return self.year==other.year and self.month==other.month and self.day==other.day


def main():
    inFile=open("input3.txt",'r')
    lst=[]
    lst2=[]
    num=0
    while True:
        line=inFile.readline()
        if line=="":
            break

        date=[int(i) for i in line.split()]
        lst.append(Date(date[0],date[1],date[2]))
        lst2.append(Date(date[3],date[4],date[5]))
        print("%d/%d/%d "%(date[0],date[1],date[2]),end="")
        print("\t%d/%d/%d\t==>"%(date[3], date[4], date[5]),end="")

        lstlen=0
        lst2len=0

        day=0
        for i in range(0, 3):
            lstlen += date[i]

        for i in range(3, 6):
            lst2len += date[i]

        while lst[num]!=lst2[num]:
            if lstlen<lst2len:
                Date.increment(lst[num])
                day += 1
            else:
                Date.increment(lst2[num])
                day-=1
        print("%9d일 경과"%day)



        num+=1


    inFile.close()

main()

## 문제 5. 하노이 탑을 구현한다. 원판의 수를 입력받아 0이 될 때까지 진행하며 원판의 이동과 이동 횟수를 출력한다.

def hanoi(n,fr,tmp,to) :
    if (n==1) :
        print("원판 1 : %s --> %s" %(fr, to))    
    else : 
        hanoi(n-1, fr, to, tmp)
        print("원판 %d : %s --> %s" %(n,fr,to))
        hanoi(n-1, tmp, fr, to)

while(1) :
    a = int(input("원판의 수를 입력하세요 :"))
    if a == 0 :
        break
    sum = (2**a)-1
    hanoi(a, 'A','B','C')
    print("\n이동 횟수 :",sum)
    print("")
