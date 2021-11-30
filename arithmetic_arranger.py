import re

class arithmetic_arranger:
    def __init__(self, numbers, answers):
        self.exceptions(numbers)
        self.arithmetic_arranger(numbers, answers)

        

    def arithmetic_arranger(self, numbers, answers):
        firstNumber = []
        secondNumber = []
        sign = []

        for n in numbers:
            firstNumber.append(re.findall("^[0-9]+", n)[0].rjust(4))
            secondNumber.append(re.findall(" [0-9]+", n)[0].rjust(4))
            sign.append(re.findall("[+-]", n)[0])

        for f in firstNumber:
            print("  ", end = "")
            print(f, end = "\t")

        print()

        for si in sign:
            print(si, end = "\t")  

        print()

        for s in secondNumber:
            print("  ", end = "")
            print(s, end = "\t")

        print()

        for i in range(0, 4):
            print("-------", end = "\t")

        print()

        if (answers):
            counter = 0
            result = 0
            while (True):
                if (counter == 4):
                    break
                
                first = int(firstNumber[counter])
                operation = sign[counter]
                second= int(secondNumber[counter])

                if (operation == '+'):
                    result = first + second

                if (operation == '-'):
                    result = first - second

                counter = counter + 1

                print(str(result).rjust(6), end = "\t")

                

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
