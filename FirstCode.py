# Python is a high level case-sensitive independent interpreted programing language which is used for general 
# purpose and allow to operate on any operating systems.
# Datatype->Datatype is a classification or categorization of data elements.
# There are two types of datatype:-
# Immutable aur mutable
# Immutable mai numeric,string,tuple aur boolean hota hai jisme se numeric mai integer,float aur complex no. hota hai
# Mutable mai List,dict aur set hota hai 
# Hello Zaid Code
# print->Function hai
# print("Hello Zaid")

# Output:Hello Zaid

# Multiplication Code
# print(10*30)

# Output:300

# Addition of Two Numbers
# a=20
# b=30

# print(a)
# print(b)
# print(a+b)

# Output:20
#        30
#        50

# A string is a sequence of character or collection of character which is enclosed or surrounded by single,double and triple
# quotation mark.
# String,List aur Tuple teeno ke chaar same operation hote hai like concatenation,Replication,Indexing and slicing hota hai 
# Concatenation of Two Strings
# x="hello"
# y="world"
# print(x)
# print(y)
# print(x+y)
# print(x+" "+y)

# Output: hello
#         world
#         helloworld
#         hello world

# id use hota location number pata karna ke liye jaha pai elements stored hora hai memory mai
# id->Function hai
# print(id(x))
# print(id(y))

# Output:1613799052016
#        1613799051888

# Variable is like a container in which we can store any data like string, integers etc.
# Varibale name cannot start with a number 
# 1x=2
# print(1x)
# Output:1x=2
#        ^
# SyntaxError: invalid decimal literal

# Variable
# x1=2
# print(x1)

# Output:2

# Spaces are not allowed in a variable

# a=10
# b=20
# total numbers=a+b
# print(total numbers)

# Output:total numbers=a+b
#              ^^^^^^^
# SyntaxError: invalid syntax

# Addition of two numbers
# a=10
# b=20
# totalnumbers=a+b
# print(a)
# print(b)
# print(totalnumbers)

# Output:10
#        20
#        30
# Special Characters are not allowed in a varibale('@','$','&') except underscore('_')
# A variable cannot be a keyword means reserved words i.e.(while,if,else,elif,True)
# override
# a=10
# a=20
# print(a)

# a=10
# print(a)
# a=20
# print(a)

# print("hello")
# print normally as a function used hota hai but print=10 edhar as a variable le liye hai toh ab yeh aagai function jaisa kaam 
# nahi karega as a variable kaam karega toh esliye hum 'del print' use karke print delete kar degai toh fir aagai jaakai as a 
# variable work nahi karega fir waapis se function jaisa work karega
# print=10
# print("world")
# Output:print("world")
# TypeError: 'int' object is not callable

# # case sensitive hai del
# del print
# print("world")

# swapping values
# x=10
# y=20
# print(x,y)

# Output:10 20
# x,y=y,x
# print(x,y)

# Output:20 10

# Multiple variable assignment with different values
# a=100
# b=200
# c=300
# print(a,b,c)
# Output:100 200 300

# a,b,c=100,200,300
# print(a,b,c)
# Output:100 200 300

# Multiple variable assignment with same values
# p=10
# q=10
# r=10
# print(p,q,r)
# Output:10 10 10
# p=q=r=10
# print(p,q,r)
# Output:10 10 10
# print(p)
# Output:10 

# user input value
# a=input("Enter Any Value: ")
# print("User Enter Value is ",a)
# Output:Enter Any Value: zaid
# User Enter Value is  zaid

# Concatenation of First_name and Last_name
# first_name=input("Enter first_name: ")
# last_name=input("Enter last_name: ")
# print("User Fullname is ",first_name+last_name)
# print("User Fullname is ",first_name+" "+last_name)
# Output:Enter first_name: Ansari
#        Enter last_name: Zaid
#        User Fullname is  AnsariZaid
#        User Fullname is  Ansari Zaid

# Concatenation of First_number and Last_number
# first_number=int(input("Enter first_number: "))
# second_number=int(input("Enter second_number: "))
# print("Addition of two numbers are ",first_number+second_number)
# Output:Enter first_number: 2
#        Enter second_number: 2
#        Addition of two numbers are  4

# Arithemetic operator

