# Реверсування однозв'язного списку

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

#Сортування однозв'язного списку
def merge_sort(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def sorted_merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, left.next)

    return result

# Об'єднання двох відсортованих однозв'язних списків

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next

# Створюємо список і додаємо елементи
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third

# Реверсуємо список
llist.reverse()

# Виведемо елементи списку після реверсу
current = llist.head
while current:
    print(current.data)
    current = current.next

# Сортування однозв'язного списку

# Створюємо новий список і додаємо елементи
llist = LinkedList()
llist.head = Node(3)
second = Node(1)
third = Node(2)
llist.head.next = second
second.next = third

# Сортуємо список
sorted_head = merge_sort(llist.head)

# Виведемо елементи після сортування
current = sorted_head
while current:
    print(current.data)
    current = current.next

# Створюємо перший відсортований список
list1 = LinkedList()
list1.head = Node(1)
list1.head.next = Node(3)
list1.head.next.next = Node(5)

# Створюємо другий відсортований список
list2 = LinkedList()
list2.head = Node(2)
list2.head.next = Node(4)
list2.head.next.next = Node(6)

# Об'єднуємо списки
merged_head = merge_sorted_lists(list1.head, list2.head)

# Виведемо елементи після об'єднання
current = merged_head
while current:
    print(current.data)
    current = current.next