class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for element in image:
            i = 0
            j = len(image) - 1


            while i <= j:
                element[i], element[j] = element[j], element[i]
                i += 1
                j -= 1

            for i in range(len(image)):
                if element[i] == 0:
                    element[i] = 1
                else:
                    element[i]  = 0

        return image