# +,-,/,*,%,//,**
# Addition->'+'.
# Subtraction->'-'.
# Division->'/':Yeh use hota hai quotient find karne ke liye but with decimal number means quotient value dega 
# decimal number ke saath for ex:2.0 .
# Floor Division->'//':Yeh use hota hai quotient find karne ke liye but without decimal number means quotient value dega 
# decimal number ke saath nahi for ex:2.
# Modulus->'%':Yeh use hota hai remainder find karne ke liye but remainder ya toh '0'hota hai ya toh '1' hota hai agar '0'
# remainder hoga means divisible hai aur '1' remainder hai toh divisible nhi hai.
# Multiplication->'*'.
# Exponentiation->'**':Means square ,cube nikalna like 2**2 i.e. 2 raise to power 2=4 aur 2**3 i.e. 2 raise to power 3=8 

# print(10/2)
# Output:5.0
# print(10//2)
# Output:5
# print(10%2)
# Output:0

# print(11/2)
# Output:5.5
# print(11//2)
# Output:5
# print(11%2)
# Output:1
# print(2**3)
# Output:8

# type function use hota hai datatype find karne ke liye
# a=10
# print(a)
# print(type(a))
# Output:10
# <class 'int'>

# a=10.5
# print(a)
# print(type(a))
# Output:10.5
# <class 'float'>

# Single Quotation,Double Quotation,Triple Quotation(String)
# a='hello world'
# b="hello world"
# c='''hello world'''
# print(a,b,c)
# print(type(a),type(b),type(c))

# Reason of using Single Quotation,Double Quotation,Triple Quotation in a String with example
# z='i love python'
# print(z)
# Output:i love python
# z='i love's python'
# print(z)
# Output:    z='i love's python'
#                             ^
# SyntaxError: unterminated string literal 
# z="i love's python"
# print(z)
# Output:i love's python
# z="i love
# python"
# print(z)
# Output:z="i love
#          ^
# SyntaxError: unterminated string literal 
# z='''i love
# pyhton'''
# print(z)
# Output:i love
#        pyhton


# Function means ( ) aur Method means .( )
# string operation
# concatenation
# x='i love python'
# y='program.'
# z=x+y
# print(z)
# Output:i love pythonprogram.
# print(x+y)
# Output:i love pythonprogram.

# replication
# a="hellozaid "
# print(a*10)
# Output:hellozaid hellozaid hellozaid hellozaid hellozaid hellozaid hellozaid hellozaid hellozaid hellozaid 

# indexing
# In Python, an indexing operation refers to the process of accessing a specific element in a data structure, like a list or 
# a string, by using its position or index. Think of it like accessing a particular item in a numbered list. The index is like 
# the item's address within the list, and by specifying that address, you can retrieve or manipulate the corresponding element.
# x="i love python program"
# print(x)
# Output:i love python program
# print("positive indexing")
# Output:positive indexing
# print(x[3])
# Output:o
# print(x[15])
# Output:r
# print("negative indexing")
# Output:negative indexing
# print(x[-18])
# Output:o
# print(x[-6])
# Output:r
# print(x[-1])
# Output:m
# postive indexing start with '0' means from first word and negative indexing start with '-1' means 
# from last word

# slicing
# In Python, slicing is a way to extract a portion of a sequence, such as a string, list, or tuple. The basic idea is to 
# specify a range of elements that you want to extract from the sequence. This range is defined by providing the starting index 
# and the ending index, separated by a colon.
# x="i love python program"
# print(x[start:end:step(default[1])])
# positive slice
# number chahe positive ho ya negative ho start small index number se hona chahiye aur end greater index number se hona chahiye  
# agar start index number greater hai toh step:-1 legai aur agar start small index number hai toh step:1 legai.
# starting ka index number '0' hamesha include hoga but last ka index number include nhi hoga exlude hoga for ex:
# '7' liye index number end ka woh include nhi hoga exclude hoke '6' index number tak ka include hoga like an array 
# print(x[7:12])
# Output:pytho
# print(x[7:13])
# Output:python
# print(x[7:13:1])
# Output:python
# print(x[7:13:2])
# Output:pto
# negative slice
# print(x[-14:-8])
# Output:python
# print(x[-14:-8:2])
# Output:pto
# print(x[-7:-15:-1])
# Output:p nohtyp
# print(x[7:])
# Output:python program
# print(x[:7])
# Output:i love
# print(x[:])
# Output:i love python program
# print(x[::-1])
# Output:margorp nohtyp evol i                                                                                                                                         
# print(x[::-1])  isse reverse hoga number

