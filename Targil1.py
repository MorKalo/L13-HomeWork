#fruits = [“apple”, “banana”, “cherry”, “kiwi”, “mango”]. create a list of all the fruits with the letter ‘a’
# inside them using list comprehension
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
print([a_fruit for a_fruit in fruits if a_fruit.count('a') > 0])
