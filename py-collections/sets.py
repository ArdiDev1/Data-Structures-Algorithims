set_ex = set()

set_ex.add(1)
set_ex.add(2)   
set_ex.add(3)

set_2 = set()
set_2.add(1)
set_2.add(3)    
set_2.add(5)

has_item = 1 in set_ex
print(has_item)  # Output: True

is_subset = set_2.issubset(set_ex)
print(is_subset)  # Output: false    

is_superset = set_ex.issuperset(set_2)
print(is_superset)  # Output: false

set_intersect = set_ex.intersection(set_2)
print(set_intersect)  # Output: {1, 2}

set_symmetric_diff = set_ex.symmetric_difference(set_2) 
print(set_symmetric_diff)  # Output: {2}

set_diff = set_2.difference(set_ex)
print(set_diff)  # Output: {5}  