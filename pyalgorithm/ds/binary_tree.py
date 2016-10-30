""" Tree """

import queue
import stack

# Defining node
class Node(object):
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

# Operations performed on the tree
class Tree(object):
    def insert(self,root=None,val):
        if root == None:
            root = Node(val=val)
            return root

        if(root.val >= val):
            root.left = self.insert(root.left,val)

        elif (root.val < val):
            root.right = self.insert(root.right,val)

        return root

    def preorder(self,root=None,start = 1,ls = []):
        if root != None:
            #print root.val
            ls.append(root.val)
            self.preorder(root.left,start+1,ls)
            self.preorder(root.right,start+1,ls)
        elif root == None:
            return []
        if start == 1:
            return ls


    def postorder(self,root=None,start = 1, ls = []):
        if root != None:
            self.postorder(root.left,start+1,ls)
            self.postorder(root.right,start+1,ls)
            #print root.val
            ls.append(root.val)

        elif root == None:
            return []

        if start == 1:
            return ls


    def inorder(self,root,start = 1,ls = []):
        if root != None:
            self.inorder(root.left,start+1,ls)
            ls.append(root.val)
            self.inorder(root.right,start+1,ls)

        elif root == None:
            return []

        if start == 1:
            return ls

    def bfs(self,root=None):

        if root == None:
            return []

        ls = []
        q = queue.Queue()
        q.enqueue(root)

        while(not(queue.is_empty())):
            temp = q.dequeue()
            ls.append(temp.val)
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)

        return ls

    def dfs(self,root=None):

        if root == None:
            return []

        ls = []
        stack = stack.Stack()
        


        # Unfinished




#tree = Tree()
#root = None

## Enter the number of nodes in a tree
#number_of_nodes = input()
#while(number_of_nodes):
#    val = input()
#    root = tree.insert(root,val)
#    number_of_nodes -= 1

##Traversals
#print "Preorder Traversal"
#tree.preorder(root)
#print "Postorder Traversal"
#tree.postorder(root)
#print "Inorder Traversal"
#tree.inorder(root)
