def longestSubstringWithoutRepeating(str):
  l = 0
  result = 0
  recorded = set()
  for i in range(len(str)):
    while str[r] in recorded:
      result = max(result, r - l + 1)
      recorded.remove(s[l])
    recorded.add(s[r])
    l += 1
  return result
  
