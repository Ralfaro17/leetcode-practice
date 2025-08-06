# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]Z
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        root = l1
        l1Digits = ''
        l2Digits = ''
        while(root != None):
            l1Digits += str(root.val)
            root = root.next
        
        root = l2
        while(root != None):
            l2Digits += str(root.val)
            root = root.next
        
        listResult = list(map(int, str(int(l1Digits[::-1]) + int(l2Digits[::-1]))))[::-1]
        newList = ListNode(listResult[0])
        result = newList
        for i in listResult[1::]:
            print(newList)
            newList.next = ListNode(i)
            newList = newList.next

        return result