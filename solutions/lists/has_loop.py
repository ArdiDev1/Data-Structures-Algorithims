def has_loop(head):
    """
    Detects if a linked list has a loop.

    Args:
        head: The head node of the linked list.
    Returns:
        True if there is a loop in the linked list, False otherwise.
    """  
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False