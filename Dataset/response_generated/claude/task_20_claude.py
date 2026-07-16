# Task: Write a function to detect a cycle in a linked list.

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head: ListNode) -> bool:
    """
    Detect if a linked list has a cycle using Floyd's cycle detection algorithm.
    
    Args:
        head: The head node of the linked list
        
    Returns:
        True if a cycle is detected, False otherwise
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
