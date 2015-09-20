# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1, l2
        p = None
        p_cur = p
        c = 0
        while (True):
            if p1 == None and p2 == None and c == 0:
                return p
            else:
                if p_cur:
                    p_cur.next = ListNode(0)
                    p_cur = p_cur.next
                else:
                    p = ListNode(0)
                    p_cur = p
                d1, d2 = 0, 0
            if p1:
                d1 = p1.val
                p1 = p1.next
            if p2:
                d2 = p2.val
                p2 = p2.next

            d = d1 + d2 + c

            if d >= 10:
                d = d - 10
                c = 1
            else:
                c = 0
            p_cur.val = d