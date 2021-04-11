class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deep_sum, depth = 0, 0
        stack = [(root, 0)]

        while stack:
            node, curr_depth = stack.pop()
            if node.left is None and node.right is None:
                if curr_depth > depth:
                    deep_sum = node.val
                    depth = curr_depth
                elif depth == curr_depth:
                    deep_sum += node.val
            else:
                if node.right:
                    stack.append((node.right, curr_depth + 1))
                if node.left:
                    stack.append((node.left, curr_depth + 1))

        return deep_sum
