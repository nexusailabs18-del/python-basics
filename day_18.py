             # Dictionaries
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just earned {new_points + 5} points")    # I don't know why while seeing a quite sitting
                                                      # number i become mathematician 😗
alien_0['x_position']    = 0
alien_0['y_position']    = 10
print(alien_0)

                   # Something with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

                   # Modifying a dictionary
alien_0 = {'color':'green'}
print(f"The color of alien is {alien_0['color'].title()}.")
alien_0['color'] = 'yELLOW'
print(f"The color of alien is now {alien_0['color'].title()}.")

                          # Continue
alien_0 = {'x_position':4,'y_position':25, 'speed':'medium'}
print(f"Original posiion: {alien_0['x_position']}")  # Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed']== 'medium':
    x_increment = 2
else:
    x_increment = 3   # This must be a fast alien.

 # The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"The new position: {alien_0['x_position']}")   #  Needs practice and deep understanding.😉

kohli = {'centuries':84,'last_century_runs':124, 'venue' :'indore'}
# Oh I forget his last century to add against newzealand at indore. 🤯🤯🤯
print(f"Kohli total centuries are {kohli['centuries']} against newzealand at {kohli['venue']}.")
print(f"He scored {kohli['last_century_runs']}.")
if kohli['last_century_runs'] == 92:
    total_century_after_that = 0
elif kohli['last_century_runs'] == 124:
    total_century_after_that = 1
else:
    total_century_after_that = 2
kohli['centuries'] = kohli['centuries'] + total_century_after_that
print(f"Finally, Kohli total centuries as of April, 2026 are {kohli['centuries']}.")

          # Removing Key-Value Pairs
# The del statement can be used to remove key-value pairs from a dictionary:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

        # A Dictionary of Similar Objects
fav_language = {
    'jen':'python',
    'sarah': 'C',
    'edward':'rust',
    'phil':'python',
}
language = fav_language['sarah'].title()
print(f"Sarah's favourite language is {language}.")

              # Using get() to access a value
alien_0 = {'color': 'green', 'speed':'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)         # But......
color_value = alien_0.get('color' , 'No color value assigned')
print(color_value)
# Output:
# No point value assigned.
# green

              # Try it yourself
person = {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

fav_no = {'Rohit': 45, 'Kohli' : 18, 'Rahul': 1, 'Dhoni': 7, 'Jasprit': 93}
print(f"Rohit's favorite number is {fav_no['Rohit']}.")
print(f"Kohli's favourite number is {fav_no['Kohli']}.")
print(f"Rahul's favorite number is {fav_no['Rahul']}.")
print(f"Dhoni's favorite number is {fav_no['Dhoni']}.")
print(f"Jasprit's favorite number is {fav_no['Jasprit']}.\n")

programming_words = {'Variable': 'Storage','String': 'Text' , 'List': 'Collection','Function': 'Action','Loop': 'Repetition'}
print(f"Variables are {programming_words['Variable']} words.")
print(f"\nStrings are {programming_words['String']} words.")
print(f"\nLists are {programming_words['List']} words.")
print(f"\nFunctions are {programming_words['Function']} words.")
print(f"\nLoops are {programming_words['Loop']} words.\n")

