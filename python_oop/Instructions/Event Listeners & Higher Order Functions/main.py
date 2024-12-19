# Event Listeners #
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()  # This allows the module to listen for events/actions to occur. Bindings are needed after this line of code, usually in the form of a function that is activated.
screen.onkey(
    key="space",
    fun=move_forwards,  # Best practice is to use keyword arguments instread of positional arguments
)  # This line binds the spacebar to activate the move_forwards function everytime you press the spacebar.

# Higher Order Functions #

"""

What we have with the above is a function that is being used as an input. For example, method (a function in a class) "screen.onkey" takes an input, whereas move_forwards does something.
We can pass move_forwards into screen.onkey.

Ex)
In our calculator.py file, we had multiple functions (add, multiply, divide functions etc).
Each of those functions did a specific task related to its name.
The below function allows us pass in the specific function to call the specific task (add, divide, multiply).
This new function is in place of "func", then returns the same func and passes in n1, and n2.

# Creating the function

def calculator (n1,n2,func)
    return func(n1,n2)

# Calling the functions.

calculator(2, 3, add) # This will result in "5", as we have passed the "add" function into this, along with the numbers.
calculator(2, 3, multiply) # This will result in "6", as we have passsed the multiply function.

Python is one of the languages where higher order functions are commonly used. Some languages do not allow this.

"""

screen.exitonclick()
