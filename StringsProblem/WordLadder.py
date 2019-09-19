s="abcabcdd"
def lengthOfLongestSubstring(s):
    dic = {}
    storage = []
    result = ""
    for i in range(len(s)):
        if s[i] in dic:
            storage.append(result)
            dic = []
            result = ""
        else:
            dic[i] = 1
            result += s[i]
    print(storage)

