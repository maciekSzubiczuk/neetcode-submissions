class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_value = arr[n-1]
        for i in range(n-1,-1,-1):
            print(f"arr[{i}]: {arr[i]}, max_value:{max_value}")
            if arr[i] > max_value:
                new_max = arr[i]
                arr[i] = max_value
                max_value = new_max
            else:
                arr[i] = max_value
            print(f"after arr[{i}]: {arr[i]}, max_value:{max_value}")
            
        arr[n-1] = -1
        return arr
                