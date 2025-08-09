from collections import defaultdict
class Solution:
    def findLadders(self,begin,end,wordList):
        set1=set(wordList)
        if end not in set1:
            return []
        dict1=defaultdict(set)
        level1={begin}
        while level1 and end not in dict1:
            level2=defaultdict(set)
            for word in level1:
                set1.discard(word)
            for word in level1:
                for i in range(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        new=word[:i]+j+word[i+1:]
                        if new in set1:
                            level2[new].add(word)
            dict1.update(level2)
            level1=level2
        list1=[]
        def dfs(word,path):
            if word==begin:
                list1.append(path[::-1])
                return
            for i in dict1[word]:
                dfs(i,path+[i])
        if end in dict1:
            dfs(end,[end])
        return list1
