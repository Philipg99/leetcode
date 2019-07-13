class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nl=[]
        for i in range(len(nums)):
            nl+=[[nums[i],i]]
        nl.sort()
        for n1 in range(len(nl)):
            for n2 in range(n1+1,len(nl)):
                if nl[n1][0]+nl[n2][0]==target:
                    return [nl[n1][1],nl[n2][1]]
                if nl[n1][0]+nl[n2][0]>target:
                    break
        '''
        for n1 in range(len(nums)):
            for n2 in range(n1+1,len(nums)):
                if nums[n1]+nums[n2]==target:
                    return [n1,n2]
        
        '''
            
