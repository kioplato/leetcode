#!/usr/bin/python2.7
# 46_Permutations.py

def permute(ordered_list, breakpoint = -1):
    permutations_list = []
    permutations_list.append(ordered_list)
    list_len = len(ordered_list)
    perm_head = list_len - 2
    perm_tail = list_len - 1
    while perm_head > breakpoint:
        perm_list = list(ordered_list)
        perm_list.insert(perm_head, perm_list.pop(perm_tail))
        permutations_list.extend(permute(perm_list, perm_head))
        if perm_tail == list_len - 1:
            perm_head = perm_head - 1
            perm_tail = perm_head + 1
        else:
            perm_tail = perm_tail + 1
    return permutations_list

if __name__ == '__main__':
    number_arr = raw_input("Enter a number to permutate: ")
    number_list = sorted(number_arr)
    print(permute(number_list))
