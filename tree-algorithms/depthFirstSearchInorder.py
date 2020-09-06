def DFSInorder(tree):
  def helper(node):
    if node.left:
      helper(node.left)
    tree_elements.append(node.value)
    if node.right:
      helper(node.right)
  tree_elements = []
  currentNode = tree.root
  helper(currentNode)
  return tree_elements