# Difference between slicing and indexing operation 
# Certainly! Here are five points explaining the difference between slicing and indexing operations in Python using 
# simple language:

# 1. **Indexing:**
#    - **What it does:** Indexing is like pointing to a specific item in a collection, such as a list or a string.
#    - **Example:** `my_list[2]` would mean selecting the third item in the list.
#    - **In simple terms:** It's like identifying and grabbing a single item at a specific position.

# 2. **Slicing:**
#    - **What it does:** Slicing is like cutting a piece from a collection, creating a new collection.
#    - **Example:** `my_list[1:4]` would mean taking a slice from the second to the fourth item in the list.
#    - **In simple terms:** It's like extracting a chunk or section of items from a sequence.

# 3. **Returned Values:**
#    - **Indexing:** Returns a single item at the specified position.
#    - **Slicing:** Returns a new collection containing a range of items.

# 4. **Usage:**
#    - **Indexing:** Used when you need a specific item from a collection.
#    - **Slicing:** Used when you want to work with a subset or part of a collection.

# 5. **Syntax:**
#    - **Indexing:** Uses square brackets with a single index like `my_list[2]`.
#    - **Slicing:** Uses square brackets with a start and stop index separated by a colon like `my_list[1:4]`.

# In summary, indexing is about getting one specific item at a particular position, while slicing is about creating a new 
# collection by selecting a range of items from an existing collection.

# # string methods
# s="i love python program"
# # find use hota index number find karne ke liye particular elements ka
# print(s.find("e"))
# Output:5
# print(s.find("o"))
# Output:3
# # capitalize use hota hai first element capital karne ke liye
# print(s.capitalize())
# Output:I love python program
# # title use hota hai harr element ka first element capital karne ke liye
# print(s.title())
# Output:I Love Python Program
# # upper use hota hai saare harr ek individual element ko capital karne ke liye
# print(s.upper())
# Output:I LOVE PYTHON PROGRAM
# # lower use hota hai saare harr ek individual element ko smaller karne ke liye
# print(s.lower())
# Output:i love python program
# # count use hota hai particular element kitni baar aaya hai woh count karne ke liye
# print(s.count("o"))
# Output:3
# # startswith use hota hai check karne ke liye ki element particular word ke saath start hora hai ki 
# # nahi
# print(s.startswith("i"))
# Output:True
# print(s.startswith("o"))
# Output:False
# # endswith use hota hai check karne ke liye ki element particular word ke saath end hora hai ki 
# # nahi
# print(s.endswith("m"))
# Output:True
# print(s.endswith("a"))
# Output:False

# s="It is python program"
# # replace use hoga 'is' ko "it's" se replace karne ke liye
# print(s.replace("is","it's"))
# Output:It it's python program
# # swapcase capital words ko small words mai convert kar dega aur small words ko capital words mai convert kar dega jitne bhi 
# elements hai unko
# print(s.swapcase())
# Output:iT IS PYTHON PROGRAM

# # format 
# # Format use hota hai string aur integer ko ek saath likhne ke liye
# name="karan"
# year=24
# print("my name is "+name+" i am "+year+" year old")->not working
# Output:print("my name is "+name+" i am "+year+" year old")
#              ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str
# print(f"my name is {name} my age is {year}")
# Output:my name is karan my age is 24

# # name="karan"
# # year=24
# statement=f"my name is {name} my age is {year}"
# print(statement)
# Output:my name is karan my age is 24

# # strip use hota right aur left side ke space ko hatane ke liye means dono side se space ko hatane ke liye
# d="         hello"
# print(d)
# Output:    hello
# print(d.strip())
# Output:hello     

# Use of Strip with example
# name=input("enter name").strip()
# print(f'hello {name}')
# Output:enter name           zaid
# hello zaid

