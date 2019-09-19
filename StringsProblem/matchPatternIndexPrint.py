def patternMatch(str,pattern):

    for i in range(len(str)-len(pattern)+1):
        patterni,stri=0,i
        while stri<len(str) and patterni<len(pattern) and str[stri]==pattern[patterni]:
            stri+=1
            patterni+=1
        if patterni==len(pattern):
            return i
    return -1
print(patternMatch("fdgfabcdabc","abc"))
