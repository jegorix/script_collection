

def FindLongestSubstring(s):
    current = 0
    used_chars = []
    max_count = 0
    i = 0
    
    while i < len(s):
        if s[i] in used_chars:
            idx = used_chars.index(s[i])
            used_chars = used_chars[idx+1:]
            current = len(used_chars)

        used_chars.append(s[i])
        current += 1

        if current > max_count:
            max_count = current

        i += 1

    return max_count

print(FindLongestSubstring("dvdf"))
print(FindLongestSubstring("abcabcbb"))
print(FindLongestSubstring("abcabcbb"))
print("b: x", FindLongestSubstring("bbbbb"))
print(FindLongestSubstring("aab"))
print(FindLongestSubstring(""))
print(FindLongestSubstring("pwwkew"))
print(FindLongestSubstring(" "))
print(FindLongestSubstring("bwf"))