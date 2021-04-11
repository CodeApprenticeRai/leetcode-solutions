'''
hyp: 
It's reduced combinatorial search. 

find the largest multiple less than n, 
find all ways to represent n
find all ways to represent n-3*i
until n=0
'''

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        cache = set()
        return self.f(n, 1, cache) 
    
    def f(self, n, calls, cache):        
        if (n==0):
            return True
        else:
            i=0
            while ((n-3**(i+1)) >= 0):  
                i += 1
            while (i in cache):
                i -= 1
            if (i < 0):
                return False
            
            cache.add(i)
            return self.f(n-3**(i), calls+1, cache)
            