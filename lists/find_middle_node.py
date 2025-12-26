def find_middle_node(head):
    """
    Finds the middle node of a singly linked list.

    :param head: The head node of the singly linked list.
    :return: The middle node of the linked list. If the list has an even number of nodes,
             returns the second middle node.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow