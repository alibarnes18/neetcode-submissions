from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = {}

        left = 0
        have = 0
        required = len(need)

        min_length = float("inf")
        min_left = 0

        for right in range(len(s)):
            char = s[right]

            if char in need:
                window[char] = window.get(char, 0) + 1

                if window[char] == need[char]:
                    have += 1

            
            while have == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left

                left_char = s[left]

                if left_char in need:
                    if window[left_char] == need[left_char]:
                        have -= 1

                    window[left_char] -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_left:min_left + min_length]