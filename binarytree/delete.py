class TreeNode:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    def insert(root,key):
        if root is None:
            return TreeNode(key)
        if key <root.val:
            root.left=insert(root.left,key)
            
        else :
            root.right-insert(root.right,key)
            
        return root
    def minValueNode(node):
        current = node
        while current.left is not None:
            current=current.left
        return current