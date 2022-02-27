class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        #populating initial array
        arr = []
        i = 0
        while i != n - 1:
            j = 0
            sub_arr = []
            while j != n - 1:
                sub_arr.append(0)
                j += 1
            arr.append(sub_arr)
            i += 1
        
        stop_left = 0
        stop_right = len(arr[0])
        stop_up = 0
        stop_down = len(arr)
        
