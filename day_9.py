                # Try it yourself (Getiing started with Looping)
pizzas = ['Pepperoni' ,'Margherita', 'Capricciosa' ]
for pizza in pizzas:  # Part 1.
  print(pizza)
  # Output: 
# Pepperoni
# Margherita
# Capricciosa
pizzas = ['Pepperoni' ,'Margherita', 'Capricciosa' ]
for pizza in pizzas:                                      # Part 2.
   print(f'I like {pizza} flavour in pizza.')
# Output: 
# I like Pepperoni flavour in pizza.
# I like Margherita flavour in pizza.
# I like Capricciosa flavour in pizza.
pizzas = ['Pepperoni' ,'Margherita', 'Capricciosa' ]
for pizza in pizzas:                                      # Part 3.
   print(f'I like {pizza} flavour in pizza.')
print(f"\n\tI really love pizza!")             # Output at end of the line with tab : 

#      Working with animals not being 😂
animals = ['rabbits','dogs','cats']
specifications = ['loving','playful']
for animal in animals:
   for specification in specifications:
       print(f"A {animal.removesuffix('s')} is so {specification} 😊 !\n")
print(f"\tAny of these animals would make a great pet!")

               # Making numerical lists.
for value in range(5):
   print(value)
 
numbers = list(range(1000))
print(numbers)

numbers = list(range(2,11,4))
print(numbers)

squares = []
for value in range(1,11):
   square = value**2
   squares.append(square)
print(squares)
          # or
squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)
                 # Simple Statistics
digits = [1, 4, 9, 16, 25]
print(min(digits))
print(max(digits))
print(sum(digits))
        # List Comprehension
squares = [n**3 for n in range(1,11)]
print(squares)

                 # Try it Yourself
numbers = list(range(1,21))
print(numbers)

nombers = []
for value in range(1,1000001):
 no = value 
 nombers.append(no)
print(nombers)
               # or
nombers = []
for value in range(1,1000001):
 nombers.append(value)
print(nombers)
           # or 
nombers = [value for value in range(1,1000001)]
print(nombers)

nombers = [value for value in range(1,1000001)]
print(min(nombers))
print(max(nombers))
print(sum(nombers))

for odd in range(1,21,2):
 print(odd)

multiple_3 = []                   # could also be multiple_3 = [value for value in range(3,31,3)]
for value in range(3,31,3):                     # print(multiple_3)
      multiple_3.append(value)
print(multiple_3)

cube = []
for value in range(1,11):
  cube.append(value**3)
print(cube)

cube = [value**3 for value in range(1,11)]
print(cube)
