class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_result = []
        for s in strs:
            # Append the length of the string, the separator, and the string itself
            encoded_result.append(f"{len(s)}#{s}")
        return "".join(encoded_result)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded_strs = []
        i = 0
        
        while i < len(s):
            # Find the delimiter '#' starting from the current index
            j = i
            while s[j] != '#':
                j += 1
            
            # The substring s[i:j] represents the length of the next string
            length = int(s[i:j])
            
            # Extract the actual string using the length
            # It starts right after '#' (j + 1) and ends at (j + 1 + length)
            start_idx = j + 1
            end_idx = start_idx + length
            decoded_strs.append(s[start_idx:end_idx])
            
            # Move the pointer to the start of the next encoded block
            i = end_idx
            
        return decoded_strs