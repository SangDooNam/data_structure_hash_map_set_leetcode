from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False
        
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        if set(counter1) != set(counter2):
            return False

        if sorted(counter1.values()) == sorted(counter2.values()):
            return True
        return False
        
# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
        
#         if len(word1) != len(word2):
#             return False
#         dct_1 = {}
#         dct_2 = {}
        
#         for letter in word1:
#             dct_1[letter] = dct_1.get(letter, 0) + 1
        
#         for letter in word2:
#             dct_2[letter] = dct_2.get(letter, 0) + 1
        
#         key_1 = sorted(dct_1.keys())
#         key_2 = sorted(dct_2.keys())
#         value_1 = sorted(dct_1.values())
#         value_2 = sorted(dct_2.values())
        
#         if key_1 == key_2 and value_1 == value_2:
#             return True
        
#         return False
        
        
        




# word1 = "abc"

# word2 = "bca"


word1 = "cabbba"
word2 = "abbccc"
# word1 = "a"
# word2 = "aa" 
sol = Solution()
print(sol.closeStrings(word1, word2))