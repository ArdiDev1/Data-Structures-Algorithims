def find_kth_node(head, k):
    fast = head
    slow = head

    #advance fast pointer k steps ahead
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    
    #move both pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    #slow now points to the kth node from the end    
    return slow