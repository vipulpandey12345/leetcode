import heapq
def sort_k_messed_array(arr, k):
    if len(arr) == 1:
      return arr
    if k >= len(arr):
      return arr
    count = 0
    heap = []
    output = []
    while count <= len(arr) -1:
        if len(heap) != k:
          heapq.heappush(heap,arr[count])
          count += 1
        lowest = heapq.heappop(heap)
        if arr[count] > lowest:
          output.append(lowest)
          heapq.heappush(heap,arr[count])
          count += 1
          print(heap)
        else:
          heapq.heappush(heap,lowest)
          output.append(arr[count])
          count += 1  
          print(heap)
    if len(heap) != 0:
      while len(heap) != 0:
        output.append(heapq.heappop(heap))
    return output