# tuple
# A tuple is a collection of homogenous and heterogenous data elements which is enclosed or surrounded by paranthesis or circle
# bracket '( )' and separated by ','.
# names=("karan","priya","kunal","pankaj")
# # names=("karan","priya","kunal","pankaj",2) isme integer bhi le sakte hai woh bhi allow hai
# print(names)
# Output:('karan', 'priya', 'kunal', 'pankaj')
# # indexing opeartion
# print(names[0])
# Output:karan
# # nested indexing
# print(names[0][0])
# Output:k    
# print(names[-1][-1])
# Output:j    

# # nested tuple
# s=(10,20,30,(30,56))
# print(s)
# Output:(10, 20, 30, (30, 56))
# print(s[-1][0])
# Output:30
# # slicing operation
# print(s[1:3])
# Output:(20, 30)
# print(s[1:])
# Output:(20, 30, (30, 56))
# # slicing ke andarr indexing 
# print(s[1:][1])
# Output:30
# print(s[:3][-1])
# Output:30

# # concatenation
# x=(10,20)
# y=(30,40)
# print(x+y)
# Output:(10, 20, 30, 40)
# # replication
# print(x*3)
# Output:(10, 20, 10, 20, 10, 20)
# print(type(x))
# Output:<class 'tuple'>

# yeh bhi tuple he hai circle bracket nahi hai yeh sochke confuse mat hojana tuple ka main 
# definition he hai separated by ',' toh iss wajah se yeh bhi tuple he hai integer mat samajhna isey
# d=23,45,67,8,67
# print(d)
# Output:(23, 45, 67, 8, 67)
# print(type(d))
# Output:<class 'tuple'>

# # tuple method 
# # indexing method yeh use hota hai index number find karne ke liye 
# print(d.index(45))
# Output:1
# # count method yeh use hota ki kitni baar elements aaya hai woh find karne ke liye
# print(d.count(67))
# Output:2

# List
# List is a collection of homogenous and heterogenous data elements which is enclosed or surrounded by Square Bracket '[ ]' and
#  separated by ','.
# names=["karan","priya","kunal","pankaj"]
# # # names=["karan","priya","kunal","pankaj",2] isme integer bhi le sakte hai woh bhi allow hai
# print(names)
# Output:['karan', 'priya', 'kunal', 'pankaj']
# print(type(names))
# Output:<class 'list'>
# # # indexing opeartion
# print(names[0])
# Output:karan
# # # nested indexing
# print(names[0][0])
# Output:k
# print(names[-1][-1])
# Output:j

# # # nested List
# s=[10,20,30,[30,56]]
# print(s)
# Output:[10, 20, 30, [30, 56]]
# print(type(s))
# Output:<class 'list'>
# print(s[-1][0])
# Output:30
# # # slicing operation
# print(s[1:3])
# Output:[20, 30]
# print(s[1:])
# Output:[20, 30, [30, 56]]
# # # slicing ke andarr indexing 
# print(s[1:][1])
# Output:30
# print(s[:3][-1])
# Output:30

# # # concatenation
# x=[10,20]
# y=[30,40]
# print(x+y)
# Output:[10, 20, 30, 40]
# # # replication
# print(x*3)
# Output:[10, 20, 10, 20, 10, 20]
# print(type(x))
# Output:<class 'list'>
# # baki sab same rahega tuple ke jaise

