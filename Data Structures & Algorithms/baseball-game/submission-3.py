class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0

        for i, operation in enumerate(operations):

            if operation == "+":
                print("reached +")
                print(record[-1] + record[-2])
                record.append(record[-1] + record[-2])
                print(record)

            elif operation == "D":
                print("reached D")
                record.append(record[-1]*2)

            elif operation == "C":
                print("reached C")
                record.pop()


            else:
                try: 
                    number = int(operation)
                    record.append(number)
                    print("reached int")

                except ValueError:
                    continue

            print(record)
            print("reached end")
        
        for score in record:
            total += score

        return total
