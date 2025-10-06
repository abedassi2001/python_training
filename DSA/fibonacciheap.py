# class Node :
#     def __init__(self, data , marked=False,degree=0): 
#         self.data = data  
#         self.next = None
#         self.marked = marked # we sae so that when we delete
#         self.degree = degree # we save this for the root nodes


# class FibonacciHeap:
#     def __init__(self):
#         self.min_node = None
#         self.num_nodes = 0

#     def insert(self, data):
#         new_node = Node(data)
#         if self.min_node is None:
#             self.min_node = new_node
#             new_node.next = new_node
#         else:
#             self._link_nodes(self.min_node, new_node)
#             if data < self.min_node.data:
#                 self.min_node = new_node
#         self.num_nodes += 1

#     def get_min(self):
#         if self.min_node is None:
#             return None
#         return self.min_node.data

#     def extract_min(self):
#         min_node = self.min_node
#         if min_node is not None:
#             if min_node.next == min_node:  # Only one node in the heap
#                 self.min_node = None
#             else:
#                 # Remove min_node from the root list
#                 self._remove_node(min_node)
#                 # Add its children to the root list
#                 child = min_node.child
#                 if child is not None:
#                     children = []
#                     current = child
#                     while True:
#                         children.append(current)
#                         current = current.next
#                         if current == child:
#                             break
#                     for c in children:
#                         self._link_nodes(self.min_node, c)
#                 self.min_node = min_node.next
#                 self._consolidate()
#             self.num_nodes -= 1
#         return min_node.data if min_node else None

#     def _link_nodes(self, node1, node2):
#         node1_next = node1.next
#         node1.next = node2
#         node2.next = node1_next

#     def _remove_node(self, node):
#         prev = node
#         while prev.next != node:
#             prev = prev.next
#         prev.next = node.next
# make a list of lists of size 100
lists = [[] for _ in range(100)]
print(lists)
#         node.next = node  # Isolate the node
lists[0].append(1)
lists[99].append(2)
print(lists)









# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# lists=[[]]
# def answer(self,root,depth):
#         if root is None :
#             return 
#         if root.left is None and root.right is None :
#             lists[depth].append(root.val)
#             return 1
#         if root.left :
#             answer(self,root.left,depth+1)
#         if root.right :
#             answer(self,root.right,depth+1)
#         lists[depth ].append(root.val)
#         return 

# def find_max_depth(self,root,depth):
#         localdepth_left = 1
#         localdepth_right = 1 
#         if root is None :
#             return 0
#         if root.left is None and root.right is None :
#             return 1
#         if root.left :
#             localdepth_left += find_max_depth(self,root.left,depth)
#         if root.right :
#             localdepth_right += find_max_depth(self,root.right,depth)            
#         return max(localdepth_right,localdepth_left)     
# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[List[int]]
#         """
#         global lists
#         depth = 0
#         #answer = answer(self , root , depth)
#         tree_depth = find_max_depth(self,root,depth)
#         print(tree_depth)
#         lists_demo = [[] for _ in range(tree_depth )]
#         lists = lists_demo
#         answer(self,root,0)
#         return lists

    

                                          
