class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(5)
print(node.data , node.next)

next_node = Node(5)
node.next = next_node
# [5] -> [3]
#print(node.data , node.next)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # 링크드 리스트에 가장 끝에 있는 노드에 새로운 노드를 연결해줘
    def append(self, value):
        cur = self.head

        while cur.next is not None :
            cur = cur.next
        
        cur.next = Node(value)

    # 링크드 리스트에서 저장한 head를 따라가면서 현재 있는 노드들을 전부 출력해주는 함수
    def printAll(self):
        cur = self.head

        while cur is not None :
            print(cur.data)
            cur = cur.next
        

linked_list = LinkedList(5)
#print(linked_list.head.data)

linked_list.append(12)
linked_list.append(8)

linked_list.printAll()
# 현재상태
# head
# [5] -> [3] -> [7] -> [6] -> [8]


# 원하는 상태
# head
#                                    new
# [5] -> [3] -> [7] -> [6] -> [8] -> [9]