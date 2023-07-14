#class to create a node
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		temp = head
		before = None
		while temp:
			after = head.next
			head.next = before
			before = head
			head = after
		return before
