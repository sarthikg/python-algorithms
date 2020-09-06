def DFSPreorder(tree):
  def helper(node):
    tree_elements.append(node.value)
    if node.left:
      helper(node.left)
    if node.right:
      helper(node.right)
  tree_elements = []
  currentNode = tree.root
  helper(currentNode)
  return tree_elements