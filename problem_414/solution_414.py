def thirdMax(list):
    if len(list) != 0:
        first_max = None
        second_max = None
        third_max = None
        for member in list:
            if first_max == None:
                first_max = member
            elif second_max == None:
                if member < first_max:
                    second_max = first_max
                    first_max = member
                elif member != first_max:
                    second_max = member
            elif third_max == None:
                if member < first_max:
                    third_max = second_max
                    second_max = first_max
                    first_max = member
                elif member != second_max:
                    third_max = member
            else:
                if member < first_max:
                    third_max = second_max
                    second_max = first_max
                    first_max = member
        if third_max == None:
            return first_max
        else:
            return third_max
    else:
        return None

if __name__ == '__main__':
    print("Type a number to add to the list.")
    print("Type -1 to stop inputing numbers.")
    list = []
    number = 0
    while number != -1:
        number = int(raw_input("Your input: "))
        if number == -1:
            break;
        list.append(number)
        print("The list is now: %s.") % (list)
    print("Calculating...")
    print("Output: %d.") % (thirdMax(list))
