def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:


    temp_node = ListNode()
    current_node =temp_node

    while(l1!= None and l2!= None):
        if(l1.val <l2.val):
            current_node.next = l1
            l1=l1.next
        else:
            current_node.next=l2
            l2=l2.next
        current_node = current_node.next
    
    if l1!=None :
        current_node.next = l1
        l1=l1.next
    if l2!=None:
        current_node.next =l2
        l2=l2.next
    return temp_node.next