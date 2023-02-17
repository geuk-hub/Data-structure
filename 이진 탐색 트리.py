## 문제 1. 순환적인 방법으로 이진 탐색 트리를 구현하여 삽입/탐색/삭제/출력을 테스트 한다.

class BSTNode :
    def __init__(self, item, left = None, right = None) :
        self.item = item
        self.left = left
        self.right = right

class BSTree :
    def __init__(self) :
        self.root = None
        self.insertSuccess = None
        self.deleteSuccess = None

    def insert(self, data) :
        self.root = self.insert1(self.root, data)
        return self.insertSuccess
    def insert1(self, node, data) :
        if node == None :
            node = BSTNode(data)
            self.insertSuccess = True
        elif data > node.item :
            node.right = self.insert1(node.right, data)
        elif data < node.item :
            node.left = self.insert1(node.left, data)
        return node

    def search(self, data) :
        return self.search1(self.root, data)
    def search1(self, node, data) :
        if node == None :
            return False
        elif data > node.item :
            return self.search1(node.right, data)
        elif data < node.item :
            return self.search1(node.left, data)
        else :
            return True

    def delete(self, data) :
        self.root = self.delete1(self.root, data)
        return self.deleteSuccess
    def delete1(self, node, data) :
        if node == None :
            self.deleteSuccess = False
        elif data > node.item :
            node.right = self.delete1(node.right, data)
        elif data < node.item :
            node.left = self.delete1(node.left, data)
        else :
            self.deleteSuccess = True
            if node.right == None :
                node = node.left
            elif node.left == None :
                node = node.right
            else :
                maxNode = node.left
                while maxNode.right != None :
                    maxNode = maxNode.right
                node.item = maxNode.item
                node.left = self.delete1(node.left, maxNode.item)
        return node

    def print(self) :
        self.print1(self.root, 0)
    def print1(self, node, skip) :
        if node != None :
            self.print1(node.right, skip + 10)
            for i in range(skip) :
                print(" ", end = "")
            print(node.item, end = "")
            if node.left != None :
                print(",L", end = "")
            if node.right != None :
                print(",R", end = "")
            print()
            self.print1(node.left, skip + 10)

def main() :
    t = BSTree()
    print("Enter a command : i(nsert), s(earch), d(elete), p(rint) or q(uit)")
    while True :
        print("> ", end = "")
        line = input().split()
        command = line[0]
        if command == 'i' :
            item = int(line[1])
            if t.insert(item) :
                print(item, "is inserted")
            else :
                print("Not inserted : same data")
        elif command == 's' :
            item = int(line[1])
            if t.search(item) :
                print(item, "is found")
            else :
                print("No such item in the tree")
        elif command == 'd' :
            item = int(line[1])
            if t.delete(item) :
                print(item, "is deleted")
            else :
                print("No such item in the tree")
        elif command == 'p' :
            t.print()
        elif command == 'q' :
            break
    
main()

## 문제 2. 반복적인 방법으로 이진 탐색 트리를 구현하여 삽입/탐색/삭제/출력을 테스트 한다.

class BSTNode :
    def __init__(self, item, left = None, right = None) :
        self.item = item
        self.left = left
        self.right = right

class BSTree :
    def __init__(self) :
        self.root = None

    def insert(self, data) :
        curr = self.root
        if curr == None :
            self.root = BSTNode(data)
            return True
        while curr != None :
            if data > curr.item :
                if curr.right == None :
                    curr.right = BSTNode(data)
                    return True
                curr = curr.right
            elif data < curr.item :
                if curr.left == None :
                    curr.left = BSTNode(data)
                    return True
                curr = curr.left
            elif data == curr.item :
                return False
        
    def search(self, data) :
        curr = self.root
        while curr != None :
            if data < curr.item :
                curr = curr.left
            elif data > curr.item :
                curr = curr.right
            else :
                return True
        return False
        
    def delete(self, data) :
        parent = None
        curr = self.root
        while curr != None :
            if data < curr.item :
                parent = curr
                curr = curr.left
            elif data > curr.item :
                parent = curr
                curr = curr.right
            else :
                break
        if curr == None :
            return False
        if curr.left == None :
            if parent == None :
                self.root = curr.right
            else :
                if data < parent.item :
                    parent.left = curr.right
                else :
                    parent.right = curr.right
        elif curr.right == None :
            if parent == None :
                self.root = curr.left
            else :
                if data < parent.item :
                    parent.left = curr.left
                else :
                    parent.right = curr.left
        else :
            parentMaxNode = curr
            maxNode = curr.left
            while maxNode.right != None :
                parentMaxNode = maxNode
                maxNode = maxNode.right
            curr.item = maxNode.item
            if parentMaxNode.right == maxNode :
                parentMaxNode.right = maxNode.left
            else :
                parentMaxNode.left = maxNode.left
        return True
    
    def print(self):
        curr = self.root
        stack = []
        number = -1
        while True :
            while curr != None:
                stack.append(curr)
                curr = curr.right
                number += 1
            if len(stack) == 0 :
                break
            curr = stack.pop()
            if curr == self.root :
                number = 0
            if curr == None :
                break
            for i in range(number) :
                print(" "*10, end = "")
            
            print(curr.item, end = "")
            if curr.left != None :
                number += 1
                print(",L", end = "")
            if curr.right != None :
                print(",R", end = "")

            print()
            curr = curr.left
            number -= 1

def main() :
    t = BSTree()
    print("Enter a command : i(nsert), s(earch), d(elete), p(rint) or q(uit)")
    while True :
        print("> ", end = "")
        line = input().split()
        command = line[0]
        if command == 'i' :
            item = int(line[1])
            if t.insert(item) :
                print(item, "is inserted")
            else :
                print("Not inserted : same data")
        elif command == 's' :
            item = int(line[1])
            if t.search(item) :
                print(item, "is found")
            else :
                print("No such item in the tree")
        elif command == 'd' :
            item = int(line[1])
            if t.delete(item) :
                print(item, "is deleted")
            else :
                print("No such item in the tree")
        elif command == 'p' :
            t.print()
        elif command == 'q' :
            break
    
main()
