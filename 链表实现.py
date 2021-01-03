# 创建一个链表
class Node:  # 定义一个节点类
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):  # 设置节点的下一个地址
        self.next = newnext

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

class LinkList:
    def __init__(self):
        self.head = Node()  # 嵌套类
        self.length = 0

    def tail_add(self, newdata):
        newnode = Node(newdata, None)
        if self.length == 0:  # 判断是否为空链表
            self.head = newnode  # 新增节点为该空链表链表的头结点，链表不再为空
            self.length = 1
        else:
            currentNode = self.head
            while currentNode.getNext() != None:
                currentNode = currentNode.getNext()
            currentNode.setNext(newnode)  # 目前最后一个节点的下一个地址为新增加的节点
            self.length += 1
    def printLinklist(self):
        currentNode = self.head
        while currentNode != None:
            print('打印节点: %s' % (currentNode.getData()))
            currentNode = currentNode.getNext()

    def getlength(self):
        return self.length


# =================================== 调用链表类实例，打印结果
foods = ['apple', 'water', 'juice', 'tomato']
newlinklist = LinkList()
for s in foods:
    newlinklist.tail_add(s)
print(newlinklist.getlength())
newlinklist.printLinklist()










