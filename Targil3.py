#*etgar: list1 = [1,2] ; list2 = [4,5]. create a list of tuples [(1,4), (1,5), (2,4), (2, 50)]
# using list comprehension

list1 = [1,2]
list2 = [4,5]

print([(i_list1, i_list2) for i_list1 in list1 for i_list2 in list2])
