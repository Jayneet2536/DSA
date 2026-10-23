# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head 

        while curr is not None:
            next_node = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next_node
        
        return prev 

    def isPalindrome(self, head):
        if head is None and head.next is None:
            return True 

        slow = head 
        fast = head 

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next 
            fast = fast.next.next 

        newHead = self.reverseList(slow.next)

        first = head 
        second = newHead 

        while second is not None:
            if first.val != second.val:
                self.reverseList(newHead)
                return False 
            
            first = first.next 
            second = second.next 

        self.reverseList(newHead) 

        return True
        