class Solution:
    def hasCycle(self, head):
        visited = set() #create a set of visited nodes to keep reference
        while head is not None: #if head = None i reached end of the list 
            if head in visited: 
                return True #if head is in the set then there is a cycle
            visited.add(head) #populate the set with visited 
            head = head.next #step forward in linked list 
        return False
