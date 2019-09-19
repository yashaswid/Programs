# Given a s tring "ABCCBCBA", give an a lgorithm for recurs ively removing lhc a djacent characlers
# if they arc the same. Por example, ABCCBCBA --> ABBCBA-->ACBA



def removeadjacent(s):
    i=1
    while i<len(s):
        if (s[i]==s[i-1]):
            s.pop(i)
            i-=1
        i+=1
    return s

s=["A", "B", "C", "C", "C", "B", "A "]
print(removeadjacent(s))