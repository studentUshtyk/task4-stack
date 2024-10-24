class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode):
    stack, result = [], []  
    current = root
    
    while current or stack:
        while current:
            stack.append(current)  
            current = current.left  
        
        
        current = stack.pop()
        result.append(current.val)  
        current = current.right
    
    return result

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)
print(inorderTraversal(root1))  # Output: [1, 3, 2]

root2 = None
print(inorderTraversal(root2))  # Output: []

root3 = TreeNode(1)
print(inorderTraversal(root3))  # Output: [1]
