class Solution:
    def ladderLength(self,begin,end,wordList):
        set1=set(wordList)
        if end not in set1:
            return 0
        queue=deque()
        queue.append([begin,1])
        while queue:
            word,level=queue.popleft()
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    new=word[:i]+j+word[i+1:]
                    if new==end:
                        return level+1
                    if new in set1:
                        set1.remove(new)
                        queue.append([new,level+1])
        return 0
