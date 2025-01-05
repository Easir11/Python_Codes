#List In Python is collection of variables

#Empty list
empty_list = []

#List with values
fruits = ['apple', 'banana', 'cherry', 'mango']

#Mixed types
mixed = [1, 'hello', 3.14, True]

print(fruits[0], fruits[1], fruits[2], fruits[3])
print(fruits[-1], fruits[-2], fruits[-3], fruits[-4])
print(fruits[0:4])
print(fruits[0:])
print(fruits[:2])

#Add in the end
fruits.append('Naspati')

#Insert at a specific position
fruits.insert(1, 'Jum')

print(fruits)

#Remove by value
fruits.remove('cherry')

#Remove by index
fruits.pop(2)

# Removes the last item
fruits.pop()   

# Clear the entire list
mixed.clear()

# Count occurrences of an item
print(fruits.count('apple'))

# Find index of the first occurrence
print(fruits.index('apple'))

nums=[1,2,3,4,5]

# Reverse the list
nums.reverse()
print(nums)

#Sort the list
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)


#2D List Comprehension
comprehension_1D=[[x for x in range(0,5,1) for i in range(0,10,1)]]
print(comprehension_1D)

comprehension_2D=[[i for i in range(0,20,1) if i%2==0],[i for i in range(0,20,1) if i%2!=0]]
print(comprehension_2D)

#Slicing in 2D List

matrix = [
    [1, 2, 3, 4],   # Row 0
    [5, 6, 7, 8],   # Row 1
    [9, 10, 11, 12] # Row 2
]

print(matrix[0:3])




