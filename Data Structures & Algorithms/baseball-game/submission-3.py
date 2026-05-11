class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):

            try:
                int(operations[i])
                record.append(int(operations[i]))
                print(f"record {int(operations[i])}")
            except ValueError:
                if operations[i].strip() == "+":
                    record.append(record[-1] + record[-2])
                    print(f"record[-1] {record[-1]}")
                    print(f"record[-2] {record[-2]}")
                    print("+")
                    for x in record:
                        print(f"record: {record}")
                if operations[i].strip() == "C":
                    record.pop()
                    print("C")
                    for x in record:
                        print(f"record: {record}")
                if operations[i].strip() == "D":
                    record.append(record[-1] * 2)
                    print(f"record[-1] * 2 {record[-1] * 2}")
        
        final_score = 0
        for i in range(len(record)):
            final_score = final_score + record[i]
        return final_score