hashmap = {}

hashmap["apple"] = 1
hashmap["eppla"] = 5
hashmap["banana"] = 2   
hashmap["cherry"] = 3

hashmap.get("banana")  # Output: 2
has_key = "apple" in hashmap
print(has_key)  # Output: True

my_tuple = hashmap.items()  # Output: dict_items([('apple', 1), ('banana', 2), ('cherry', 3)])  # Convert to list of tuples
print(my_tuple)

hashmap.keys()  # Output: dict_keys(['apple', 'banana', 'cherry'])
for key in hashmap.keys():
    print(key) 

hashmap.values()  # Output: dict_values([1, 2, 3])
for value in hashmap.values():
    print(value)

hashmap.pop("banana")  # Removes key 'banana' and its value
hashmap.update({"date": 4, "elderberry": 5})  # Adds multiple key-value pairs


my_string = "hello"
my_res = -0-tuple(my_string)