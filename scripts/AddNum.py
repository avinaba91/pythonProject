from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getDigit(l1, l2) -> dict:
            no1 = 0
            if l1 != None:
                no1 = l1.val
            
            no2 = 0
            if l2 != None:
                no2 = l2.val

            sumNo = sum(no1 + no2)
            if sumNo >= 10:
                dict["0"] = sumNo % 10
                dict["1"] = 1
            else:
                dict["0"] = sumNo
                dict["1"] = -1
            return dict

        reminder = 0
        firstNode = ListNode()
        resultNode = firstNode

        while resultNode != None:
            digiDict = getDigit(l1, l2)
            
            resultNode.val = digiDict["0"] + reminder

            if digiDict["1"] > 0:
                reminder = digiDict["1"]
            l1 = l1.next
            l2 = l2.next
            if l1 != None or l2 != None:
                resultNode.next = ListNode()
                resultNode = resultNode.next
        
        return firstNode