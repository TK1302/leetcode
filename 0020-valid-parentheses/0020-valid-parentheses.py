class Solution:
    def isValid(self, s):
        stack = []
        opening = set(['(', '[', '{'])
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()

        return len(stack) == 0
