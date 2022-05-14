import pyperclip


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
    def find_user(cls,username):
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