# list method
# mylist = [1,2,3,4,5]
# print(mylist)
# Output:[1, 2, 3, 4, 5]
# In Python, the append method is a function that belongs to lists. It is used to add a new element to the end of a list.
# # append add karta hai element ko at the end of element
# mylist.append(10)
# print(mylist)
# Output:[1, 2, 3, 4, 5, 10]
# add=[7,8,9,11]
# # append method add karne ka kaam karta hai at the end of element but extend method integer aur string dono ko 
# # saath mai merge kar sakta hai but concatenation mai same datatypes chahiye rehta hai different 
# # datatypes nhi chalta hai
# mylist.extend(add)
# print(mylist)
# Output:[1, 2, 3, 4, 5, 10, 7, 8, 9, 11]    
# # count use hota hai count karne ke liye ki kitni baar particular element aaya hai
# print(mylist.count(10))
# Output:1
# print(mylist)
# Output:[1, 2, 3, 4, 5, 10, 7, 8, 9, 11]
# # index use hota hai index number find karne ke liye particular element ka
# print(mylist.index(10))
# Output:5
# print(mylist)
# Output:[1, 2, 3, 4, 5, 10, 7, 8, 9, 11]
# # insert use hota insert karne ke liye element ko particular defined index number position pai jaise yaha pai humne
# # index number 1 pai 50 add kiya hai (index_number,insert_value)
# mylist.insert(1,50)
# print(mylist)
# Output:[1, 50, 2, 3, 4, 5, 10, 7, 8, 9, 11]
# # pop use hota hai defined index number waala element remove karne ke liye jaise yaha pai humne 
# # index number 1 ko remove kiya means joh bhi element index number 1 pai hoga woh remove hojayega
# # pop remove karta hai element ko based on index number 
# mylist.pop(1)
# print(mylist)
# Output:[1, 2, 3, 4, 5, 10, 7, 8, 9, 11]
# # remove use hota particular element ko remove karne ke liye joh element defined karte hai woh element ko remove karta hai
# # remove method remove karta hai element ko based on defined element
# mylist.remove(4)
# print(mylist)
# Output:[1, 2, 3, 5, 10, 7, 8, 9, 11]       
# # yeh use hota hai reverse karne ke liye element ko
# mylist.reverse()
# print(mylist)
# Output:[11, 9, 8, 7, 10, 5, 3, 2, 1]       
# # sort karega element ko based on ascending order
# mylist.sort()
# print(mylist)
# Output:[1, 2, 3, 5, 7, 8, 9, 10, 11]       
# # reverse=True means yeh descending order mai sort karega element ko aur by default yeh reverse=False hota  hai
# toh descending order mai reverse karne ke liye reverse=True daalna parta hai
# mylist.sort(reverse=True)
# print(mylist)
# Output:[11, 10, 9, 8, 7, 5, 3, 2, 1]

# # single value tuple hai yeh
# s=("python",)
# print(s)
# # Output:('python',)
# print(type(s))
# Output:<class 'tuple'>

# # edhar list aur tuple ko extend kiye hai taaki humey full 'python' aisa mil sakai
# l=[1,2,3]
# s=("python",)
# l.extend(s)
# print(l)
# Output:[1, 2, 3, 'python']

# split method
# In Python, the split method is used to break a string into a list of substrings based on a specified delimiter. 
# split method use hota hai string ko list mai change ke liye specific character ko laikai
# s="i love python programming"
# print(s.split(" "))
# Output:['i', 'love', 'python', 'programming']
# print(s.split("python"))
# Output:['i love ', ' programming']

# Join method
# In simple terms, the join method in Python is used to combine elements of an iterable (like a list or a tuple) into a single 
# string. It takes a string as a separator and joins the elements of the iterable using that separator.
# # join method use hota hai list ko string mai change karne ke liye based on specific character
# l=["i","love","python","programming"]
# s=" ".join(l)
# print(s)
# Output:i love python programming
# print(type(s))
# Output:<class 'str'>

# # split join used example
# email=input("enter email")
# email=email.split("@") #["arfa","gmail.com"]
# username=email[0] # "arfa"
# print(username)
# Output:enter emailazaid@gmail.com
# azaid
# email="@".join(email) # "arfa@gmail.com"
# print(email)
# Output:azaid@gmail.com

# # dictionary
# # dictionary unordered hota hai
# # dictionary is a collection of key value pairs which is enclosed by curly braces'{ }' and separated by ','
# # dictionary mai key hamesha immutable hoti hai means woh belong karti hai numeric,string,tuple and boolean se aur 
# # value mutable ya immutable dono ho sakta hai
# # d={"key":value}

# d={"a":10,"b":20,"c":30}
# print(d)
# Output:{'a': 10, 'b': 20, 'c': 30}
# print(type(d))
# Output:<class 'dict'>

# info={
#     "name":"karan",
#     "email":"azaid@gmail.com",
#     "password":"2234asdf"
#     }

