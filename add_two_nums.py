class Solution:
    def addTwoNumber(self, l1: Optional[ListNodel], l2: Optional[ListNodel]):
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, sum_val = divmod(val1 + val2 + carry, 10)

            curr.next = LsitNode(sum_val)

            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next