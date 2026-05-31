
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=[]
        freq=Counter(nums)
        for i in range(k):
            max1=freq.most_common(1)[0][0]
            del freq[max1]            
            a.append(max1)
        return a

































