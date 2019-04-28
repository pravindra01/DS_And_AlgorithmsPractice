# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time complexity : O(N\log k) where k is the number of linked lists.

# We can merge two sorted linked list in O(n) time where nn is the total number of nodes in two lists.
# Sum up the merge process 
# Space complexity : O(1)

# We can merge two sorted linked lists in O(1) space.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        if ( amount <= 0):
            return lists
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next   

if __name__ == "__main__":
    test = Solution()
    head = ListNode(0)
    testList = []
    current = head
    for i in (1,4,5):
        newNode = ListNode(i)
        current.next = newNode
        current = newNode
    testList.append(head)
    NewDummy = ListNode(0)
    current = NewDummy
    for i in (1,3,4,5,6,7,8,9):
        newNode = ListNode(i)
        current.next = newNode
        current = newNode
    testList.append(NewDummy.next)
    LastL = ListNode(2)
    LastL.next = ListNode(6)
    testList.append(LastL)
    val = test.mergeKLists(testList)
    current = val
    while current.next is not None:
        print current.val
        current = current.next
    print current.val
