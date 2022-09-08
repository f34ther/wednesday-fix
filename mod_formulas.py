# ### 2) Create a Module in VS Code and Import It into jupyter notebook <br>
# <p><b>Module should have the following capabilities:</b><br><br>
# 1) Has a function to calculate the square footage of a house <br>
#     <b>Reminder of Formula: Length X Width == Area<b>
#         <hr>
# 2)<p> Has a function to calculate the circumference of a circle <br><br>
# <b>Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage</b>
# </p>

# enters = '\nEnter a number for length here '
# enter = '\nEnter a number for width here '

def area(l, w):
    length = '\nEnter a number for length here '
    width = '\nEnter a number for width here '
    l = int(input(length))
    w = int(input(width))
    return l*w


print(area(10, 11))


def cir(radius):
    radius = '\nEnter a number for radius here '
    r = int(input(radius))
    return 2*(3.1415926) * r


print(cir(0))
