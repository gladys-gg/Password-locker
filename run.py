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
    return user.display_user()   
    
    
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
def create_new_credential(account, account_username, account_password):
    new_account = Credentials(account, account_username, account_password)
    return new_account



def save_credential(credentials):
    
    credentials.save_credential()
    

def display_credentials():
    '''returns all the saved credentials'''
    return credentials.display_credentials

def password_generator():
    
    ''' generates a password '''
    gen_pass = Credentials.password_generator()
    return gen_pass


def delete_credential(credentials):
    '''delete an account from the list'''
    return credentials.delete_credential()

def find_credential(account):
    
    '''finds an account by the name'''
    return credentials.find_credential(account)


def copy_account():
    '''a function that copies another account credentials'''
    return Credentials.copy_credentials()

def main():
    print('Welcome to password locker. This is an application that will allows you to keep track of your passwords without having to memorize them.')
    print('/n')
    print("Select a short code to navigate through: To create a new user use 'cu': To login use 'lg' or 'ex to exit")
    short_code = input().lower()
    print('\n')
    if short_code == 'cu':
        print("Create Account")
        print("-"*10)
        print('Type in your username: ')
        username = input()
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
        if login_user == 'login':
            print(f"Hello {username}. Welcome to password locker")
            print('.'*50)
        while True:
            print("Navigation codes: \n cc-Create a credential \n dc-Display Credentials \n sa- Find credentials\n cp-Copy Password \n ex-Exit:")
            if short_code =='cc':
                print('Welcome and create a new credential')
                print('*'*30)
                print('Account name:')
                account = input().lower()
                print('Type in your account username: ')
                account_username = input()
                while True:
                    print('Type in your password:')
                    password = input()
                    break
                else:
                    print('Invalid password')
            save_credential(create_new_credential(account,account_username,account_password))
            print('*'*30)
            print('Account credential for {account} created. Username is {account_username} and password is {account_password}')
            print('*'*30)
    elif short_code =='dc':
        if display_credentials():
            print("Here is a list of all your credentials")
            print('\n')
            for account in display_credentials():
                print(f'Account: {credentials.account} \n {credentials.account_username} \n {credentials.account_password}')
                print('*'*30)
            else:
                print('There are no credentials saved yet.')
                print('*'*30)
        elif short_code =='sa':
            print('Enter the account name:')
            print('*'*30)
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print('*'*30)
                print(f"Account Name : {search_credential.account}")
                print('*'*30)
                print(f"Account Username : {search_credential.account_username}")
                print('*'*30)
            else:
                print('Credential not found')
                print('\n')
        elif short_code =='de':
            print('Enter the account name to proceed')
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)    
                print('*'*30)
                search_credential.delete_credential()
                print('\n')
                print(f'{search_credential.account} deleted successfully.')
                print('\n')
            else:
                print('Failed. Credential not found.')
    elif short_code =='ex':
        print(f'Goodbye {username} ,Exiting the password locker application')
    else:
        print('Invalid choice')

if __name__ == '__main__':
    main()







