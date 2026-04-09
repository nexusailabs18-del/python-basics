            #  Revision overview of the Week  [Who am I?]
first_name = "Ridhan"
last_name = "Kumarxyz"
print(f"Hello, {first_name} {last_name.removesuffix('xyz')}, welcome to the world of Python programming!")
fav_player = "12Virat Kohli"
print(f"\n\tMy favourite cricketer is the king of cricket, {fav_player.removeprefix('12')}.")
my_marks = 90+4
print(f"I scored {my_marks} percent in class 8th exams, and my marks are (out of 60):")
marks = [59,58,57,54,58,46]
print(f"\t{marks[0]} in maths.")
print(f"\t{marks[1]} in english")
print(f"\t{marks[2]} in social science.")
print(f"\t{marks[3]} in science.")
print(f"\t{marks[4]} in hindi.")
print(f"\t{marks[5]} in sanskrit, which was very tough exam.")  # Never got below 55 in sanskirt before 😭
print(f"\nI want to improve myslef day be day and second by second 😎.")
my_hobbies = ['Playing cricket','Dreaming big','Coding in Python','Watching kohli scoring','Cooking friends']
print(f"My hobbies are:")
print(f"\t{my_hobbies[0]} with my friends where we play local cricket with sticks and tennis balls.")
print(f"\t{my_hobbies[1]} about becoming a successful person in life and making my parents proud.")
print(f"\t{my_hobbies[2]} and learning new things in Python programming language.")
print(f"\t{my_hobbies[3]} and cheering for my favourite cricketer, THE King, Virat Kohli.")
print(f"\tI ❤️ {my_hobbies[4]} both with words and runs.")
secret = "dbpl"
print(f"\n🤫 Our series name {secret.upper()} 'Dandi Ball Premier League' is very exciting!")
print(f"I am trying to hold the most runs cap for the first time🏏" )
print(f"I don't know why we dont fell real cricket not more exciting playing than our DBPL series.")
my_hobbies.insert(2, "Love in physics")
print(f"Oh, I forgot to mention that I also had a deep interest in {my_hobbies[2]}.")
popped_mark = marks.pop(5)
print(f"Oh! These are my losted marks recorded ever: {popped_mark}")
my_hobbies.sort()
print(f"My hobbies in sorted order are: {my_hobbies}")
my_hobbies.sort(reverse=True)
print(f"My hobbies in reverse sorted order are: {my_hobbies}")
print(f"At last I had total {len(my_hobbies)} hobbies and I am proud of all of them.") 
