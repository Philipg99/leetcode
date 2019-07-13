class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ""
        a += str(l1.val)
        while l1.next != None:
            l1 = l1.next
            a += str(l1.val)
            
        b = ""
        b += str(l2.val)
        while l2.next != None:
            l2 = l2.next
            b += str(l2.val)
            
        na=int(a[::-1])
        nb=int(b[::-1])
        c=list(map(int,list(str(na+nb))))
        return c[::-1]
        
        
