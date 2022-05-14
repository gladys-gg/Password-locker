import pyperclip
from user import User

class Credentials:
    """
    generates new instances of credentials
    """
                    
    credentials_list = []  #list of accounts a user may have
    

    def __init__(self, account,account_username,account_password):
        """
        helps define properties of our object self
        """

        self.account = account
        self.account_username = account_username
        self.account_password = account_password
        
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our users or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                    a_user == user.username
        return 
    
    def save_credential(self):

        '''
        save_account method saves account objects into credentials_list
        '''

        Credentials.credentials_list.append(self)


    def delete_credential(self):

        '''
        delete_account method deletes a saved account from the credentials_list
        '''

        Credentials.credentials_list.remove(self)
        

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the account list
        '''
        return cls.credentials_list

    @classmethod
    def find_credential(cls,account):
            """
            Method that takes in a username and returns a user that matches that number
            """
            for credential in cls.credentials_list:
                if credential.account== account:
                    return credential
                
    @classmethod
    def copy_credentials(cls,account):
        
        """
        a method that copies credentials info
        """	
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)
        
    @classmethod
    def credentials_exist(cls, account):
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
            return False