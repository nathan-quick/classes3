# classes3
For a group classes assignment
Student class

Create a class called Student that has an attribute (local class variable) for each CSV column value. 
Make the constructor (__init__) take the values as arguments and set them for the class. 
Make a print_headers() method to print a header for the columns
Override the __str__ method to print out the attributes in a nice looking way that matches the print_header() headers
Make getter methods for all the attributes.

Students class

Create a second class called Students
It should take a CSV filename in its __init__ for a file like you are given for this project
It should have an attribute which is a list of Students filled from the CSV file
It should have a method to print a nicely formatted table (override the __str__ method) of the contents of its list of students. This can use the Student methods to do this.
It should have methods freshman, sophomore, junior, and senior that each return the IDs as a tuple of the students that match the requirements for each class standing as outlined in the current Union College Bulletin.
