def bubble_sort(my_list):
    #start at the end, largest elem bubbles towards end
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    
    return my_list

my_list = [1, 5, 7, 2, 4, 6]

# Unsorted
print(my_list)

# Sorted 
print(bubble_sort(my_list))