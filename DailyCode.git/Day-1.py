# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
from collections import defaultdict

def day1 (nums: [int], k: int) -> bool:
    if not nums:
        return False
    d = defaultdict(int)
    for num in nums:
        print(d)
        if abs(k-num) in d:
            return True
        d[num]+=1

day1([10,3,7,1,1,1,1,4], 7)