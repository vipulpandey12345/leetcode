class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) == 1:
            return s
        new_string_arr = s.split(" ")
        new_string = ""
        i = len(new_string_arr) - 1
        while i >= 0:
            if " " not in new_string_arr[i]:
                new_string += new_string_arr[i] + " "
                i -= 1
        return new_string[:-1]
