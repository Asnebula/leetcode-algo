# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = self.conv2int(l1)
        num2 = self.conv2int(l2)
        return self.conv2LN(num1 + num2)

    # convert to integer and reversely
    def conv2int(self, l):
        num = str(l.val)
        n_next = l.next
        while n_next is not None:
            tmp_ln = n_next.val
            num += str(tmp_ln)
            n_next = n_next.next
        return int(num[::-1])

    # convert to ListNode and reversely
    def conv2LN(self, i):
        def conv(i):
            if 0 == i:
                return None
            else:
                tmp = ListNode(i % 10)
                i = i // 10
                tmp.next = conv(i)
                return tmp

        if 0 == i:
            return ListNode(0)
        else:
            return conv(i)
