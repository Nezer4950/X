import random
 
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