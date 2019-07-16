#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        needAddOne = False
        # start node is not actual first node
        startNode = ListNode(0)
        lastNode = startNode
        while True:
            if not l1 or not l2:
                break
            currRes = l1.val + l2.val
            currRes += 1 if needAddOne else 0
            if currRes > 9:
                needAddOne = True
                currRes -= 10
            else:
                needAddOne = False
            currNode = ListNode(currRes)
            lastNode.next = currNode
            lastNode = currNode

            l1 = l1.next
            l2 = l2.next
        leftList = l1 if l1 else l2
        while True:
            if not leftList:
                break
            currRes = leftList.val
            currRes += 1 if needAddOne else 0
            if currRes > 9:
                needAddOne = True
                currRes -= 10
            else:
                needAddOne = False
            currNode = ListNode(currRes)
            lastNode.next = currNode
            lastNode = currNode
            leftList = leftList.next
        if needAddOne:
            lastNode.next = ListNode(1)
        startNode = startNode.next
        return startNode

