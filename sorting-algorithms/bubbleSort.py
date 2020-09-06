def bubbleSort(array):
  end_length = len(array) - 1
  while end_length > 0:
    noSwaps = True
    for i in range(0, end_length):
      if array[i] > array[i+1]:
        temp_value = array[i]
        array[i] = array[i+1]
        array[i+1] = temp_value
        noSwaps = False
    end_length-=1
    if noSwaps:
        break
  return array