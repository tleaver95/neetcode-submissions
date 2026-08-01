class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        failed_counter = 0

        while len(sandwiches) > 0:
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
                failed_counter = 0
            else:
                failed_student = students.pop(0)
                students.append(failed_student)
                failed_counter += 1

                if failed_counter == len(students)+1:
                    return len(students)

        return 0
            

        
        
    
        return len(students)
