import math

def getDigit(number, place):
  return ((number // (10 ** place)) % 10)

def getTotalDigits(number):
  if number == 0:
    return 1
  return math.floor(math.log(number, 10)) + 1
  
def getMaxDigits(array):
  maxDigits = 0
  for num in array:
    tempMax = getTotalDigits(num)
    if tempMax > maxDigits:
      maxDigits = tempMax
  return maxDigits

def radixSort(array):
  maxDigits = getMaxDigits(array)
  for i in range(0, maxDigits):
    buckets = [[],[],[],[],[],[],[],[],[],[]]
    for num in array:
      bucket = getDigit(num, i)
      buckets[bucket].append(num)
    i = 0
    for bucket in buckets:
      for num in bucket:
        array[i] = num
        i+=1
  return array