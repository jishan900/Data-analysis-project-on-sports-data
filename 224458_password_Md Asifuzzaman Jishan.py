import pickle
import time
from termcolor import colored

def change_pw():
    while True:
        new_password = input('Please set your password: \n')
        if len(new_password) < 10:
            print('Password has to have minimum 10 character.')
            continue
        else:
            print('Congratulations!')
        if new_password=="E":
            continue
        if new_password != input('Confirm password: \n'):
            print(colored('Passwords must be equal to the previous password.','red'))
            continue
        pickle.dump(new_password, open(r'C:\Users\Jishan\OneDrive - Technische Universität Dortmund\Desktop\Final Assignment\pw_file.p', 'wb'))
        print('Password successfully changed.')
        return new_password

failures=0
exit_flag = False

while True:
    try:
        password = pickle.load(open(r'C:\Users\Jishan\OneDrive - Technische Universität Dortmund\Desktop\Final Assignment\pw_file.p', 'rb') )
    except:
        password = change_pw()

    enter_password= input('Enter the password. (Or enter "E" to exit.)\n')


    if enter_password == password:
        while True:
            option = input('Enter "P" to show secret file, Enter "C" to change the password, Enter "L" to lock, Enter "E" to exit the programm.\n').upper()
            
            if option == "P": 
                secret_file = open(r'C:\Users\Jishan\OneDrive - Technische Universität Dortmund\Desktop\Final Assignment\password-20221001\secret_file.txt', 'r', encoding='utf8')
                secret_file_content = secret_file.read()
                print(secret_file_content)
                secret_file.close()
                continue

            if option == "C":
                password = change_pw()

            if option == "L":
                break
                
            if option == "E":
                exit_flag = True
                break                   
                            
            print(colored('No valid not detected', 'red'))
        if exit_flag :
            break
    
    elif enter_password == "E":
        break        
    else:
        failures += 1
        if failures == 6:
            time.sleep(10)
            failures = 0
        print(colored('Wrong Password!', 'red'))