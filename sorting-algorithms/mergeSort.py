def mergeSortedArrays(array1, array2):
  pointer1 = 0
  pointer2 = 0
  mergedArray = []
  while pointer1 < len(array1) and pointer2 < len(array2):
    if array1[pointer1] <= array2[pointer2]:
      mergedArray.append(array1[pointer1])
      pointer1 += 1
    elif array1[pointer1] > array2[pointer2]:
      mergedArray.append(array2[pointer2])
      pointer2 += 1
  if pointer1 == len(array1):
    mergedArray.extend(array2[pointer2:])
  else:
    mergedArray.extend(array1[pointer1:])
  return mergedArray

def divideArray(array):
  length = len(array) // 2
  array1 = array[:length]
  array2 = array[length:]
  return (array1, array2)

def mergeSort(array):
  if len(array) < 2:
    return array
  else:
    [array1, array2] = divideArray(array)
    return mergeSortedArrays(mergeSort(array1), mergeSort(array2))