#Find all of the numbers from 1-1000 that are divisible by 7
dv7 = [n for n in range(1-1000) if n % 7 == 0]

#Find all of the numbers from 1-1000 that have a 3 in them
hv3 = [n for n in range(1-1000) if '3' in str(n)]

#Count the number of spaces in a string
string = " H e l l o "
spaces = [s for s in string if s == ' ']

#Create a list of all the consonants in the string 
#“Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
string = 'Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams'
vocals = ['a','e','i','o','u']
consonants_list = [c for c in string if c not in vocals]

#Get the index and the value as a tuple for items in 
#the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). 
#Result would look like (index, value), (index, value)
list = ['hi', 4, 8.99, 'apple', ('t,b','n')]
indexed = [(index, item) for (index, item) in enumerate(list)]

#Find the common numbers in two lists (without using a tuple or set)
#list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
list_a = 1, 2, 3, 4
list_b = 2, 3, 4, 5
common_items = [item_a for item_a in list_a if item_a in list_b]

#Get only the numbers in a sentence like ‘In 1984 there were 13 instances 
#of a protest with over 1000 people attending’
sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
words = sentence.split()
numbers_in = [n for n in words if not n.isalpha()]

#Given numbers = range(20), produce a list containing the word ‘even’ if a number 
#in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
numbers = range(20)
even_odd = ['even' if n % 2 == 0 else 'odd' for n in numbers]

#Produce a list of tuples consisting of only the matching numbers in these lists 
#list_a = 1, 2, 3,4,5,6,7,8,9, list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12)
list_a = 1, 2, 3, 4, 5, 6, 7, 8, 9
list_b = 2, 7, 1, 12
match_list = [(a, b) for a in list_a for b in list_b if a == b]

#Find all of the words in a string that are less than 4 letters
string = 'Hello, John, how are yourself today, mate?'
words = string.split()
less4 = [word for word in words if len(word) < 4]

#Use a nested list comprehension to find all of the numbers from 1-1000 
#that are divisible by any single digit besides 1 (2-9)
result = [number for number in range(1,1000) if True in [True for x in range(2,10) if number % x == 0]]
print(result)

