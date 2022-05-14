import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    test class that defines test cases for the user class behaviours.
    ARgs:
    unittest.Testcase: testcase that helps in creating test cases
    """

def setUp(self):
    """
    set up method to run before each test cases
    """
    self.newuser = User('gmwangi','g2022')

def test_init(self):
    """
    test_init test case to test if the object is initialized properly
    """
    self.assertEqual(self.newuser.user_name,"gmwangi")

    self.assertEqual(self.newuser.password,"g2022")

def test_save_user(self):
    """
    to test wether the user object is saved into the user list
    """

    self.newuser.save_user()
    self.assertEqual(len(User.user_list),1)

def test_delete_user(self):
    """
    to check whether we can delete a user from our list
    """

    self.newuser.save_user()
    test_user = User('tuser','2019')
    test_user.save_user()

    self.newuser.delete_user()
    self.assertEqual(len(User.user_list),1)

if __name__ =='__main__':
    unittest.main()
