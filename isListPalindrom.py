'''Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

Example

For l = [0, 1, 0], the output should be
solution(l) = true;

For l = [1, 2, 2, 3], the output should be
solution(l) = false.'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l):
    return isPalindrom(l ,l)[0]
def isPalindrom(cur , head):
    if cur is None:
        return True, head
    isPalin , head = isPalindrom(cur.next,head)
    if not isPalin:
        return False, head
    if cur.value != head.value:
        return False, head
    head = head.next
    return True, head    
                    

