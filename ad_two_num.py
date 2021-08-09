class Node:
    def __init__(self, x, next_node=None):
        self.val = x
        self.next = next_node


def print_list(u):
    value = []
    while u:
        value.append(u.val)
        u = u.next
    print(value)


def add_numbers(l1, l2):
    sum1 = l1.val + l2.val
    carry = int(sum1 / 10)

    l3 = Node(sum1 % 10)
    p1 = l1.next
    p2 = l2.next
    p3 = l3
    while p1 != None or p2 != None:
        sum1 = carry + (p1.val if p1 else 0) + (p2.val if p2 else 0)
        carry = int(sum1 / 10)
        p3.next = Node(sum1 % 10)
        p3 = p3.next
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None

    if carry > 0:
        p3.next = Node(carry)

    return l3

# input
a1 = Node(2, Node(4, Node(3)))
a2 = Node(5, Node(6, Node(4)))
a3 = add_numbers(a1, a2)
print_list(a3)
