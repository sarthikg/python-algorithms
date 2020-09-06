def selectionSort(array):
  start_length = 0
  while start_length < len(array)-1:
    smallest_index = start_length
    for i in range(start_length+1, len(array)):
      if array[i] < array[smallest_index]:
        smallest_index = i
    temp_value = array[start_length]
    array[start_length] = array[smallest_index]
    array[smallest_index] = temp_value
    start_length +=1
  return array