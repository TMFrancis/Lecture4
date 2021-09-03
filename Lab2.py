# question 1
import turtle

def draw_square(t, sz):
     """Make turtle t draw a circle of sz."""
     for i in range(300):
         t.forward(sz)
         t.left(65)
         t.color('red')


wn = turtle.Screen()        # Set up the window and its attributes
wn.bgcolor("Yellow")
wn.title("Alex meets a function")

alex = turtle.Turtle()      # Create alex
draw_square(alex, 100)       # Call the function to draw the square   # the number is referring to the size of pixels(side of the shape)
wn.mainloop()


# question 2
for i in range(0,100):
    if i % 2:
        print ("win")
    else:
        print ("lose")

# question 3
import os

path = "/Users/tomfrancis/Documents/"

# Change the directory
os.chdir(path)

# Read text File

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

lstd = os.listdir (path)
print (lstd)

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        print ('The file is found at the following directory:')
        print (file_path)
        # call read text file function
        read_text_file(file_path)

# Question 4
import math
xx = math.sqrt(14)
print(xx)

# Question 5
# non-code answer.

