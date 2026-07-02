# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        
        stack = [root]
        

        while stack:
            curr = stack.pop()

            if curr is None:
                ans.append("N")
                continue

            ans.append(str(curr.val))

            stack.append(curr.right)
            stack.append(curr.left)
        
        return ",".join(ans)
        
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")

        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return
            
            node = TreeNode(vals[self.i])
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))