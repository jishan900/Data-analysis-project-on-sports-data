import pickle
import time
from termcolor import colored

def change_pw():
    while True:
         = input('Set your password:\n')


        if new_password=="E":
            continue
        if new_password != input('Confirm password:\n'):
            print(colored('Both Passwords must be equal.','red'))
            continue
        pickle.dump(open('pw_file.p', 'wb'))
        print('Password successfully changed.')
        return new_password

failures=0
while True:
    try:
        password = 
    except:
        password = change_pw()

    enter_password= input('Enter the password. (Or enter "E" to exit.)\n')


    if  :
        while True:
            option = input('Enter "S" to show secret file, Enter "C" to change the password, Enter "L" to lock, Enter "E" to exit the programm.\n').upper()
            if option == "S":

            if option == "C":



            print(colored('No valid entry.', 'red'))
    else:
        print(colored('Wrong Password!', 'red'))


