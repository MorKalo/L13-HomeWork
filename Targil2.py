#some_list = [1,4,7,12,19,22, 23, 26]. create of list of string for even or odd: in this case
#[‘1 is odd’, ‘4 is even’, ‘7 is odd’ …] using list comprehension

some_list =[1,4,7,12,19,22, 23, 26]

print([f'{num} is {"Even" if num % 2 == 0 else "Odd"}' for num in some_list])

