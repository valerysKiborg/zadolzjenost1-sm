
def merge_lists(list1, list2):
    merged_list = list1 + [item for item in list2 if item not in list1]
    return merged_list


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(merge_lists(list1, list2))  