# print(info)
# Output:{'name': 'karan', 'email': 'azaid@gmail.com', 'password': '2234asdf'}
# # yeh keys() apne ko keys batata hai sirf
# print(info.keys())
# Output:dict_keys(['name', 'email', 'password'])
# # values () apne ko values batata hai sirf
# print(info.values())
# Output:dict_values(['karan', 'azaid@gmail.com', '2234asdf'])     
# # yeh list of tuples dikhata hai means key aur value dono par with circle bracket
# print(info.items())
# Output:dict_items([('name', 'karan'), ('email', 'azaid@gmail.com'), ('password', '2234asdf')])
# # get se particular key daalke uska value show kar sakte hai
# print(info.get("name"))
# Output:karan
# # iss tarha se bhi key ke values show kar sakte hai
# print(info["name"])
# Output:karan

# # difference between get operation and get method
# # yeh get operation hai isme agar joh key nhi hai means defined kiya huwa nhi hai 
# # woh daalegai toh error aayega
# print(info["fullname"])
# Output:print(info["fullname"])
#              ~~~~^^^^^^^^^^^^
# KeyError: 'fullname'
# # yeh get method hai isme agar joh key nhi hai means defined kiya huwa nhi hai woh daalegai toh
# # error nhi aayega  
# print(info.get("name","hello"))
# Output:karan
# # isme hello daal diye hai toh woh dikhayega
# print(info.get("fullname","hello"))
# Output:hello
# # isme none dikhayega kyu ki kuch nahi diye hai
# print(info.get("fullname"))
# Output:None

# # but yeh dono single key value pair add karte hai
# # isme age:24 add kar diye hai dictionary mai
# info.setdefault("age",24)
# print(info)
# Output:{'name': 'karan', 'email': 'azaid@gmail.com', 'password': '2234asdf', 'age': 24}
# # isme city:thane add kiye hai dictionary mai 
# info["city"]="thane"
# print(info)
# Output:{'name': 'karan', 'email': 'azaid@gmail.com', 'password': '2234asdf', 'age': 24, 'city': 'thane'}

# # update bhi used hota hai add karne ke liye key value pair dictionary mai but edhar mutilpe key value pairs 
# # add kar sakte hai

# info["age"]=25
# info.update({"city":"kalva"})
# print(info)
# Output:{'name': 'karan', 'email': 'azaid@gmail.com', 'password': '2234asdf', 'age': 25, 'city': 'kalva'}

# address={
#           "zipcode":400612,
#           "state":"maharashtra",
#           "dist":"thane"
# }

# info.update(address)
# print(info)
# Output:{'name': 'karan', 'email': 'azaid@gmail.com', 'password': '2234asdf', 'age': 25, 'city': 'kalva', 'zipcode': 400612, 
# 'state': 'maharashtra', 'dist': 'thane'}  

# set
# set unordered hota hai means harr baar elements print karne pai elements koi bhi sequence mai show hote hai output mai
# jisey hum predict nahi kar sakte hai ki kis sequence mai elements print hogai output mai.
# set is a collection of unique values but without key value pairs and it is enclosed by '{ }' and separated
# by ','
# set mai elemenet immutable datatypes hote hai but set mutable datatypes hota hai means element belong karte hai 
# immutable datatypes se

# s={1,2,5,3,4,5}
# print(s)
# Output:{1, 2, 3, 4, 5}
# print(type(s))
# Output:<class 'set'>

# # isme tuple ko daaley hai set ke andarr aur tuple immutable datatypes hota hai aur maine kya bola tha set ke elements 
# immutable datatypes se belong karte hai esliye edhar error nhi aara hai tuple ko set ke andarr daalne pai as an elements
# s={1,2,5,3,(4,5)}
# print(s)
# Output:{1, 2, 3, (4, 5), 5}
# print(type(s))
# Output:<class 'set'>

# # isme list ko daaley hai set ke andarr toh error aara hai aur list mutable datatypes hota hai aur maine kya bola tha 
# set ke elements immutable datatypes se belong karte hai esliye edhar error aara hai list ko set ke andarr daalne pai 
# as an elements
# s={1,2,5,3,[4,5]}
# print(s)
# Output:s={1,2,5,3,[4,5]}
#          ^^^^^^^^^^^^^^^
# TypeError: unhashable type: 'list'
# print(type(s))
# error ke wajah se kuch answer nahi milega dekhne ko

# set operations
# s1={1,2,3,4,5}
# s2={3,4,5,6,7,8}

