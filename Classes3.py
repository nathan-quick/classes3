class Student:
    def __init__(self, ID, FirstName, LastName, CreditsAccomplished, GPA):
        self.__ID = ID
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__CreditsAccomplished = CreditsAccomplished
        self.__GPA = GPA
    
    def print_headers(self, headers):
        for h in headers:
            print(h)
    
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

with open('CPTR226-HW25-Data.csv', newline='') as csvfile:
    for l in csvfile:
        print(l)
