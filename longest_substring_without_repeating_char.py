# class Solution:
def lengthOfLongestSubstring(s):
    char_index = {}
    start = max_length = 0
    longest_substr = ""
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        if end - start + 1 > max_length:
            max_length = end - start + 1
            longest_substr = s[start:end+1]
    return max_length,longest_substr

s = "abdcabcdb"
# solution = Solution()
print(lengthOfLongestSubstring(s))  # Output: 4 ("abcd")