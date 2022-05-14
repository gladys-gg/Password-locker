import string
import random
from xml.dom.minidom import CharacterData
from xml.dom.pulldom import CHARACTERS
import pyperclip
from re import T
from requests import delete

class User:
    '''
    class that generates new instances of user
    '''
    user_list = [] #an array to store a collection of users

    def __init__(self, first_name,last_name,username,password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
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
    def display_user(cls):
            """
            return information from the users list
            """
            return cls.user_list

    @classmethod
    def find_by_name(cls,username):
            """
            Method that takes in a username and returns a user that matches that number
            """
            for user in cls.user_list:
                if user.username == username:
                    return user

    @classmethod
    def user_exist(cls,username):
            for user in cls.user_list:
                if user.username == username:
                    return True
                return False


class Credentials:
    """
    generates new instances of credentials
    """
                    
    accounts = []  #list of accounts a user may have
    
    
    @classmethod
    def verify_user(cls,username,password):
        '''
        method to verify if the user exists
        '''
        is_user = ""
        for user in User.user_list:
            if(user.username ==username and user.password == password):
                is_user == user.username
            return is_user

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

    def password_generator(characters = string.ascii_letters + string.punctuation  + string.digits):
        gen_pass =  "".join(random.choice(CharacterData) for x in range(random.randint(8, 16)))
        return gen_pass


    @classmethod
    def display_accounts(cls):
            """
            return information from the users list
            """
            return cls.accounts

    @classmethod
    def find_by_name(cls,account_username):
            """
            Method that takes in a username and returns a user that matches that number
            """
            for account in cls.accounts:
                if account.account_username == account_username:
                    return account

    @classmethod
    def copy_account(cls,account_name):
        
        """
        a method that copies credentials info
        """	
        find_credential = Credentials.find_by_name(account_name)
        pyperclip.copy(find_credential.password)

    @classmethod
    def account_exist(cls, account_name):
        for account in cls.accounts:
            if account.account_name == account_name:
                return True
            return False
        
            



