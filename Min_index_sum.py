class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
       
       freq = {name: i for i, name in enumerate(list1)}

       result = []
       _min = float('inf')

       for j, name in enumerate(list2):
           if name in freq:
               current = j + freq[name]

               if current < _min:
                   _min = current
                   result = [name]
               elif current == _min:
                   result.append(name)

       return result