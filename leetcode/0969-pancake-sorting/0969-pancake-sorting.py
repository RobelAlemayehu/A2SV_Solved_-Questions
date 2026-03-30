class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:


        def reverse(array, end):
            
            start = 0
            while start < end:
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1
      
        n = len(arr)
        result = []
      
        for current in range(n - 1, 0, -1):
            target = current + 1
            index = current
          
            while index > 0 and arr[index] !=  target:
                index -= 1
          
            if index < current:
                if index > 0:
                    result.append(index + 1)
                    reverse(arr, index)
              
                result.append(current + 1)
                reverse(arr, current)
      
        return result