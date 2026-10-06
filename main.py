# Imports and global info
import random
import pyperclip
passwords = {

}
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=~Gith"
response = "y"

while response != "n":
    if response == "y":
        # asks for website name
        website = input("What website is the password for? ", )

        # generates password and copies it to the clipboard
        random_letters = ""
        for i in range(8):
            random_letters += random.choice(letters)
        print(f"Here is your password for {website}: ", random_letters)
        pyperclip.copy(random_letters)
        print("Your password has been copied to the clipboard")
        passwords[website] = random_letters

        # shows all passwords
        print(" ")
        print("All passwords:")
        for x, y in passwords.items():
            print(x, ": ", y)
        # asks user if they want to enter another password
        response = input("Enter another password? (y/n): ", )
    elif response == "n":
        break
    else:
        print("That isn't a valid input, try again")
        response = input("Enter another password? (y/n): ", )