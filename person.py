from datetime import date
from datetime import datetime

class Person:
    '''Defines a person'''

    def __init__(self, firstname, surname, dob):
        '''Assigns instance variables for later use'''

        self.firstname = firstname
        self.surname = surname
        self.dob = datetime.strptime(dob, '%b %d %Y').date()
        self.age = self.calculate_age(self.dob)

    def calculate_age(self, born):
        '''Calculates age from date of birth'''
        
        self.__today = date.today()
        self.__years_difference = self.__today.year - born.year
        self.__is_before_birthday = (self.__today.month, self.__today.day) < (born.month, born.day)
        self.__elapsed_years = self.__years_difference - int(self.__is_before_birthday)
        return self.__elapsed_years
    
