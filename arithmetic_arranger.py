import re

class arithmetic_arranger:
    def __init__(self, numbers, answers):
        self.exceptions(numbers)
        self.arithmetic_arranger(numbers, answers)

        
    def arithmetic_arranger(self, numbers, answers):
        first = []
        second = []
        sign = []

        for n in numbers:
            first.append(re.findall("^[0-9]+", n)[0])
            second.append(re.findall(" [0-9]+", n)[0])
            sign.append(re.findall("[+-]", n)[0])

        for f in first:
            print("  ", end = "")
            print(f, end = "\t")

        print()

        for si in sign:
            print(si, end = "\t")  

        print()

        for s in second:
            print("  ", end = "")
            print(s, end = "\t")

        print()

        for i in range(0, 4):
            print("-----", end = "\t")

    def exceptions(self, numbers):
        if (len(numbers) > 5):
            raise Exception("Too much problems")

        for val in numbers:
            if ('*' in val or '/' in val):
                raise Exception("Multiplication or division not accepted")

        for val in numbers:
            new_list = re.findall("[0-9]+", val) 
            for num in new_list:
                if (len(num) > 4):
                    raise Exception("Number too big")

    


