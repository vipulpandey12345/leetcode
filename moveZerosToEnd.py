def moveZerosToEnd(arr):
  first_store_index = 0
  for i in range(len(arr)):
    if arr[i] == 0:
      if arr[first_store_index] != 0:
        first_store_index = i
    elif arr[i] != 0 and arr[first_store_index] == 0:
      arr[first_store_index],arr[i] = arr[i], arr[first_store_index]
      for j in range(first_store_index,len(arr)):
        if arr[j] == 0:
            first_store_index = j
            break
  return arr
