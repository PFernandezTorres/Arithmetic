from arithmetic_arranger import arithmetic_arranger

def main(): 
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
    print()
    print()
    arithmetic_arranger(["45 + 666", "3801 - 662", "245 + 754", "976 + 2435"], False)

if __name__ == "__main__":
    main()