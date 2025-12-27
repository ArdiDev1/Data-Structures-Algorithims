string = "This is a sample string for demonstration purposes."

string = string.replace("sample", "test")
print(string)

string = string.upper()
print(string)

string = string.lower()
print(string)

string_list = string.split(" ")
print(string_list)

string = " ".join(string_list)
print(string)

string[1].isascii() 
print(string[1].isascii())