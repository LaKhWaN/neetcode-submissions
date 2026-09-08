class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        arr = []

        for ele in matrix:
            if target <= ele[len(ele) - 1] and target >= ele[0]:
                arr = ele
                break
        print(arr)
        if len(arr) == 0: return False

        l = 0 
        r = len(arr)

        while l <= r:
            mid = int((l+r) / 2)

            if arr[mid] < target: l = mid + 1
            elif arr[mid] > target: r = mid - 1
            elif arr[mid] == target: return True
        
        return False

            