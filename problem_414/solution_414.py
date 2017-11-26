def listify(string):
    list = []
    for char in string:
        if char != ' ' and char != '[' and char != ']' and char != ',':
            list.append(int(char))
    return list

def thirdMax(list):
    first_max = None
    second_max = None
    third_max = None
    for member in list:
        if member > first_max:
            third_max = second_max
            second_max = first_max
            first_max = member
        elif member > second_max and first_max != member:
            third_max = second_max
            second_max = member
        elif member > third_max and second_max != member and first_max != member:
            third_max = member
    if third_max == None:
        return first_max
    return third_max

if __name__ == '__main__':
    string_list = raw_input("Enter a list (ex. [3,2,1]): ")
    list = listify(string_list)
    print("Output: %d") % (thirdMax(list))
