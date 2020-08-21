def naiveString(long, short):
  count = 0
  for i in range(0, len(long)):
    for j in range(0, len(short)):
      if i+j < len(long)-1:
        if j == len(short)-1 and long[i+j] == short[j]:
          count+=1
        elif long[i+j] != short[j]:
          break
      else:
        break
  return count