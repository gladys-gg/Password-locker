class User:
    '''
    class that generates new instances of user
    '''

    def __init__(self, user_name,password):
        self.user_name = user_name
        self.password = password
        
        def save_user(self):
            """
            save a new user object
            """

            user_list = [] #an array to store a collection of users

            User.user_list.append(self)  #add new users to the user list