class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = [""]
        
        for digit in digits:
            new_result = []
            for combo in result:
                for letter in phone_map[digit]:
                    new_result.append(combo + letter)
            result = new_result
        
        return result
