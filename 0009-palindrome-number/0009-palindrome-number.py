class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        # Calculate the reverse of the number
        reverse = 0
        temp = x
        while temp > 0:
            reverse = reverse * 10 + temp % 10
            temp //= 10
        
        # Compare the original number with its reverse
        return x == reverse
