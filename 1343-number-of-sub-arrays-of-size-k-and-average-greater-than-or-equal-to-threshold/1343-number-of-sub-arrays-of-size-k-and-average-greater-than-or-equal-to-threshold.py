class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        count =0
        w_sum = 0
        for i in range(k):
            w_sum += arr[i]
        m_a = 0
        if w_sum/k >= threshold:
            m_a = w_sum/k
            count+=1
        for i in range(1,len(arr)-k+1):
            w_sum = w_sum-arr[i-1]+arr[i+k-1]
            if w_sum/k >= threshold:
                m_a = max(m_a,w_sum/k)
                count+=1
        return count