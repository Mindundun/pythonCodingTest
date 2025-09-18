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

    def get_node(self, index):
        cur = self.head
        cur_index = 0 

        while index != cur_index :
            cur = cur.next
            cur_index = cur_index + 1
        
        return cur
    # N 번째 인덱스에 M 값을 넣은 후 연결하는 함수
    def add_node(self, index, value):
        new_node = Node(value)
        # 인덱스가 0인 경우 예외처리
        if index == 0 :
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.get_node(index - 1) # 0 일때는 , , ? 
        # 기존에 연결된 노드
        next_node = prev_node.next

        prev_node.next = new_node
        new_node.next = next_node        

    # N 번째 인덱스의 노드를 삭제
    def delete_node(self, index):
        # 인덱스가 0인 경우 예외처리
        if index == 0 :
            self.head = self.head.next
            return
        
        prev_node = self.get_node(index - 1)
        next_node = self.get_node(index + 1)

        prev_node.next = next_node

linked_list = LinkedList(5)
#print(linked_list.head.data)
# 현재상태
# head
# [5] -> [3] -> [7] -> [6] -> [8]


# 원하는 상태
# head
#                                    new
# [5] -> [3] -> [7] -> [6] -> [8] -> [9]

linked_list.append(7)
linked_list.append(6)
# [5] -> [7] -> [6]

linked_list.printAll()
print("--------------------------------")
print(linked_list.get_node(1).data)
# =================================================
#현재상태
# [5] -> [7] -> [6]

# 원하는 상태
# [5] -> [3] -> [7] -> [6] 

print("--------------------------------")
linked_list.add_node(1, 3)
linked_list.printAll()
print("--------------------------------")

linked_list.add_node(0, 7) # 0번째에 7번 노드 추가
linked_list.printAll()
print("--------------------------------")
linked_list.delete_node(0) # 0번째의 노드 삭제
linked_list.printAll()