# print("Hello Zaid")
# print(10*30)

# a=20
# b=30

# print(a)
# print(b)
# print(a+b)

# x="hello"
# y="world"
# print(x)
# print(y)
# print(x+y)
# print(x+" "+y)
# print(id(x))
# print(id(y))

# # 1x=2
# x1=2
# print(x1)

# a=10
# b=20
# # total numbers=a+b
# totalnumbers=a+b
# print(a)
# print(b)
# print(totalnumbers)
# # # override
# # a=10
# # a=20
# # print(a)

# a=10
# print(a)
# a=20
# print(a)

# print("hello")
# print=10
# # print("world")
# # case sensitive hai del
# del print
# print("world")

# swapping values
# x=10
# y=20
# print(x,y)
# x,y=y,x
# print(x,y)

# Multiple variable assignment with different values

# a=100
# b=200
# c=300
# print(a,b,c)

# a,b,c=100,200,300
# print(a,b,c)

# Multiple variable assignment with same values
# p=10
# q=10
# r=10
# print(p,q,r)
# p=q=r=10
# print(p,q,r)
# print(p)

# user input value
# a=input("Enter Any Value: ")
# print("User Enter Value is ",a)

# first_name=input("Enter first_name: ")
# last_name=input("Enter last_name: ")
# print("User Fullname is ",first_name+last_name)

# first_number=int(input("Enter first_number: "))
# second_number=int(input("Enter second_number: "))
# print("Addition of two numbers are ",first_number+second_number)

# Arithemetic operator

# +,-,/,*,%,//

# print(10/2)
# print(10//2)
# print(10%2)

# print(11/2)
# print(11//2)
# print(11%2)
# print(2**3)

# a=10
# print(a)
# print(type(a))

# a=10.5
# print(a)
# print(type(a))

# a='hello world'
# b="hello world"
# c='''hello world'''
# print(a,b,c)
# print(type(a),type(b),type(c))

# z='i love python'
# # z='i love's python'
# z="i love's python"
# # z="i love
# # python"
# z='''i love
# pyhton'''
# print(z)

# string operation
# concatenation
# x='i love python'
# y='program.'
# z=x+y
# print(z)
# print(x+y)

# replication
# a="hellozaid "
# print(a*10)

# indexing
# x="i love python program"
# print(x)
# print("positive indexing")
# print(x[3])
# print(x[15])
# print("negative indexing")
# print(x[-18])
# print(x[-6])
# print(x[-1])
# postive indexing start with '0' means from first word and negative indexing start with '-1' means 
# from last word

# slicing
# x="i love pyhton program"
# print(x[start:end:step(default[1])])
# positive slice
# number chahe positive ho negative start small hona chahiye aur end greater hona chahiye index 
# number ka agar start greater hai toh step:-1 hoga aur agar start small hai toh step:1 hoga.
# starting ka '0' include hoga index mai but last ka '7' liye index mai toh '6' tak include hoga 
# like an array 
# print(x[7:12])
# print(x[7:13])
# print(x[7:13:1])
# print(x[7:13:2])
# negative slice
# print(x[-14:-8])
# print(x[-14:-8:2])
# print(x[-7:-15:-1])
# print(x[7:])
# print(x[:7])
# print(x[:])
# print(x[::-1])
# print(x[::-1])  isse reverse hoga number

# # string methods
# s="i love python program"
# # find use hota index number find karne ke liye particular elements ka
# print(s.find("e"))
# print(s.find("o"))
# # capitalize use hota hai first element capital karne ke liye
# print(s.capitalize())
# # title use hota hai harr element ka first element capital karne ke liye
# print(s.title())
# # upper use hota hai saare harr ek individual element ko capital karne ke liye
# print(s.upper())
# # lower use hota hai saare harr ek individual element ko smaller karne ke liye
# print(s.lower())
# # count use hota hai particular element kitni baar aaya hai woh count karne ke liye
# print(s.count("o"))
# # startswith use hota hai check karne ke liye ki element particular word ke saath start hora hai ki 
# # nahi
# print(s.startswith("i"))
# print(s.startswith("o"))
# # endswith use hota hai check karne ke liye ki element particular word ke saath end hora hai ki 
# # nahi
# print(s.endswith("m"))
# print(s.endswith("a"))

# s="This is python program"
# # replace use hoga is ko it's se replace karne ke liye
# print(s.replace("is","it's"))
# # swapcase capital ko small aur small ko capital kar dega saare elements ko 
# print(s.swapcase())

# # format method
# # yeh use hota hai string aur integer ko ek saath combine karne ke liye
# name="karan"
# year=24
# # print("my name is "+name+" i am "+year+" year old")->not working
# print(f"my name is {name} my age is {year}")

