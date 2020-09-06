def DFSPostorder(tree):
  def helper(node):
    if node.left:
      helper(node.left)
    if node.right:
      helper(node.right)
    tree_elements.append(node.value)
  tree_elements = []
  currentNode = tree.root
  helper(currentNode)
  return tree_elements