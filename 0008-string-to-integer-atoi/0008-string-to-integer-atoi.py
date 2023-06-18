class Solution(object):
    def myAtoi(self, s):
        i = 0
        sign = 1
        result = 0
        
        # Step 1: Skip leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1
        
        # Step 2: Check sign
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 4: Convert digits to integer
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
        
        # Step 5: Clamp result to 32-bit range
        result = max(-2**31, min(sign * result, 2**31 - 1))
        
        return result
