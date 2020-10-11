import csv


class Student:
    def __init__(self, ID, FirstName, LastName, CreditsAccomplished, GPA):
        self.__ID = ID
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__CreditsAccomplished = CreditsAccomplished
        self.__GPA = GPA

    def __str__(self):
        out_str = f'{self.__ID}, {self.__FirstName}, {self.__LastName}, {self.__CreditsAccomplished}, {self.__GPA}'
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


s1 = Student(1123, 'Nathan', 'Quick', 17, 4.0)
print(s1)
s1.print_headers()
