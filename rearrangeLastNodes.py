'''Note: Try to solve this task in O(list size) time using O(1) additional space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, move the last n list nodes to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
solution(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
solution(l, n) = [7, 1, 2, 3, 4, 5, 6].'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, n):
    if l is None or n<=0:
        return l
    cur, tail , len = l , None, 0
    while cur is not None:
        tail = cur
        cur, len = cur.next, len+1
    acc , mark, cur = 0,len-n-1, l
    if n>=len:
        return l
    while acc<mark:
        cur, acc = cur.next, acc+1        
    tail.next= l
    new_head = cur.next
    cur.next = None
    return new_head    
             

           
        
        

