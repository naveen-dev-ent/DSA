class ListNode:
	def __init__(self, data):
		self.data = data
		self.next = None

class Solution:
	def has_cycle(self, head: Optional[ListNode]) -> bool:
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				retrun True
		return False