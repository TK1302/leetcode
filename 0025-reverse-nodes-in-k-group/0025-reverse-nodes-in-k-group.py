class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Calculate the length of the linked list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        # Reverse groups of size k
        prev_group_tail = None
        curr = head
        new_head = None
        i = 0
        
        while i + k <= length:
            group_head = curr
            prev = None
            j = 0
            
            while j < k:
                # Reverse the current node
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                j += 1
            
            # Set the head of the new linked list
            if not new_head:
                new_head = prev
            
            # Connect the reversed group to the previous group
            if prev_group_tail:
                prev_group_tail.next = prev
            
            # Update the tail of the previous group
            prev_group_tail = group_head
            
            # Move to the next group
            i += k
        
        # Connect the remaining nodes after the last group
        if prev_group_tail:
            prev_group_tail.next = curr
        
        # Return the head of the modified linked list
        return new_head
