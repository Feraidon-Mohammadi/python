import tkinter as tk

root = tk.Tk()

def on_button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

root.mainloop()



""" 
#insert value in form html
python_text = "Hello, this is some Python text!"
return render_template('index.html', python_text=python_text)

 """



""" second form -You can also use the +=, -=, *=, and /= operators to 
perform these operations in a shorthand way:  """


# Addition
result = 2
result += 3
print(result) # Output: 5

# Subtraction
result = 5
result -= 2
print(result) # Output: 3

# Multiplication
result = 2
result *= 3
print(result) # Output: 6

# Division
result = 6
result /= 2
print(result) # Output: 3.0

""" It's also possible to perform more complex mathematical operations using 
the math module or numpy package. They provide a wide range of mathematical 
functions such as trigonometric, logarithmic, and statistical functions, etc.

In case of complex mathematical operations, 
it's highly recommended to use these libraries to perform the calculations,
 as they are optimized for performance and may provide a more accurate result """
 
 
 
 
 
 
# """ some changes """
x = 2 + 2
y = 4 + 3
print("rechteck :", x * y)

print(2, 3, 5, 6, 7, 10, sep=" - ")  # seb : between of the words write - or any other word.

print(2, 3, 5, 6, 7, 10, end=" ending")  # end : what want we add  at end of my  print.

print(2, '\n', 5, '\n', 6, '\n', 7, '\n', 10, sep="#")  # schreiben im nächste satz.


# find ID 
# x = input("Enter Your Name: ")
# print("your name is:", x )
a=2
b=2
c=a
print(id(a))
print(id(b))
print(id(C))




""" ********************************************************************* """
#import data to data banke or database .

import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='username', password='password', host='host', database='database_name')

# Create a cursor
cursor = cnx.cursor()

# Prepare the data
data = ("John", "Doe", "john.doe@example.com")

# Execute the SQL statement
cursor.execute("INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)", data)

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()

""" ********************************************************************* """
#


# add css style for html .

html_style = """
button {
    background-color: blue;
    color: white;
    font-size: 18px;
    padding: 10px 20px;
}

button:hover {
    background-color: darkblue;
}


header {
    background-color: #4CAF50; /* Green */
    color: white;
    padding: 20px;
}

.header-content {
text-align: center;
}
  
header {
background-image: url('your-image-path.jpg');
background-size: cover;
background-repeat: no-repeat;
height: 200px;
}

"""





