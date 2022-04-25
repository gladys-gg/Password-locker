
from user import Credentials, User


def create_user(first_name,last_name,user_name,password):
    newuser = User(first_name, last_name, user_name,password)
    return newuser

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def find_user(username):
    return User.find_by_number(username)

def display_users():
    return User.display_users()

def login_user(username,password):
    exist_user = User.user_exist(username,password)
    return exist_user


def create_account(account_username, account_name, account_password):
    newaccount = Credentials(account_username, account_name, account_password)
    return newaccount



def save_account(user):
    Credentials.save_account()

def delete_account(user):
    Credentials.delete_account()

def find_account(account_name):
    return Credentials.find_by_number(account_name)

def display_accounts():
    return Credentials.display_accounts()

def main():
    while True:
        print("Welcome to password locker")
        print('\n')
        print("Select a short code to navigate through: To create a new user use 'cu': To login use 'lg' or 'ex to exit")
        short_code = input().lower()
        print('\n')

        if short_code == 'cu':
            print("Create Account")
            print("-"*10)

            print ("First name ....")
            first_name = input()

            print("Last name ...")
            last_name = input()

            print("Create your username")
            user_name = input()

            print("Create password")
            password = input()

            print("confirm password")
            confirm_password = input()

            while confirm_password != password:
                print("Password did not match")
                print("Enter the password")
                password = input()
                print("Confirm the password")
                confirm_password = input()

            else:
                
                save_user(create_user(first_name,last_name,user_name,password)) # create and save new contact.
                print ('\n')
                print(f"Congratulations New User {first_name} {last_name} created successfully")
                print ('\n')
                print("Proceed to login")
                print("Enter your username: ")
                user_name = input()
                print("Enter your password: ")
                password = input()

            while user_name != user_name:
                print("Invalid Username or Password!!")
                print("Username: ")
                user_name = input()
                print("Enter the password")
                password = input()
                print("Logged in successfully")


        elif short_code == 'lg':
            print("Welcome")
            print("Kindly input your username: ")
            user_name = input()
    
            print("Enter your password: ")
            password = input()
            print('\n')

            print("Login successful")
            print('\n')
            print('\n')

        elif short_code == 'ex':
            break
        else:
            print("Enter valid code to continue")

if __name__ == '__main__':
    main()







