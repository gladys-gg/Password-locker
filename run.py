from user import Credentials, User


def create_user(first_name,last_name,user_name,password):
    newuser = User(first_name, last_name, user_name,password)
    return newuser

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def find_user(number):
    return User.find_by_number(number)

def display_users():
    return User.display_users()


def create_account(account_username, account_name, account_password):
    newaccount = Credentials(account_username, account_name, account_password)
    return newaccount