# print(s1|s2) # union of two sets(sab elements aayegai dono sets mai se but ek baar repeat mai koi bhi elements nahi aayegai 
# dono sets mai se)
# Output:{1, 2, 3, 4, 5, 6, 7, 8}
# print(s1&s2) # intersection of two sets(dono sets mai se common elements show karega bas)
# Output:{3, 4, 5}
# print(s1-s2) # difference of two sets(aise elements show karega joh s2 sets mai se nahi hai)
#  s1 set mai se s2 set minus kar diye edhar
# Output:{1, 2}
# print(s2-s1) # difference of two sets(aise elements show karega joh s1 sets mai se nahi hai) 
# s2 set mai se s1 set minus kar diye edhar
# Output:{8, 6, 7}



# # yeh add karega s2 set mai 11 
# s2.add(11)
# print(s2)
# Output:{3, 4, 5, 6, 7, 8, 11}

# # yeh remove karega 6 s2 set mai se
# s2.remove(6)
# print(s2)
# Output:{3, 4, 5, 7, 8, 11}

# # len( ) function use hota hai length pata karne ke liye elements ka 
# a=["p",23,3,6,0]
# print(len(a))
# Output:5
# a="hello world"
# print(len(a))
# Output:11

# Comparison or relational operator (ismey boolean mai he output aayega means True aur False )
# >,<,>=,<=,==,!=
# x=10
# print(x>20)
# # Output:False
# print(x<20)
# # Output:True
# print(x>=20)
# # Output:False
# print(x<=20)
# # Output:True
# print(x!=20)
# # Output:True
# print(x==20)
# # Output:False
# print(x>10)
# # Output:False
# print(x>=10)
# # Output:True
# print(x!=10)
# # Output:False

# Assignment operator 
# =,+=,-=,*=,%=,/=,//=
# x=10
# x=x+5
# print(x)
# Output:15
# x+=5
# print(x)
# Output:15

x=10
# x=x-5
# print(x)
# Output:5
# x-=5
# print(x)
# Output:5

# Membership Operator(boolean mai aayega output ismey bhi means True aur False )
# in , not in
# t=(2,3,1,45,67,8)
# print(t)
# Output:(2,3,1,45,67,8)
# print(45 in t)
# Output:True
# print(50 in t)
# Output:False
# print(50 not in t)
# Output:True
#print(50 not in t)
# print(40 not in t)
# Output:True

# Identity Operator
# is , is not
# a=[1,2,3]
# b=[1,2,3]
# print(a==b) # compare karega yeh elements dono variable ke 
# Output:True
# print(id(a))
# Output:139767580863872
# print(id(b))
# Output:139767580008896
# print(a is b) # compare karega yeh location dono variable ke elemets ka
# Output:False

# Immutable mai true dega aur mutable mai false dega because immutable ko one time stored karta hai
# same location pai aur mutable mai harr baar alag-alag location pai stored karega elemets ko
# x=10
# y=10
# print(x==y)
# # Output:True
# print(id(x))
# # Output:9789280
# print(id(y))
# # Output:9789280

# x=2588
# y=2588
# print(x==y)
# # Output:True
# print(id(x))
# # Output:140391871175536
# print(id(y))
# # Output:140391871175536
# print(x is y)
# Output:True

#Conditional statement
# if,else,elif
# if(condition->True)
#     executable block

# print("hello")
# if(True):
#     print("hi")
# print("bye")    
#  Output:hello
#         hi
#         bye

# print("hello")
# if(False):
#     print("hi")
# print("bye")    
# Output:hello
#        bye

# x=10
# print("hello")
# if(x>10):
#     print("hi")
# print("bye")
# Output:hello
#        bye

# take age from user and print hello if age is greater than 18
# user=int(input("Enter Your age:"))
# if(user>18):
#     print("hello")
# Output:Enter Your age:19
#                   hello

# Output:Enter Your age:18

# take age from user and check he is eligible for vote or not

# age=int(input("enter age"))
# if(age>=18):
#     print("eligible for vote")
# else:
#     print("Not eligible for vote")    
# Output:enter age23
# eligible for vote
# Output:enter age17
# Not eligible for vote

# take number from user and check it is positive or negative
# number=float(input("Enter a number: "))
# if number>0:
#     print("number is positive")
# else:
#     print("number is negative")  
#   Output:Enter a number:23
#    number is positive
#   Output:Enter a number:-2
#    number is negative


