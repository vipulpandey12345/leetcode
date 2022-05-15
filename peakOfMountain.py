def peak_of_mountain_array(arr: List[int]) -> int:
    left,right = 0, len(arr) - 1
    res = -1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            res = arr[mid]
            right = mid
        else:
            left = mid + 1
    return res
