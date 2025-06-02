number = input('Please enter the impure number:')
separatorset = ""
# This code takes a string of numbers with various separators
for num in number:
    
    if not num.isnumeric():
    
        # If the character is not numeric, it is a separator
        # Replace the separator with an empty string
        separator = num
        separatorset = separatorset+separator 
        number = number.replace(separator, "")

print(number)       
print(separatorset)