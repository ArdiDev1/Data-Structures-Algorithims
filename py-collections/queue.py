my_queue = []

my_queue.append('task1')
my_queue.append('task2')    
my_queue.append('task3')

# Removes 'task1'
my_queue.pop(0)  

# Removes 'task2'
my_queue.remove('task2')  

# Adds 'urgent_task' at the front
my_queue.insert(0, 'urgent_task')  

# Adds multiple tasks at the end
my_queue.extend(['task4', 'task5'])  

# Inserts 'task1.5' at index 1
my_queue.insert(1, 'task1.5')  

for task in my_queue:
    print(task)
