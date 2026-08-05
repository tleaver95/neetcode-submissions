class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Height = len(matrix)
        Width = len(matrix[0])

        # Search the rows
        B, T = 0 , Height -1

        while B <= T:
            mid = (B + T)//2

            if matrix[mid][0] > target:
                T = mid - 1

            elif matrix[mid][-1] < target:
                B = mid + 1 
            
            else:
                row_idx = mid
                arr = matrix[row_idx]

                L, R = 0, len(arr) - 1

                while L <= R:
                    mid = (L+R)//2

                    if arr[mid] > target:
                        R = mid - 1

                    elif arr[mid] < target:
                        L = mid + 1
                    
                    else:
                        return True 

                return False
        return False







        