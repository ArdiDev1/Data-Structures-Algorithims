hashmap = {}

hashmap["apple"] = 1
hashmap["banana"] = 2   
hashmap["cherry"] = 3

hashmap.get("banana")  # Output: 2
has_key = "apple" in hashmap
print(has_key)  # Output: True

# Output: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])  # Convert to list of tuples
my_tuple = hashmap.items()
print(my_tuple)

# Output: dict_keys(['apple', 'banana', 'cherry'])
hashmap.keys()
for key in hashmap.keys():
    print(key) 

# Output: dict_values([1, 2, 3])
hashmap.values()  
for value in hashmap.values():
    print(value)

# Removes key 'banana' and its value
hashmap.pop("banana")  

# Adds multiple key-value pairs
hashmap.update({"date": 4, "elderberry": 5})  