# Python2.7
# 46_Permutations.py

def permutate(ordered_list, breakpoint):
    print("%s") % (''.join(ordered_list))
    list_len = len(ordered_list)
    perm_head = list_len - 2
    perm_tail = list_len - 1
    while perm_head > breakpoint:
        perm_list = list(ordered_list)
        perm_list.insert(perm_head, perm_list.pop(perm_tail))
        permutate(perm_list, perm_head)
        if perm_tail == list_len - 1:
            perm_head = perm_head - 1
            perm_tail = perm_head + 1
        else:
            perm_tail = perm_tail + 1

if __name__ == '__main__':
    number_arr = raw_input("Enter a number to permutate: ")
    number_list = sorted(number_arr)
    permutate(number_list, -1);
