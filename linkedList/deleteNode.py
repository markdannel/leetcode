class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# make cycle linked list
arr = [1,2,3,4]
head = ListNode(arr[0])
i = 1
l = len(arr)
node = head
while i < l:
    node1 = ListNode(arr[i])
    node.next = node1
    node = node.next
    i += 1
node.next = head

i = 0
while i < l+1:
    print(node, id(node))
    node = node.next
    i += 1

if head == None or head.next == None:
    #return False
    pass
count = 0
node1 = head
node2 = head
while node1:
    count += 1
    node1 = node1.next
    node2 = node2.next.next
    if id(node1) == id(node2):
        #return True
        print("2:",node,id(node),id(head))
        break
#return False
print("count", count)