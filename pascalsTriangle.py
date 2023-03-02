class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1,1]]
        else:
            arr = [[1], [1,1]]
            i = 2
            while i != numRows:
                entry = [0] + arr[-1] + [0]
                first = 0
                second = 1
                new_arr = []
                while second != len(entry):
                    new_arr.append(entry[first] + entry[second])
                    first += 1
                    second += 1
                arr.append(new_arr)
                i += 1
            return arr
