class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        # 방법 0
        # arr = []
        # cur = self.head
        # while cur is not None:
        #     arr.append(cur)
        #     cur = cur.next
        
        # return arr[-k]

        # 방법 1
        # 1. 우선 모든 linkedList의 길이를 구한다
        # 2. linkedList의 길이에서 k만큼 빼고, 그만큼 이동한다.
        # 3. 그 노드를 반환한다.
        # length = 1
        # cur = self.head

        # while cur.next is not None:
        #     cur = cur.next
        #     length += 1
        
        # end_length = length - k
        # cur = self.head
        
        # for i in range(end_length):
        #     cur = cur.next
        
        # return cur
    
        # 방법 2
        # k만큼의 차이나는 위치에 2개의 노드 
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!