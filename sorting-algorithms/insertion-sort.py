def insertionSort(array):
  sorted_length = 1
  while sorted_length < len(array):
    search_length = sorted_length
    while search_length > 0:
      if array[search_length] > array[search_length-1]:
        break
      else:
        temp = array[search_length-1]
        array[search_length-1] = array[search_length]
        array[search_length] = temp
        search_length -= 1
    sorted_length +=1
  return array