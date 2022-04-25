
from re import T
from requests import delete

class User:
    '''
    class that generates new instances of user
    '''
    user_list = [] #an array to store a collection of users

    def __init__(self, first_name,last_name,user_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        
    def save_user(self):
            """
            save a new user object in our user list
            """
            User.user_list.append(self)  #add new users to the user list
        
    def delete_user(self):
            """
            deletes a saved user from the list
            """
            User.user_list.remove(self)

    

    @classmethod
    def display_users(cls):
            """
            return information from the users list
            """
            return cls.user_list

    @classmethod
    def find_by_number(cls,number):
            """
            Method that takes in a username and returns a user that matches that number
            """
            for user in cls.user_list:
                if user.user_name == number:
                    return user

    @classmethod
    def user_exist(cls,number):
            for user in cls.user_list:
                if user.user_name == number:
                    return True
                    return False


class Credentials:
    """
    generates new instances of credentials
    """
                    
    accounts = []  #list of accounts a user may have

    def __init__(self, account_username,account_name,account_password):
        """
        helps define properties of our object self
        """

        self.account_username = account_username
        self.account_name = account_name
        self.account_password = account_password

    def save_account(self):
        """
        save user information into the accounts
        """

        Credentials.accounts.append(self)

    def delete_account(self):
        """
        delete a saved credential from ana account
        """
        Credentials.accounts.remove(self)

    @classmethod
    def display_accounts(cls):
            """
            return information from the users list
            """
            return cls.accounts

    @classmethod
    def find_by_number(cls,number):
            """
            Method that takes in a username and returns a user that matches that number
            """
            for account in cls.accounts:
                if account.account_username == number:
                    return account