# name="karan"
# year=24
# statement=f"my name is {name} my age is {year}"
# print(statement)

# # strip use hota right aur left means dono side se space ko hatane ke liye
# d="         hello"
# print(d)
# print(d.strip())

# name=input("enter name").strip()
# print(f'hello {name}')

# tuple
# names=("karan","priya","kunal","pankaj")
# # names=("karan","priya","kunal","pankaj",2) isme integer bhi le sakte hai woh bhi allow hai
# print(names)
# # indexing opeartion
# print(names[0])
# # nested indexing
# print(names[0][0])
# print(names[-1][-1])

# # nested tuple
# s=(10,20,30,(30,56))
# print(s)
# print(s[-1][0])
# # slicing operation
# print(s[1:3])
# print(s[1:])
# # slicing ke andarr indexing 
# print(s[1:][1])
# print(s[:3][-1])

# # concatenation
# x=(10,20)
# y=(30,40)
# print(x+y)
# # replication
# print(x*3)
# print(type(x))

# yeh bhi tuple he hai circle bracket nahi hai yeh sochke confuse mat hojana tuple ka main 
# definition he hai separated by ',' toh iss wajah se yeh bhi tuple he hai integer mat samajhna isey
# d=23,45,67,8,67
# print(d)
# print(type(d))

# # tuple method 
# # indexing method yeh use hota hai index number find karne ke liye 
# print(d.index(45))
# # count method yeh use hota ki kitni baar elements aaya hai woh find karne ke liye
# print(d.count(67))

# List
# names=["karan","priya","kunal","pankaj"]
# # # names=["karan","priya","kunal","pankaj",2] isme integer bhi le sakte hai woh bhi allow hai
# print(names)
# print(type(names))
# # # indexing opeartion
# print(names[0])
# # # nested indexing
# print(names[0][0])
# print(names[-1][-1])

# # # nested List
# s=[10,20,30,[30,56]]
# print(s)
# print(type(s))
# print(s[-1][0])
# # # slicing operation
# print(s[1:3])
# print(s[1:])
# # # slicing ke andarr indexing 
# print(s[1:][1])
# print(s[:3][-1])

# # # concatenation
# x=[10,20]
# y=[30,40]
# print(x+y)
# # # replication
# print(x*3)
# print(type(x))
# # baki sab same rahega tuple ke jaise

# list method
# mylist = [1,2,3,4,5]
# print(mylist)
# # append add karta ho element at the end of whole element
# mylist.append(10)
# print(mylist)
# add=[7,8,9,11]
# # append merge karne ka kaam karta like a concatenation but extend integer aur string dono ko 
# # saath mai merge kar sakta hai but concatenation mai same datatypes chahiye rehta hai different 
# # datatypes nhi chalta hai
# mylist.extend(add)
# # count use hoga count karne ke liye ki kitni particular element aaya hai
# print(mylist.count(10))
# # index use hota hai index number find karne ke liye particular element ka
# print(mylist.index(10))
# # insert use hota insert karne ke element particular defined index number pai jaise yaha pai humne
# # index number 1 pai 50 add kiya hai (index_number,insert_value)
# mylist.insert(1,50)
# print(mylist)
# # pop use hota hai defined index number waala element remove karne ke liye jaise yaha pai humne 
# # index number 1 ko remove kiya means joh bhi element index number 1 pai hoga remove hojayega
# # pop remove karta hai element ko based on index number 
# mylist.pop(1)
# print(mylist)
# # remove use hota particular element ko remove karne woh element defined karke jisko remove karna hai
# # remove karta hai element ko remove based on defined element
# mylist.remove(4)
# print(mylist)
# # yeh use hota hai reverse karne ke element ko
# mylist.reverse()
# print(mylist)
# # sort karega element ko based on ascending order
# mylist.sort()
# print(mylist)
# # reverse=True means yeh descending order mai sort karega element ko
# mylist.sort(reverse=True)
# print(mylist)

# # single value tuple hai yeh
# s=("python",)
# print(s)
# print(type(s))

# # edhar list aur tuple ko extend kiye hai taaki humey full "python" aisa mil sakai
# l=[1,2,3]
# s=("python",)
# l.extend(s)
# print(l)

# # split method use hota hai string ko list mai change ke liye specific character ko laikai
# s="i love python programming"
# print(s.split(" "))
# print(s.split("python"))

# # join ,method use hota hai list ko string mai change karne ke liye based on specific character
# l=["i","love","python","programming"]
# s=" ".join(l)
# print(s)
# print(type(s))

# # split join used example
# email=input("enter email")
# email=email.split("@") #["arfa","gmail.com"]
# username=email[0] # "arfa"
# print(username)
# email="@".join(email) # "arfa@gmail.com"
# print(email)





