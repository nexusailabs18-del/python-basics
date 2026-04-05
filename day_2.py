author = "albert einstein"
quote = "A person who never made a mistake never tried anything new."
print(f"{author.title()} once said, \"{quote}\"")
# ANSWER: Albert Einstein once said, "A person who never made a mistake never tried anything new."

# REMOVING WHITESPACES, PREFIXES AND SUFFIX
favourite_language = " Python "
favourite_language = favourite_language.strip()
print(favourite_language)
# ANSWER: Python

nostarch_url = "https://www.nostarch.com/"
# Chaining methods to remove both prefix and suffix
print(nostarch_url.removeprefix("https://").removesuffix("/"))
# ANSWER: www.nostarch.com

# ADDING WHITESPACE TO STRINGS WITH TABS OR NEWLINES
print("\tPython") 
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
# ANSWER:
# Languages:
#     Python
#     C
#     JavaScript

# Avoiding Syntax error with Strings
# Incorrect usage of single quotes inside single quotes
message = 'One of Python's strengths is its diverse community.'
print(message)
# ANSWER: SyntaxError: invalid syntax (unterminated string literal)
# Fix: Use double quotes "Python's" or escape the character \'

# TRY IT YOURSELF (1)
person_1 = "eric"
print(f"Hello {person_1.title()}, would you like to learn some python today?")
# ANSWER: Hello Eric, would you like to learn some python today?

name_r = "rohit"
print(name_r.upper())
print(name_r.lower())
print(name_r.title())
# ANSWER: ROHIT, rohit, Rohit

# TRY IT YOURSELF (2)
Person_1 = " rohit "
Person_2 = " gurbaz "

# Using \n (newline) and \t (tab) with stripping
print(f"(1){Person_1.strip()}\n\t{Person_2.strip()}")
print(f"(2){Person_1.rstrip()}\n\t{Person_2.rstrip()}")
print(f"(3){Person_1.lstrip()}\n\t{Person_2.lstrip()}")

# Removing Suffixes
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
# ANSWER: python_notes
