# Swades Enterprises Portal

Swades Enterprises Portal is a menu‑driven Python console application that to view GST statistics, generate a GST invoice, celebrate their anniversary lucky Prize Winner form their customers list and add basic sales records.

# Features

Dashboard with 5 main options:
  View GST information (prices, GST percentages, GST rates)
  Generate a GST invoice in a formatted text layout
  Anniversary special: randomly pick a customer name for Lucky Prize Winner
  Enter more sales information
  Exit the portal
Uses basic statistics (max, min, mean, sum, mode) on existing sales data.
Simple, fully terminal‑based UI using Python’s input() and print().

# Project Structure

text

Data.py          # Contains Info list with existing records (dictionary)
main.py          # Somika Enterprises Portal 
README.md        # Project documentation

# Requirements

1) Python 3.8 or higher
2) Standard library modules only:
                statistics
                random
3) A Data.py file that defines Info, typically a list of dictionaries, for example:
Info = [{"Name": "Customer 1","Product": "HP Omnibook","Price": 86100,"GST_P": 18,"GST_R": 18900}]

# How to Run

1) Download this project folder.
2) Make sure Data.py is in the same folder i.e. in project folder.
3) Open a terminal in the project directory.
4) Run:

# How to Use

After running the script, the portal header is displayed and you see the dashboard :

1. GST Information
   Choose:
      1 for Sale Price statistics
      2 for GST Percentage statistics
      3 for GST Rate statistics
    Then choose:
      Highest value
      Lowest value
      Average (for prices)
      Total (sum)
      Most frequent value (mode)

2. GST Invoice Generator 
    Enter:
      Enterprise name and address
      Shipping address
      Product description, quantity, rate, GST amount, GST percentage
      The program prints a nicely formatted invoice in the console.

3. Anniversary Special
     Randomly selects and prints a customer name from info for Lucky Prize Winner

4. Enter More Information
    Enter:
       Customer name
       Product sold
       Sale price
       GST percentage and GST rate
    The new record is appended to info during that run.

5. Exit
     Just stops the program.

# Author
      Krishna Maheshwari
      CSE(AI and ML) Student
      VIT Bhopal 

