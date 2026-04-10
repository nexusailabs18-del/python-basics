                     # Working with lists
# Looping allows you to loop through a list and do something with each item in the list.
cricketers = ['Sachin', 'Virat', 'Dhoni', 'Rohit']
for cricketer in cricketers:
 print(cricketer)
 # Output:
# Sachin
# Virat
# Dhoni
# Rohit
cats = ["Leo", "Milo"]
dogs = ["Rex", "Buddy"]
list_of_items = ["Ball", "Treat"]
for cat in cats:
 for dog in dogs:
  for item in list_of_items:
    # Change your print line to this:
    print(f"{cat}, is with {dog}, looking at the {item}.")
    print(f"\tThey are so naughty, doing fun everyday with no work.\n")
 
 print(f"\n\n\tThanks eveyone might looping not looping in your mind 🤣!") # Non-indented list [Therefore, not repeated]
                   # Indentation errors
# Forgetting to indent 
cricketers = ['Sachin', 'Virat', 'Dhoni', 'Rohit']
for cricketer in cricketers:
print(cricketer)
# Output: 
# IndentationError: expected an indented block after 'for' statement on line 25
cricketers = ['Virat', 'Dhoni', 'Rohit']
for cricketer in cricketers:
  print(f"{cricketer.title()} has a athletic body.")
print(f"{cricketer.title()}, is very smart.") # Loop not indented so only we get,[Rohit, is very smart.]

message = "Hello Python World!"
   print(message) # Output: IndentationError: unexpected indent

# Indenting unnecessarily after a loop
cats = ["Leo", "Milo"]
dogs = ["Rex", "Buddy"]
list_of_items = ["Ball", "Treat"]
for cat in cats:
 for dog in dogs:
  for item in list_of_items:
    # Change your print line to this:
    print(f"{cat}, is with {dog}, looking at the {item}.")
    print(f"\tThey are so naughty, doing fun everyday with no work.\n")
    
     print(f"{cricketer.title()}, is very smart.") # Loop not indented so only we get,[Rohit, is very smart.]
    # At last, Output: print(f"{cricketer.title()}, is very smart.") # Loop not indented so only we get,[Rohit, is very smart.]
IndentationError: unexpected indent

 # Forgettinh the colon (:)
cricketers = ['Sachin', 'Virat', 'Dhoni', 'Rohit']
for cricketer in cricketers
 print(cricketer)
 # Output: for cricketer in cricketers                 ^
# SyntaxError: expected ':'

