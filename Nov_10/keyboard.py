class Solution:
    def findWords(self,words):
        result = []
        line1 = set('qwertyuiop')
        line2 = set('asdfghjkl')
        line3 = set('zxcvbnm')

        for word in words:
            w = set(word.lower())
            if w <= line1 or w <= line2 or w <= line3:
                result.append(word)
        return result 
    
words = ["Hello","Alaska","Dad","Peace"]

answer = Solution().findWords(words)

print('given:',words)
print('filtered:', answer)
