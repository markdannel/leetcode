class LinkedList(object):
    def __init__(self, x):
        self.val = x
        self.next= None

def reverse(node):
    p = node
    cur = node.next
    p.next = None
    while cur:
        temp = cur.next
        cur.next = p
        p = cur
        cur = temp
    return p