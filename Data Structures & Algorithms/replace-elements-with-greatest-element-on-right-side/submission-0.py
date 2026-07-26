class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        largest = arr[-1]

        for i in range(1,length+1):
            if arr[-i] > largest:
                new_largest = arr[-i]
                arr[-i] = largest
                largest = new_largest

            else:
                arr[-i] = largest
        
        arr[-1] = -1

        return arr

        