'''Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
solution(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
solution(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l1, l2):
    temp = ListNode(None)

    if l1 is None:
        return l2
    if l2 is None:
        return l1    
    if l1.value <= l2.value:
        temp = l1
        temp.next = solution(l1.next, l2)
    else:
        temp = l2
        temp.next = solution(l1, l2.next)
    return temp
