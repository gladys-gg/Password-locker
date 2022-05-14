from user import Credentials, User


def create_user(first_name,last_name,username,password):
    '''
    function to create a new user
    '''
    new_user = User(first_name, last_name, username,password)
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
    return User.find_by_number(username)



def user_exist(username,password):
    exist_user = User.user_exist(username,password)
    return exist_user

#creating the credentials for the given accounts
def create_new_account(account_username, account_name, account_password):
    new_account = Credentials(account_username, account_name, account_password)
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
    credentials.delete_account()

def find_account(account_name):
    
    '''finds an account by the name'''
    return credentials.find_credential(account_name)


def copy_account():
    '''a function that copies another account credentials'''
    return Credentials.copy_account()

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


        elif short_code == 'lg':
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
                account_name = input("Enter the account name:-")
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

                    save_account(create_account(account_username, account_name, account_password))
                    print('\n')
                    print(f"Account created: ACcount Name: {account_name} Account Username: {account_username} Password: {account_password}")
                    
            elif short_code == 'dc':
                    print("Hi there:")
                    if display_accounts(username):
                        print("here is a list of all your accounts")
                        print("+"*40)
                        for credentials in display_accounts(username):
                            print(f"Account Name : {account_name} Account Username : {account_username} Account Password : {account_password}") 
                            print("-"*30)
                    else:
                        print("-"*30)
                        print("No user found. No credentials saved")
                        print("*"*30)
            elif short_code =='cp':
                print('\n')
                choose_account = input("Enter the account name to copy:-")
                copy_account(choose_account)
                print('\n')

            else:
                print("Wrong option. Choose again.")
            else:
                print('\n')
                print("Wrong details entered. Choose again or create an account")

        else:
            print("*"*50)
            print("Wrong option . Choose again")


if __name__ == '__main__':
    main()







