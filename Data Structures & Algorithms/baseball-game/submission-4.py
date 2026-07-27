class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0

        for i, operation in enumerate(operations):

            if operation == "+":
                record.append(record[-1] + record[-2])


            elif operation == "D":
                record.append(record[-1]*2)

            elif operation == "C":
                record.pop()


            else:
                try: 
                    number = int(operation)
                    record.append(number)

                except ValueError:
                    continue


        return sum(record)
