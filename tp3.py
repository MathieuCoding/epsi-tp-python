# Exo 1
# def nb_figures_square(number):
#     return len(str(number ** 2))
#
# print(nb_figures_square(int(input("Enter a number: "))))

# Exo 2
# def is_prime(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
#
# print(is_prime(int(input("Enter a number: "))))

# Exo 3
# def display_prime_numbers(number):
#     for i in range(2, number + 1):
#         if is_prime(i):
#             print(i)
#
# print(display_prime_numbers(int(input("Enter a number: "))))

# Exo class
import re

class Date:
    def __init__(self, day = 1, month = 1, year = 1970):
        self.day = day
        self.month = month
        self.year = year

    def to_string(self):
        return print(str(self.day) + "/" + str(self.month) + "/" + str(self.year))

def add_date():
    date = Date()
    re_year = "^\d{4}$"
    re_month = "^\d{2}$"
    re_day = "^\d{1,2}$"

    year = input("Enter a year: ")
    month = input("Enter a month: ")
    day = input("Enter a day: ")
    if re.search(re_year, year) is None or re.search(re_month, month) is None or re.search(re_day, day) is None:
        print("Date is not valid")
    else:
        date.year = year
        date.month = month
        date.day = day

    date.to_string()
    return date

add_date()


class Person:
    def __init__(self, first_name, last_name, date_of_birth, start_date):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.start_date = start_date

    def to_string(self):
        print("Person: " + self.first_name + " " + self.last_name)
        print("Date of birth: ")
        self.date_of_birth.to_string()
        print("Start date: ")
        self.start_date.to_string()

def add_person():
    person = Person(first_name = input("Enter a first name: "), last_name = input("Enter a last name: "), date_of_birth = add_date(), start_date = add_date())

    person.to_string()
    return person

# add_person()

def is_more_recent_than(date1, date2):
    if date1.year > date2.year:
        return True
    elif date1.year == date2.year:
        if date1.month > date2.month:
            return True
        elif date1.month == date2.month:
            if date1.day > date2.day:
                return True
    return False

def compare_seniority(person1, person2):
    person1.to_string()
    if is_more_recent_than(person1.start_date, person2.start_date):
        print(" is more senior than ")
    else:
        print(" is more senior than ")
    person2.to_string()