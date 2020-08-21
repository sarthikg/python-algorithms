def binarySearch(array, element):
  left = 0
  right = len(array)-1
  while left <= right:
    middle = (left+right) // 2
    print(left, middle, right)
    if array[middle] == element:
      return middle
    elif element > array[middle]:
      left = middle+1
    elif element < array[middle]:
      right = middle-1
  return -1