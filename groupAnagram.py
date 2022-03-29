class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        for i in strs:
            current_word = [0] * 26
            for j in i:
                letter_index = ord(j) - ord('a')
                current_word[letter_index] += 1
            current_word = tuple(current_word)
            if current_word in groupings:
                groupings[current_word].append(i)
            else:
                groupings[current_word] = [i]
        return groupings.values()
