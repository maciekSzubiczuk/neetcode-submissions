class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized_s = ''.join(c.lower() for c in s if c.isalnum())
        for i in range(len(sanitized_s)):
            k =  len(sanitized_s) -i -1
            if k != i:
                if sanitized_s[k] != sanitized_s[i]:
                    return False
        return True