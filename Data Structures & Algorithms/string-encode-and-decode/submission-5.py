from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # Prefix each string with its length + '#'
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # Find the position of the '#'
            j = s.find('#', i)
            length = int(s[i:j])  # Extract length
            i = j + 1  # Move past the '#'
            result.append(s[i:i+length])  # Extract the string of that length
            i += length  # Move to the next chunk
        return result
