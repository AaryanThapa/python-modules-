list = [int,float,34,56,7,87,89,34,0,1,2,3,4]
for item in list:
    if str(item).isnumeric() and item>7:
        print(item)