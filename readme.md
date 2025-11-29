# Password Generator

Generate pseudo-random passwords instantly and copy them to your clipboard!

## Description

This app uses two Python modules to generate and keep track of passwords. Simply enter in a website or app name and a password is generated and copied to the clipboard. At the end, all passwords are conveniently displayed.  

## Getting Started

### Dependencies

* python
* random, pyperclip modules

### Installing

* Fork this repo to create your own copy. 
* It is recommended to create a python virtual environment:
```sh
pipenv shell
```
* Install the required modules with pip:
```sh
pip install [moduleName]
```

### Executing program

1. In your IDE, make sure you are in the project folder.
2. Activate your virtual environment if you have created one:
```sh
pipenv shell
```
3. Run the program by typing:
```sh
python [filename].py
```

## Sample Run
```
🔒 Welcome to Password Generator 🔒

What website is the password for? GitHub
Here is your password for GitHub: $6E?"l,h_:[4
Your password has been copied to the clipboard!

Press enter to continue...

All passwords:
GitHub: $6E?"l,h_:[4

Enter another password? (y/n): y
What website is the password for? gmail
Here is your password for gmail: Jbu)_F"Wl[q>
Your password has been copied to the clipboard!

Press enter to continue...

All passwords:
GitHub: $6E?"l,h_:[4
gmail: Jbu)_F"Wl[q>

Enter another password? (y/n): gsmlkd
'gsmlkd' is not a valid yes/no response.

Enter another password? (y/n): n

All passwords:
GitHub: $6E?"l,h_:[4
gmail: Jbu)_F"Wl[q>

Have a nice day!
```

## Authors

[sp1dev | GitHub](https://github.com/sp1dev)

## Acknowledgments

* [Automate the Boring Stuff](https://automatetheboringstuff.com/)
* [W3Schools](https://www.w3schools.com/python/default.asp)

## Pseudocode example
```py
# imports go up here

# characters to choose from for password

# dictionary to save passwords


# program loop


    # ask user for website


    # generate random password using a for-loop

    
    # show password

    
    # save password to dictionary

    
    # copy password to clipboard


    # reset password string

    
    # print all passwords


    
    # ask user if they want to enter another password



# print passwords one last time

```