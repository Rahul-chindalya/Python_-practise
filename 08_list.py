# List Methods 
list_nums = [10,20,30,40,50]
print(list_nums) # Before append
list_nums.append(60) # one element
print(list_nums) # After append

# list_nums.append(70,80) # multiple element
# TypeError: list.append() takes exactly one argument (2 given)
list_nums.append([70,80])
print(list_nums) # After append --> added as nested list

list_nums.append("Hello")
print(list_nums)

# In Lists we can have duplicates
list_nums.append(60)
list_nums.append("Hello")
print(list_nums)

list_nums = [10,20,30,40,50]
# list_nums.extend(60) --> TypeError: 'int' object is not iterable
list_nums.extend([60]) 
print(list_nums)

list_nums.extend([70,80])
print(list_nums) # After extend --> added as Individually
list_nums.extend("Hello")
print(list_nums)

# list_nums.extend([70,80],[90,100]) --> TypeError: list.extend() takes exactly one argument (2 given)
print(list_nums)

list_nums = [10,30,40,50]
print(list_nums)
list_nums.insert(1,20)
print(list_nums)

list_nums.insert(10,20)
print(list_nums)

list_nums.insert(0,5)
print(list_nums)

list_nums[0] = 15
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.pop()
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.pop(2)
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
# list_nums.pop(10) --> IndexError: pop index out of range
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.remove(20)
print(list_nums)
# list_nums.remove(60) --> ValueError: list.remove(x): x not in list
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.clear()
print(list_nums)

list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
print(list_nums)
print(list_nums.index(40))

print(list_nums.index(20,4,8))

list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
print(list_nums.count(50))

list_nums = [10,20, 30,40,50]
print(list_nums)

backup_list_nums = list_nums.copy() # shallow copy
print(backup_list_nums)

backup_list_nums.append(60)

print("Original: ", list_nums)
print("Updated: ", backup_list_nums)

# Soft copy 
list_nums = [10,20, 30,40,50]
print(list_nums)

backup_list_nums_soft = list_nums # Soft copy
backup_list_nums_soft.append(60)

print("Original: ", list_nums)
print("Updated: ", backup_list_nums_soft)

list_nums = [10,20, 30,40,50]
print(list_nums)

print(list_nums.reverse())
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
# print(text[::-1])
print(list_nums[::-1])
print(list_nums)

list_nums = [10,30,20,50,40]
print(list_nums)
print(list_nums.sort(reverse=False)) # ascending
print(list_nums)

print(list_nums.sort(reverse=True)) # descending
print(list_nums)

list_text = ["hi","abc","zoro"]
print(list_text)
print(list_text.sort())
print(list_text)

mixed_list = ["hi",2,3.5,"abc","zoro"]
print(mixed_list)
print(mixed_list.sort())
print(mixed_list)




#demo

----------------------------
----------------------------

# simple variable
value = 10 # regular int
values = 10,20,30 # data structure -> tuple

print(type(value))
print(type(values))

# Create Empty List
empty_list = []
print(type(empty_list))
print(empty_list)

# Create List With Numeric Data
list_nums = [10,20,30,40,50]
print(type(list_nums))
print(list_nums)

# Create List With Text Data
list_courses = ["Python","Java","Cloud"]
print(list_courses)

# Create List With Mixed Data
list_mixed = [1,2,3.5,"Python"]
print(list_mixed)

# Access data in lists
list_nums = [10,20,30,40,50]
# Indexing
print(list_nums[0])
print(list_nums[-1])

# Slicing
print(list_nums[:])
print(list_nums[::])
print(list_nums[::2])
print(list_nums[::-1])

# Memory Management
list_nums_1 = [10,20,30,40,50]
list_nums_2 = [10,20,30,40,50]
print(id(list_nums_1)) # 4375154432
print(id(list_nums_2)) # 4375175104

print(id(list_nums_1[0])) # 4374178384
print(id(list_nums_2[0])) # 4374178384
value = 10
print(id(value)) # 4374178384

# Accessing Out Of Range Elements
list_nums = [10,20,30,40,50]
# print(list_nums[10]) # IndexError: list index out of range

# Loop Through List for accessing/operating on indiviudal elements
# for loop
for i in list_nums:
    print(i) # deafult is new line

# for i in list_nums:
#     print(i,end=" ") 

# for i in list_nums:
#     print(i,end="-") 

# create list with class
list_nums = list()
print(list_nums)   

list_nums = list([10,20,30,40,50])
print(list_nums)

# if we pass an non-iterable object
# list_nums = list(10) # TypeError: 'int' object is not iterable
list_nums = list([10]) 
print(list_nums)

# iterable check 
value = 10 # no __iter__ means not iterable
# print(dir(value))

list_value = [10]
print(dir(list_value)) # we get __iter__ means it's iterable

string_value = "Ravi"
print(dir(string_value)) # we get __iter__ means it's iterable

# Range -> gives range of values
range_values = range(6)
for i in range_values:
    print(i)

range_values_list = list(range(0,51,5))
print(range_values_list)

# perform some operations on list items
# arithmetic operations
for i in range_values_list:
    print(i*2)

# in to check if item is available
days = ["sun","mon","tue","wed","thu","fri","sat"]    
print("wed" in days)
check_day = input("Enter Day Name In a Week: ")
if check_day in days:
    print(f"Day {check_day} Exists")
else:
    print(f"Day {check_day} Doesn't Exist")

print(dir(list_value))