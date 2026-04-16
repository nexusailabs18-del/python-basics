                # Reviewing previous topics.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car =='bmw':
    print(car.upper())
  else:
    print(car.title())
car = 'Lamborghini'
if car.lower() == 'lamborghini':
  print(car.upper())
else:
  print("I have no budget for this car. It's too expensive.😭😭")

the_king = 'virat kohli'
if the_king != 'rohit sharma':
  print("Still you are not the king!😒")
else:
  print("You are the king kohli!😎")

prince = 77
king = 18
print(prince >= 99 and king >= 99)    # False
print(prince >= 99 or king >= 18)     # True

top_centuriens = ['virat kohli', 'sachin tendulkar', 'ricky ponting', 'brian lara']
print('virat kohli' in top_centuriens)  # True
print('ms dhoni' in top_centuriens)     # False

top_wickettakers = ['shane warne', 'jimmy anderson', 'irfan pathan', 'mohammad shami','shoaib akhtar']
print('jasprit bumrah' not in top_wickettakers)    # True
print('jimmy anderson' not in top_wickettakers)    # False

kohli_had_80_plus_centuries = True; rohit_had_80plius_centuries = True
rohit_had_80_plus_centuries = False
if kohli_had_80_plus_centuries:
  print("Virat Kohli is a legend!😎😎")
else:
  print("Dear wake up from dreams!🤫")
if rohit_had_80_plus_centuries:
  print("No way, his work is differnet!😎😎")
else:
  print("Rohit Sharma is still a legend!😎😎")

                 # Try it yourserlf
car = 'lamborghini'
name = 'ridhan'
age = 14

print("Is car == 'lamborghini'? I predict True.")
print(car == 'lamborghini')

print("\nIs name == 'ridhan'? I predict True.")
print(name == 'ridhan')

print("\nIs age == 14? I predict True.")
print(age == 14)
    
print("Is car == 'LAMBORGHINI'? I predict True.")
print(car.lower() == 'lamborghini')

print("\nIs name == 'ARYAN'? I predict False.")
print(name.lower() == 'aryan')

print("\nIs age == 14? I predict True.")
print(age == 14)

print("\nIs age == 15? I predict True.")
print(age + 1 == 15)

print("\nIs age > 10? I predict True.")
print(age > 10)

print("\nIs age <= 10 and age >= 10? I predict False.")
print(age < 10 and age >= 10)

print("\nIs age != 10 or >= 10? I predict True.")
print(age != 10 or age >= 10)

print("\nIs car != 'lamborghini' ? I predict False.")
print(car != 'lamborghini')

print("\nIs name 'ridhan' in list? I predict True.")
print('ridhan' in name)

print("\nIs name 'ridhan' not in list? I predict False.")
print('ridhan' not in name)

                         #  If statements
age =19
if age >= 18:
    print("You are old enough to vote.")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age =17
if age >= 18:
    print("You are old enough to vote.")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12 
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