# Take two number from a and b and check which one is greater and smaller

# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# if(a>b):
#     print("a is greater")
# else:
#     print("b is greater")    
# Output:Enter a number:23
#        Enter a number:3
#        a is greater

# Output:Enter a number:3
#        Enter a number:23
#        b is greater

# example of if,elif and else
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# if(a>b):
#      print("a>b")
# elif(b>a):
#      print("b>a")
# else:
#      print("a==b")    
# Output:Enter a number: 23
#        Enter a number: 20
#        a>b

# Output:Enter a number: 20
#        Enter a number: 34
#        b>a

# if,if,else(ismey first 'if' statement ko alag lega aur dusre 'if' statement aur 'else' statement ko saath mai lega)
# a=int(input("enter first number"))
# b=int(input("enter second number"))
# if(a>b):
#      print("a>b")

# if(b>a):
#      print("b>a")
# else:
#      print("a==b")          


# take two numbers and operator from user and calculate the numbers based on user entered operator
# num1=float(input("enter the first number:"))
# num2=float(input("enter the second number:"))
# operator=input("Enter the operator(+,-,*,/,//): ")

# if (operator=="+"):
#      print(num1+num2)
# elif (operator=="-"):
#      print(num1-num2)
# elif (operator=="*"):
#      print(num1*num2)
# elif (operator=="/"):
#      print(num1/num2)
# elif (operator=="//"):
#      print(num1//num2)
# else:
#      print("invalid operator")     
# Output:enter the first number:5
#        enter the second number:5
#        Enter the operator(+,-,*,/,//): +
#        10.0
     
# a=int(input("enter number"))
# # print(11%2==0)     
# if(a%2==0):
#      print("even number")
# else:
#      print("odd number")     
# Output:enter number8
#        even number
# Output:enter number11
#        odd number

#take number from user and check it is divisible by 7 or not
# number = int(input("Enter a number: "))
# if number % 7 == 0:
#     print(f"{number} is divisible by 7.")
# else:
#     print(f"{number} is not divisible by 7.")
# # Output:Enter a number: 49
# #        49 is divisible by 7.
# #take number from user and check it is multiple of 5 or not
# number = int(input("Enter a number: "))

# if number % 5 == 0:
#     print(f"{number} is a multiple of 5.")
# else:
#     print(f"{number} is not a multiple of 5.")
# Output:Enter a number: 25   
#        25 is a multiple of 5.
    
# Logical Opearator(ismey answer boolean mai aayega ya toh True aayega aur ya toh False aayega)
# and,or,not
# and(dono conditon true chahiye toh true milega otherwise false milega agar ek bhi false hai toh)
# print(True and True)    
# Output:True
# print(False and True)
# Output:False
# print(False and False)
# Output:False

# or(koi bhi ek condition true rahega toh true milega)
# print(True or True)    
# Output:True
# print(False or True)
# Output:True
# print(False or False)
# Output:False

# or and and combination
# print(True or False and True)
# Output:True 
# print(True or True and False)
# Output:True 

# and
# print(10>2 and 10<20)
# Output:True
# print(10>2 and 10<8)
# Output:False

# or
# print(10>2 or 10<20)
# Output:True
# print(10>2 or 10<8)
# Output:True

# not(true ka false hoga aur false ko true hoga means ulta)
# print(not True)
# Output:False
# print(not 10>2)
# Output:False

# 0-20->hello
# 20-50->hii
# 50-80->hey
# 80-100->bye

# take a number from user and if user number is between 0-20 then print 'hello' and if user number is between 20-50 then print 'hi' and if user number 
# is between 50-80 then print 'hey' and if user number is between 80-100 then print 'bye' in python

# user_number = int(input("Enter a number: "))

# if 0 <= user_number <= 20:
#     print("Hello")
# elif 20 < user_number <= 50:
#     print("Hi")
# elif 50 < user_number <= 80:
#     print("Hey")
# elif 80 < user_number <= 100:
#     print("Bye")
# else:
#     print("Number is outside the specified ranges.")

# Output:Enter a number: 20
#        Hello  
# Output:Enter a number: 80
#        Hey

print("hellos")