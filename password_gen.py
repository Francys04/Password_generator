"""Generating random characters"""
import random
"""For all characters""" 
import string

"""store the sets of ASCII letters, digits (0-9), and special characters, respectively."""
def generate_password(min_lenght, numbers=True, special_characters=True):
    letters = string.ascii_letters #The minimum length of the password to be generated.
    digits = string.digits #A boolean flag to indicate whether numbers should be included in the generated password (default is True).
    special = string.punctuation #A boolean flag to indicate whether special characters should be included in 
    #the generated password (default is True).

    """print(letters, special, digits) and combine in list"""
    
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = "" #store the generated password
    
    """Include just number or special char or all of this"""
    """track whether the generated password meets the specified criteria."""
    meets_criteria = False
    has_number = False
    has_special = False
    
    """This while loop generates the password character by character using the 
    random.choice() function to select a random character from the characters set and adds it to the pwd string."""
    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
            # if do not have any criteria , will be false
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


"""Call the func and generate_password(10, True, False)"""

min_lenght = int(input("Enter the minimum lenght: "))
has_number = input("Do you want to have numbers (y/n)?: ").lower() == "y"
has_special = input("Do you want to have special char (y/n)?: ").lower() == "y"
pwd = generate_password(min_lenght, has_number, has_special)

print("The generate password is: ", pwd)
