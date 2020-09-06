def BFS(tree):
  temp_queue = []
  tree_elements = []

  temp_queue.append(tree.root)
  while temp_queue != []:
    removedNode = temp_queue.pop(0)
    tree_elements.append(removedNode.value)
    if removedNode.left:
      temp_queue.append(removedNode.left)
    if removedNode.right:
      temp_queue.append(removedNode.right)
    print(tree_elements)