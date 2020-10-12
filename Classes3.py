#!/var/env python3
#
# Classes3.py
#
# This file serves as an example of how to use classes
#
# Author: Nathan Quick and Jared Schiavone
# Date: 2020 October 12
# Version: 1.0
# Course: CPTR 226
# Assignment: Classes Part 3
"""This is a description of the file that shows up in the docstring
   documentation methods.
"""

# Includes
import argparse
import doctest
import csv

# Global Variables


# Functions
class Student:
    def __init__(self, ID, FirstName, LastName, CreditsAccomplished, GPA):
        self.__ID = ID
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__CreditsAccomplished = CreditsAccomplished
        self.__GPA = GPA

    def __str__(self):
        # I don't know how to get this line shorter without breaking it
        out_str = (f"{self.__ID}, {self.__FirstName}, {self.__LastName}, {self.__CreditsAccomplished}, {self.__GPA}")
        return out_str

    def print_headers(self):
        print("ID, FirstName, LastName, CreditsAccomplished, GPA")

    # stores all values in a dictionary for them to be called by value
    # this way I did not need to make a new get for every value
    def get_student(self, value):
        stats = {
            'ID': self.__ID,
            'FirstName': self.__FirstName,
            'LastName': self.__LastName,
            'Credits': self.__CreditsAccomplished,
            'GPA': self.__GPA
        }
        return stats[value]


class Students:
    def __init__(self, studentsFilename):
        self.__StudentsFilename = studentsFilename
        self.__StudentsList = []
        self.__StudentsDictList = []

    def get_students(self):
        with open(self.__StudentsFilename, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)

            # headers = csvreader.__next__()
            # self.print_headers(headers)

            for row in csvreader:
                # create new student
                student = Student(row['ID'], row['FirstName'], row['LastName'],
                                  row['CreditsAccomplished'], row['GPA'])
                # append student to list
                print(student.get_student('FirstName'))
                self.__StudentsList.append(student)
                self.__StudentsDictList.append(row)

    def write_all_students(self):
        with open('out.csv', 'w') as csvfile:
            csvwriter = csv.DictWriter(csvfile, ['ID', 'FirstName', 'LastName',
                                                 'CreditsAccomplished', 'GPA'])
            csvwriter.writeheader()
            csvwriter.writerows(self.__StudentsDictList)

    def print_headers(self, headers):
        for h in headers:
            print(h)

    def printStudent(self):
        print(self.__StudentsFilename)


# This runs if the file is run as a script vs included as a module
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--doctest', action='store_true',
                        help='Pass this flag to run doctest on the script')
    args = parser.parse_args()  # parse the arguments from the commandline

    if(args.doctest):
        doctest.testmod(verbose=True)  # run the tests in verbose mode

    print("------------------")
    s1 = Students('CPTR226-HW25-Data.csv')
    s1.printStudent()
    s1.get_students()
    s1.write_all_students()
