import random
import string
def ask_uppercase():
    print("DO YOU WANT UPPERCASE LETTERS IN YOUR PASSWORD? \n")
    ans=input("(YES/NO)")
    if ans == 'YES' or ans == 'yes' or ans == 'Yesy':
        return True
    else :
        return False
def ask_lowercase():
    print("DO YOU WANT LOWERCASE LETTERS IN YOUR PASSWORD? \n")
    ans=input("(YES/NO)")
    if ans == 'YES' or ans == 'yes' or ans == 'Yes':
        return True
    else :
        return False
def ask_number():
    print("DO YOU WANT NUMBERS IN YOUR PASSWORD? \n")
    ans=input("(YES/NO)")
    if ans == 'YES' or ans == 'yes':
        return True
    else :
        return False
def ask_special():
    print("DO YOU WANT SPECIAL SYMBOLS IN YOUR PASSWORD? \n")
    ans=input("(YES/NO)")
    if ans == 'YES' or ans == 'yes':
        return True
    else :
        return False

def generate_password(length,uppercase,lowercase,number,symbol):
    characters = ''
    if uppercase:
        characters = characters + string.ascii_uppercase
    if lowercase:
        characters = characters + string.ascii_lowercase
    if number:
        characters = characters + string.digits
    if symbol:
        characters = characters + string.punctuation
    if not characters:  
        return "No character types selected!"
    password = []
    if uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if number:
        password.append(random.choice(string.digits))
    if symbol:
        password.append(random.choice(string.punctuation))
    for i in range (length-len(password)):
        password.append(random.choice(characters))
    random.shuffle(password)
    return ''.join(password)
def main():
    print("WELCOME TO RANDOM PASSWORD GENERATOR\n")
    while True:
        try:
            length = int(input("HOW MUCH SHOULD BE THE LENGTH OF YOUR PASSWORD (MINIMUM 8 CHARACTERS): "))
            if length < 8:
                print("Password length must be atleast 8 characters, Please try again")
                continue
            break
        except ValueError:
            print("Enter a valid number")
    up=ask_uppercase()
    low=ask_lowercase()
    symbol=ask_special()
    num=ask_number()
    password=generate_password(length,up,low,num,symbol)
    print(password)
main()

