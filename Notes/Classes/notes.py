# Creating a class


class User:
    """A class to represent a user with followers and following attributes."""

    # Must be PascalCase to id and differentiate classes from other user_created variables.
    # Will be called everytime a new object is created, and has set default values upon creation.

    def __init__(self, user_id, username):
        """__init__ Initialize the user with an ID, username, and default follower/following counts.

        Args:
            user_id (str): The user's ID.
            username (str): The user's username.
        """

        # The below is creating default attributes for any object created on first run
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Generally the name of the attribute will be the name of the variable, not always
    # The __init__ function is called a constructor. Sets default values and creates

    # Calling a Method example
    def follow(self, user):
        """
        Follow another user, increasing their followers and this user's following count.

        Args:
            user (User): The user to follow.
        """
        # self is always included so the function knows the object that called it.
        user.followers += 1
        self.following += 1


# Create users
user_1 = User("001", "Angela")
user_2 = User("002", "Dorothy")

# User 1 follows User 2
user_1.follow(user_2)

# Print follower and following counts
print(user_1.followers)  # Output: 0
print(user_1.following)  # Output: 1
print(user_2.followers)  # Output: 1
print(user_2.following)  # Output: 0

# Relevant Notes
# user_1 = User() # user_1 item created from User() class
# user_1.id = "001" # Attribute created related to object
# user_1.username = "Angela - Second attribute created from object

# Repeating the above for, example a 100 different students is prone to error and tedious repetition.
# Constructors come into play when multiple objects are needed. Shown on line 4 and represented by "Class"
