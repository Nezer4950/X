count = 0
while (count<10):
    num=int(input("ENTER A NUMBER: "))
    if (num<0):
        break;
    else:
        count=count+1
print("COUNT OF POSITIVE NUMBERS IS", count)