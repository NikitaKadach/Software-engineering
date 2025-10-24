x1 = int(input("Enter x1"))
y1 = int(input("Enter y2"))
x2 = int(input("Enter x2"))
y2 = int(input("Enter y2"))
if (x1>0 and y1>0 and x2>0 and y2>0): 
    print('yes I')
elif (x1<0 and y1>0 and x2<0 and y2>0):  
    print('yes II')
elif (x1<0 and y1<0 and x2<0 and y2<0): 
    print('yes III')
elif (x1>0 and y1<0 and x2>0 and y2<0): 
    print('yes IV')
elif (x1==0 or y2==0 or x2==0 or y1==0):
    print('delete zero')
else: 

     print('nope')
