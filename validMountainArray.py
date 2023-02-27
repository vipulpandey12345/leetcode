class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_in_arr = max(arr)
        not_found_max = False
        i = 0
        while i != len(arr) - 1 and not not_found_max:
            if arr[i] == max_in_arr:
                not_found_max = True
                break
            elif arr[i] >= arr[i + 1]:
                return False
            i += 1
        while i != len(arr) - 1 and not_found_max:
            if arr[i] <= arr[i + 1]:
                return False
            i += 1
        return True
