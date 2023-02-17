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