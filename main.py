l = [65, 785, 34, 765, 3]

print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}" )

f = open("test.txt", "w")
f.write("Hello World")
f.close()

f = open("test.txt", "a")
f.write("123") 
f.close() 

f = open("test.txt", "r")
print(f.read())
f.close()

import datetime
a = 0
log = open("log.txt", "w")
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