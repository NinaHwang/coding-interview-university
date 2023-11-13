"""
2785. Sort Vowels in a String
https://leetcode.com/problems/sort-vowels-in-a-string/
"""
import heapq


class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        answer = [None] * len(s)
        appeard_vowels = []
        # vowel_indices = []

        for i, c in enumerate(s):
            if c in VOWELS:
                appeard_vowels.append(c)
                # vowel_indices.append(i)
                continue
            answer[i] = c
        appeard_vowels.sort()

        # for i, idx in enumerate(vowel_indices):
        #     answer[idx] = appeard_vowels[i]

        i = 0
        for vowel in appeard_vowels:
            while i < len(s) and answer[i]:
                i += 1
            answer[i] = appeard_vowels
            i += 1
        
        return "".join(answer)
    
print(Solution().sortVowels(s = "lYmpH"))

        


