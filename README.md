# 5G Hackathon Registration Form
## Project Overview
A Registration form which takes the input from the users and store in the database. Created with a help of **Python**, **Tkinter** and **MySQL**. Tkinter is the standard GUI
library for python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object- oriented interface to the Tk GUI toolkit.
MySQL is an relational database management system based on SQL - Strucutered Query Lnaguage. The application is used for a wide range of purposes, including data warehousing, e-commerce, and logging applications. The most common use for mysql however, is for the purpose of a web database. It can be used to store anything from a single record of information to an entire available products for an online store.

## Prerequistes
#### 1. [Python](https://www.python.org/downloads/)
#### 2. [MySQL](https://dev.mysql.com/downloads/)
**Make sure to click on python-connector installer while installing MySQL.**

**3. Pillow module**
```python
pip install Pillow
```

Tkinter will be installed automatically while installation process of python.

**Before running the code make sure to download the image from above and store in the same location as of the python file(or you can specify the path name in imag) .**


## Importing Modules
```python
from tkinter import *
```
To load the images we import python imaging library pillow
```python
from PIL import ImageTk, Image
```
import connector to make interaction with the database
```python
import mysql.connector
```
## Main Window
First, we should be explicitly creating the main window by using an instance of Tk. When we do this we can allocate a title to our window. After title creation we specify the size of our main window and i configured the window to white color which may not be necessary. 

**Image Display**
Displayed the image using **Label** 
*Label is tkinter widget which is used to display text or image.*
Image which i had loaded in the start of our program using
```python
imag = Image.open('new_bg.jpeg')
image1 = ImageTk.PhotoImage(imag)
```
has been placed onto this label widget (bg_label). We can specify the position of label using *grid or *place method in grid method we specify features like row,column similar to matrix and in place method we use positional features like x,y to place at more accurate place.

**Frame and It's Widgets**
A frame is a rectangular region on the screen. It is used as a foundation class to implement complex widgets. Can also be used to organize a group of widgets. Placed a frame besides image label on which i would be placing other widgets.

As said earlier a label is used to display text or image. So now i would be creating labels to place text onto the frame.
Created label's like
1. fullname
2. mail_id
3. Gender
4. Country
5. Phone Number

*Collecting User's data*
*Entry* is widget used to enter or display a single line text
So placed this entry widgets beside label widgets in frame

Entry widget's
1. fullname_entry -----------To get the fullname of user
2. email_entry    -----------To get email_id of user
3. idea_entry     -----------To get phone number of user

Other Widget's
1. RadioButtons   -----------To get gender of user
2. Combobox       -----------To select the country
3. Button         -----------To submit the form along with entry into the database.

**Extracting the information from Entry Widget**

Have placed few variables before every label widget in order to get the information from the Entry widget the type of the variable depends upon the information being extracted for string variable StrVar() has been used and for int variabel IntVar() has been used. 


#### Database
Button widget(submit) consists of an option(command) which defines what to do when an user clicks on it. So our next goal is to store the information into the database, so this command option is directed to a function (database() -- on top of the page) which consists of database username and password in order to insert this data into a database(registration) created to store the data.
Added some extra functionality's like when the user try's to submit the form without filling all the data a pop up appears insisting to fill the form.
      After submitting the form previous data is deleted from entry widget using Entry.delete(start, end) method.
