class Node:
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right


def invert(root):
  if root is None:
    return None
  
  stack = [root]

  while stack:
    cur_node = stack.pop()

    placeholder = cur_node.left
    cur_node.left = cur_node.right
    cur_node.right = placeholder

    if cur_node.left:
      stack.append(cur_node.left)
    if cur_node.right:
      stack.append(cur_node.right)
    
  return root

node1 = Node(1)
node3 = Node(3)
node2 = Node(2, node1, node3)

root = node2

inverted_root = invert(root)

def printing_traversal(node):
  if not node:
    return []
  return printing_traversal(node.left) + [node.val] + printing_traversal(node.right)

print(printing_traversal(inverted_root))
