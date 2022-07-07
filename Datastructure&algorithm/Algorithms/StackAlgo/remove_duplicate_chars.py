class Solution:
    def __repr__(self) -> str:
        words = "careermonk"
        return self.removeAdjacentDuplicates(words)
    def removeAdjacentDuplicates(self,words: str)-> str:
        chars = {}
        for char in words:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] +=1
        res = ""
        for key in chars:
            if chars[key] == 1:
                res += key
        return res
if __name__ == "__main__":       
    print(Solution())