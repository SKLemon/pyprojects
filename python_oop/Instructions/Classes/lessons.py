# Creating a class


class User:  # Must be PascalCase to id and differentiate classes from other user_created variables.
    # This is to initialize the function with starting values. The code inside this will be called everytime a new object is created.
    def __init__(self, user_id, username):
        self.id = user_id  # The below is creating default attributes for any object created on first run
        self.username = username
        self.followers = 0
        self.following = 0

    # Generally the name of the attribute will be the name of the variable, not always
    # The __init__ function is called a constructor. Sets default values and creates

    # Calling a Method example
    def follow(
        self, user
    ):  # Creating a function to follow users. self is always included so the function knows the object that called it.
        user.followers += 1
        self.following += 1


user_1 = User(
    "001", "Angela"
)  # Created a user with default users from the Class above.
user_2 = User("002", "Dorothy")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# Relevant Notes
# user_1 = User() # user_1 item created from User() class
# user_1.id = "001" # Attribute created related to object
# user_1.username = "Angela - Second attribute created from object

# Repeating the above for, example a 100 different students is prone to error and tedious repetition.
# Constructors come into play. Shown on line 3.
