#!/usr/bin/env python3.9

from user import User
from credentials import Credentials


def create_user(username,password):
    '''
    function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    function to save a new user
    '''
    user.save_user()

def delete_user(user):
    '''
    function to delete a new user
    '''
    user.delete_user()

def display_user():
    '''
    function to display existing user
    
    '''
    return User.display_user()   
    
    
def login_user(username,password):
    '''
    function that checks whether the user exists then logs the user in 
    '''
    check_user = Credentials.verify_user(username,password)
    return check_user


def find_user(username):
    return User.find_user(username)



def user_exist(username,password):
    
    return user

#creating the credentials for the given accounts
def create_new_account(account, account_username, account_password):
    new_account = Credentials(account, account_username, account_password)
    return new_account



def save_account(credentials):
    
    credentials.save_account()
    

def display_accounts():
    '''returns all the saved credentials'''
    return credentials.display_accounts

def password_generator():
    
    ''' generates a password '''
    gen_pass = Credentials.password_generator()
    return gen_pass


def delete_account(credentials):
    '''delete an account from the list'''
    return credentials.delete_account()

def find_crredential(account):
    
    '''finds an account by the name'''
    return credentials.find_credential(account)


def copy_account():
    '''a function that copies another account credentials'''
    return Credentials.copy_credentials()

def main():
    print("Hello, Welcome to password locker. What is your name?")
    username = input()
    print('Welcome {username} to password locker. This is an application that will allows you to keep track of your passwords without having to memorize them.')
    print('/n')
    print("Select a short code to navigate through: To create a new user use 'cu': To login use 'lg' or 'ex to exit")
    short_code = input().lower()
        print('\n')
        if short_code == 'cu':
            print("Create Account")
            print("-"*10)
            username = input('Type in your username: ')
            while True:
                print("reply with 'ip' to input your password.")
                password_choice = input().lower().strip()
                if password_choice =='ip':
                    password = input('Enter your password: ')
                    break
                else:
                    print('Invalid password')
            save_user(create_user(username,password))
            print('-'*30)
            print('Congratulations {username}. Your account created successfully.')
            print('*'*30)
            
        elif short_code == 'lg':
            print('*'*30)
            print('Enter your username and password to login:')
            print('*'*30)
            username = input('Type in your username: ')
            password = input('Type in your password: ')
            login = login_user(username,password)
            
                

                print("Invalid password.")
                
                save_user(create_user(first_name,last_name,username,password)) # create and save new contact.
                print ('\n')
                print(f"Congratulations New User {first_name} {last_name} created successfully")
                print ('\n')
                print("Proceed to login")
                print("Enter your username: ")
                username = input()
                print("Enter your password: ")
                password = input()

            while username != username:
                print("Invalid Username or Password!!")
                print("Username: ")
                username = input()
                print("Enter the password")
                password = input()
                print("Logged in successfully")
        elif short_code =='lg':
            print("Welcome. To login enter your account details:-")
            print("Kindly input your username: ")
            username = input()
            password = str(input("Enter your password:-"))
            print('\n')
            login = login_user(username,password)
            if login_user == login:
                print(f"Hello {username}.Welcome To Password Locker")  
                print('\n')
                while True:
                    print("*"*30)
                    print('\n')
                    print("Navigation codes: \n cc-Create a credential \n dc-Display Credentials \n cp-Copy Password \n ex-Exit:")
                    short_code = input('Enter a choice: ').lower().strip()
                    if short_code =='ex':
                        print(f"goodbye {username}")
                        break
        elif short_code == 'cc':
            print("*"*60)
            print('Enter your account details:-')
            account = input("Enter the account name:-")
            account_username = input("Enter your account\'s username:-")
            while True:
                print("+"*30)
                print("Please choose an option of the password. \n ep-enter existing password \n pg-password generate \n ex-exit")
                password_choice = input("Enter an option to continue:-").lower()
                if password_choice =='ep':
                    print('\n')
                    account_password = input("Enter your password:")
                    break
                                
                elif password_choice =='pg':
                    account_password = password_generator()
                    break
                    
                elif password_choice =='ex':
                    print("You are exiting")
                    break 
                else:
                    print("Wrong option entered. Try again.")
                    save_account(create_account(account, account_name, account_password))
                    print('\n')
                    print(f"Account created: ACcount Name: {account} Account Username: {account_username} Password: {account_password}")
        elif short_code =='dc':
            print("Hi there:")
            if display_accounts(username):
                print("here is a list of all your accounts")
                print("+"*40)
                for credentials in display_accounts(username):
                    print(f"Account Name : {account} Account Username : {account_username} Account Password : {account_password}")
                    print("-"*30)
                else:
                    print("-"*30)
        elif short_code =='cp':
            print('\n')
            choose_account = input("Enter the account name to copy:-")
            copy_account(choose_account)
            print('/n')
            break
        
        else:
            print("Wrong details entered. Choose again or create an account")


if __name__ == '__main__':
    main()







