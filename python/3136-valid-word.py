class Solution(object):
    def isValid(self, word: str):
        """
        :type word: str
        :rtype: bool
        """
        has_vowel = False
        has_consonant = False
        
        if len(word) < 3:
            return False
        
        for character in word:
            if not has_vowel and character.lower() in ("a", "e", "i", "o", "u"):
                has_vowel = True
            if (
                not has_consonant
                and character.isalpha()
                and character.lower() not in ("a", "e", "i", "o", "u")
            ):
                has_consonant = True
            if not character.isalnum():
                return False

        if has_consonant and has_vowel:
            return True
        return False

# print(Solution().isValid("UuE6"))