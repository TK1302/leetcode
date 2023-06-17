class Solution(object):
    def reverse(self, x):
        # Check if x is negative
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x
        
        # Reverse the digits of x
        reversed_x = 0
        while x != 0:
            reversed_x = reversed_x * 10 + x % 10
            x //= 10
        
        # Check if the reversed integer is within the 32-bit range
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        # Return the reversed integer with the correct sign
        return -reversed_x if is_negative else reversed_x
