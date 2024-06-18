class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        m = {}
        for i in range(len(difficulty)):
            temp = m.get(difficulty[i], 0)
            m[difficulty[i]] = profit[i] if profit[i] > temp else temp
        keys = list(m.keys())
        keys.sort()
        m = {i: m[i] for i in keys}
        
        largest = 0
        for k in m:
            if m[k] > largest:
                largest = m[k]
            m[k] = largest

        def binary_search(arr, x):
            l = 0
            r = len(keys) - 1
            mid = 0
            prev = -1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] < x:
                    l = mid + 1
                    prev = mid
                elif arr[mid] > x:
                    r = mid - 1
                else:
                    return mid
            return prev

        output = 0
        for w in worker:
            ind = binary_search(keys, w)
            if ind >= 0:
                output += m[keys[ind]]

        return output