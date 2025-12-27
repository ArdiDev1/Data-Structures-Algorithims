my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)  # Convert tuple to list
my_list.append(6)  # Add an element to the list

my_tuple = tuple(my_list)  # Convert list back to tuple

for item in my_tuple:
    print(item)

my_stack = []

my_stack.append('item1')
my_stack.append('item2')    
my_stack.append('item3')
my_stack.pop()  # Removes 'item3'
my_stack.append('item4')  # Adds 'item4' to the top of the stack        
for item in my_stack:
    print(item) 

my_stack.count('item1')  # Counts occurrences of 'item1' in the stack
my_stack.reverse()  # Reverses the stack order