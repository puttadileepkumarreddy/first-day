string=int(input("enter the no of words:"))
b=[]
for i in range (string):
    c=input("enter the words:")
    b.append(c)
print("list of words:",b)
c=input("enter the choice(a/d):")
if c=="a":
    print("ascending order:")
    b.sort()
    print(b)
elif c=="d":
    c=b.sort()
    print("descending order:")
    c.reverse()
    print(c)
else:
    print("invalid")
    
      
