class Solution:
    def twoSum(self, nums, target):
        # Create a hash table to store the elements and their indices
        hash_table = {}
        
        # Iterate through the array.
        for i in range(len(nums)):
            complement = target - nums[i]
            
            # Check if the complement exists in the hash table
            if complement in hash_table:
                return [hash_table[complement], i]
            
            # Add the current element to the hash table
            hash_table[nums[i]] = i
        
        # If no solution is found, return an empty array
        return []
