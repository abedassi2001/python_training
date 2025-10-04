class Node : 
    def __init__(self, data): 
        self.data = data  
        self.next = None

def insert(head, data): 
    new_node = Node(data) 
    if head is None: 
        return new_node 
    new_node.next = head
    return new_node

def append(head, data): 
    new_node = Node(data) 
    if head is None: 
        return new_node 
    last = head 
    while last.next: 
        last = last.next 
    last.next = new_node 
    return head
def isempty(head):
    return head is None
def length(head):
    count = 0 
    iter = head 
    while iter: 
        count += 1 
        iter = iter.next
    return count        

head = Node(1)
head = insert(head, 2)
head = insert(head, 3)

iter = head
while iter:
    print(iter.data)
    iter = iter.next
print(length(head))
    

    