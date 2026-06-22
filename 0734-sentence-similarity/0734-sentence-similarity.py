class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        is_similar = defaultdict(bool)

        for first, second in similarPairs:
            if first > second:
                first, second = second, first
            
            is_similar[(first, second)] = True
        
        for i in range(len(sentence1)):
            word1, word2 = sentence1[i], sentence2[i]

            if word1 == word2:
                continue
            
            if word1 > word2:
                word1, word2 = word2, word1
            
            if is_similar[(word1, word2)]:
                continue
            
            break
        else:
            return True
        
        return False
