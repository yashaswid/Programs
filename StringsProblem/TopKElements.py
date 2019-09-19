from collections import Counter


class Solution:
    def topKFrequent(self, words, k):
        result = []
        dic = Counter(words)
        print(dic)
        count = 0
        for key, v in dic.items():
            if (count < k):
                result.append(key)
                count += 1

        print(result)


sol=Solution()
words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k=4
sol.topKFrequent(words,k)