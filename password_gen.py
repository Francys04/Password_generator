import random
# for all characters 
import string


def generate_password(min_lenght, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # print(letters, special, digits)
    # combine in list
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    # include just number or special char or all of this
    meets_criteria = False
    has_number = False
    has_special = False

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


# call the func
# generate_password(10, True, False)

min_lenght = int(input("Enter the minimum lenght: "))
has_number = input("Do you want to have numbers (y/n)?: ").lower() == "y"
has_special = input("Do you want to have special char (y/n)?: ").lower() == "y"
pwd = generate_password(min_lenght, has_number, has_special)

print("The generate password is: ", pwd)
