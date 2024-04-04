import random

class Student:
    def __init__(self, name, age, year, grade):
        self.name = name
        self.age = age
        self.year = year
        self.grade = grade

    def get_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Курс: {self.year}, Середній бал: {self.grade}")

    def increase_year(self):
        self.year += 1

    def update_grade(self, new_grade):
        self.grade = (self.grade + new_grade) / 2

student1 = Student("Артем", 21, 2, 88)
student1.get_info() 
student1.increase_year()
student1.get_info() 

student1.update_grade(90)
student1.get_info()  

student2 = Student("Даніїл", 23, 2, 78)
student2.get_info() 
 
n_comp = random.randint(1, 100)
 
while True:
    n = int(input("ENTER NUMBER FROM 1 TO 100: "))
    if n==n_comp:
        print("YOU GUESSED IT!")
        break
    elif n>n_comp:
        print("YOU ENTERED MORE THAN THE COMPUTER REMEMBERED! TRY AGAIN!")
    elif n<n_comp:
        print("YOU ENTERED LESS THAN THE COMPUTER REMEMBERED! TRY AGAIN!")
        
print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}" )
f = open("a.txt", "w") 
f.write("Hello World") 
f.close() 

f = open("a.txt", "a") 
f.write("123") 
f.close() 

f = open("a.txt", "r")
print(f.read()) 
f.close()

import datetime
a = 0
log = open("b.txt", "w")
while a < 100:
    try: 
        print(100 / a)
        if a % 2 == 0:
            name += 5
    except ZeroDivisionError: 
        log.write(f"[{datetime.datetime.now()}] a = {a} - ZeroDivisionError\n") 
    except NameError: 
        log.write(f"[{datetime.datetime.now()}] a = {a} - NameError\n")
    else:
        log.write(f"[{datetime.datetime.now()}] a = {a} - no problems\n")
    a += 1
    if a == 100:
        break
    print(a)
else: 
    print("End")
