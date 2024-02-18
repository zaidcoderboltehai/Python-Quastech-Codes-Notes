# Python is a high level case-sensitive independent interpreted programing language which is used for general 
# purpose and allow to operate on any operating systems.
# Case-Sensitive means small 'a' is not equal to capital 'A'.
# Datatype->Datatype is a classification or categorization of data elements.
# There are two types of datatypes:-
# Immutable aur mutable:-
# Immutable mai numeric,string,tuple aur boolean hota hai jisme se numeric mai integer,float aur complex no. hota hai.
# Mutable mai List,dict aur set hota hai.
# Hello Zaid Code
# print()->Function hai.
# print("Hello Zaid")

# Output:Hello Zaid

# Function aisa hota hai->( )
# Method aisa hota hai->.( )

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
# String,List aur Tuple teeno ke chaar same operation hote hai like concatenation,Replication,Indexing and slicing hota hai.
# Operation of strings: 
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

# id use hota hai location number pata karna ke liye jaha pai elements stored hora hai memory mai.
# id()->Function hai.
# print(id(x))
# print(id(y))

# Output:1613799052016
#        1613799051888

# Variable is like a container in which we can store any data like string, integers etc.
# Varibale name cannot start with a number.
# 1x=2
# print(1x)
# Output:1x=2
#        ^
# SyntaxError: invalid decimal literal

# Variable
# x1=2
# print(x1)

# Output:2

# Spaces are not allowed in a variable.
# Addition of two numbers
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
# Special Characters are not allowed in a varibale('@','$','&') except underscore('_').
# A variable cannot be a keyword means reserved words i.e.(while,if,else,elif,True)

# override
# a=10
# a=20
# print(a)
# Output:20

# a=10
# print(a)
# Output:10
# a=20
# print(a)
# Output:20

# print("hello")
# Output:hello
# print normally as a function used hota hai but print=10 edhar as a variable le liye hai toh ab yeh aagai function jaisa kaam 
# nahi karega as a variable kaam karega toh esliye hum 'del print' use karke print as a variable delete kar degai toh fir yeh aagai jaakai as a 
# variable work nahi karega firse waapis se function jaisa work karega.
# print=10
# print("world")
# Output:print("world")
# TypeError: 'int' object is not callable

# # case sensitive hai del
# print=10
# del print
# Output:"       #delete hogaya yaha pai print=10
# print("world")
# Output:world

# swapping values
# x=10
# y=20
# print(x,y)
# Output:10 20
# x,y=y,x          # edhar 'x' mai 'y' ki value 20 aajayegi aur 'y' mai 'x' ki value 10 aajayegi
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
# print(a)
# Output:100 200 300
# Output:100


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

# user input value code
# a=input("Enter Any Value: ")
# print("User Enter Value is ",a)
# Output:Enter Any Value: zaid
# User Enter Value is  zaid

# Concatenation of First_name and Last_name code
# first_name=input("Enter first_name: ")
# last_name=input("Enter last_name: ")
# print("User Fullname is ",first_name+last_name)
# print("User Fullname is ",first_name+" "+last_name)
# Output:Enter first_name: Ansari
#        Enter last_name: Zaid
#        User Fullname is  AnsariZaid
#        User Fullname is  Ansari Zaid

# Concatenation of First_number and Last_number code
# first_number=int(input("Enter first_number: "))
# second_number=int(input("Enter second_number: "))
# print("Addition of two numbers are ",first_number+second_number)
# Output:Enter first_number: 2
#        Enter second_number: 2
#        Addition of two numbers are  4

# Arithemetic operator
# python mai by default numbers decimal mai hote hai like 2.0,3.0 .
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
# Exponentiation->'**':Means square ,cube nikalna like 2**2 i.e. 2 raise to power 2 =4 aur 2**3 i.e. 2 raise to power 3 =8 .

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

# type( ) function use hota hai datatype find karne ke liye
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
# Output:
# hello world hello world hello world
# <class 'str'> <class 'str'> <class 'str'>

# Reason of using Single Quotation,Double Quotation,Triple Quotation in a String with example
# z='i love python'
# print(z)
# Output:i love python
# z='i love's python'   
# print(z)
# Output:    z='i love's python' # single quotation ke andarr waapis se dusra single quotation use nahi kar sakte hai esliye double quotation use karna parta hai
#                             ^
# SyntaxError: unterminated string literal 
# z="i love's python"
# print(z)
# Output:i love's python
# z="i love
# python"
# print(z)
# Output:z="i love  #Long string ke liye triple quotation use karte hai
#          ^
# SyntaxError: unterminated string literal 
# z='''i love
# pyhton'''
# print(z)
# Output:i love
#        pyhton


# Function means ( ) aur Method means .( )
# string operation
# concatenation:
# x='i love python'
# y='program.'
# z=x+y
# print(z)
# Output:i love pythonprogram.
# print(x+y)
# Output:i love pythonprogram.

# replication:
# a="hellozaid "
# print(a*10) #edhar ten times "hello world" repeat hoga
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
# postive indexing start with '0' means from first word and negative indexing start with '-1' means from last word

# slicing
# In Python, slicing is a way to extract a portion of a sequence, such as a string, list, or tuple. The basic idea is to 
# specify a range of elements that you want to extract from the sequence. This range is defined by providing the starting index 
# and the ending index, separated by a colon.
# x="i love python program"
# print(x[start:end:step(default[1])]) #step by default 1 hoga
# positive slice
# number chahe positive ho ya negative ho start small index number se hona chahiye aur end greater index number se hona chahiye  
# agar start index number greater hai toh step:-1 legai aur agar start small index number hai toh step:1 legai.
# starting ka index number '0' hamesha include hoga but last ka index number include nhi hoga exlude hoga for ex:
# '7' liye index number end ka woh include nhi hoga exclude hoke '6' index number tak ka include hoga like an array.
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
# # startswith use hota hai check karne ke liye ki element particular word ke saath start hora hai ki nahi(answer True ya False mai aayega)
# print(s.startswith("i"))
# Output:True
# print(s.startswith("o"))
# Output:False
# # endswith use hota hai check karne ke liye ki element particular word ke saath end hora hai ki nahi(answer True ya False mai aayega)
# print(s.endswith("m"))
# Output:True
# print(s.endswith("a"))
# Output:False

# s="It is python program"
# # replace use hoga 'is' ko "it's" se replace karne ke liye
# print(s.replace("is","it's"))
# Output:It it's python program
# # swapcase capital words ko small words mai convert kar dega aur small words ko capital words mai convert kar dega jitne bhi elements hai unko
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
# # names=("karan","priya","kunal","pankaj",2) isme integer bhi le sakte hai woh bhi allow karta hai string ke saath.
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

# yeh bhi tuple he hai circle bracket nahi hai yeh sochke confuse mat hojana tuple ka main definition he hai separated by ',' 
# toh iss wajah se yeh bhi tuple he hai integer mat samajhna isey
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

# List(pura same hai yeh tuple ke jaisa bas method iske kam hai compare to tuple)
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
# # saath mai merge kar sakta hai but concatenation mai same datatypes chahiye rehta hai different datatypes nhi chalta hai
# difference between append and extend  list method in python with simple english words (5 points)
# Certainly! Here are five key points explaining the difference between the `append` and `extend` methods in Python lists using simple language:

# 1. **Adding Elements:**
#    - **Append:** Adds a single element to the end of the list.
#    - **Extend:** Adds multiple elements, such as elements of another iterable (list, tuple, etc.), to the end of the list.

# 2. **Input Type:**
#    - **Append:** Takes a single argument, which can be any data type (number, string, object, etc.).
#    - **Extend:** Takes an iterable (list, tuple, etc.) as its argument.

# 3. **Effect on Original List:**
#    - **Append:** Modifies the original list by adding the specified element at the end.
#    - **Extend:** Modifies the original list by adding all elements from the iterable at the end.

# 4. **Usage Example:**
#    - **Append:** `my_list.append(5)` adds the number 5 to the end of the list.
#    - **Extend:** `my_list.extend([6, 7, 8])` adds the elements 6, 7, and 8 to the end of the list.

# 5. **Multiple Elements:**
#    - **Append:** Only adds one element at a time.
#    - **Extend:** Can add multiple elements at once, making it efficient for combining lists.
# In summary, `append` adds a single element, while `extend` adds multiple elements from an iterable to the end of the list.

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
# # index number 1 pai 50 add kiya hai (index_number,insert_new_value)
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
# # yeh use hota hai reverse karne ke liye element ko but jaisa woh sorted hai waise he same sorted way mai reverse hokai elements aayega
# mylist.reverse()
# print(mylist)
# Output:[11, 9, 8, 7, 10, 5, 3, 2, 1]       
# # sort karega element ko based on ascending order(chhote se bada order)
# mylist.sort()
# print(mylist)
# Output:[1, 2, 3, 5, 7, 8, 9, 10, 11]       
# # reverse=True means yeh descending order mai sort karega element ko aur by default yeh reverse=False hota  hai
# toh descending order mai reverse karne ke liye reverse=True daalna parta hai(bade se chhota order)
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
# Output:i love python programming       # Python mai by default string hota hai
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
# # dictionary is a collection of key value pairs which is enclosed or surrounded by curly braces'{ }' and separated by ','
# # dictionary mai key hamesha immutable hota hai means woh belong karta hai numeric,string,tuple and boolean immutable datatypes se aur 
# # value mutable ya immutable dono ho sakta hai.
# # d={"key":   value}
#        |        |
#        v        v
#      {immutable,mutable}
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
# # yeh list of tuples dikhata hai means key aur value dono but with circle bracket
# print(info.items())
# Output:dict_items([('name', 'karan'), ('email', 'azaid@gmail.com'), ('password', '2234asdf')])
# # get method se particular 'key' daalke uska 'value' show kar sakte hai
# print(info.get("name"))
# Output:karan
# # iss tarha se bhi key ke values show kar sakte hai
# print(info["name"])
# Output:karan

# # difference between get operation and get method
# # yeh get operation hai isme agar joh key nhi hai means defined kiya huwa nhi hai  woh daalegai toh error aayega
# print(info["fullname"])    #ismey direct 'key' defined karke values nikalte hai
# Output:print(info["fullname"])
#              ~~~~^^^^^^^^^^^^
# KeyError: 'fullname'
# # yeh get method hai isme agar joh key nhi hai means defined kiya huwa nhi hai woh daalegai toh error nhi aayega  
# print(info.get("name","hello"))  #ismey bhi 'key' defined karke he values nikalte hai but .get( ) bhi lagate hai saath mai
# Output:karan
# # isme hello daal diye hai toh woh dikhayega
# print(info.get("fullname","hello"))
# Output:hello
# # isme none dikhayega kyu ki kuch nahi diye hai aur "fullname" defined key nahi hai dictionay mai
# print(info.get("fullname"))
# Output:None

# # but 'get opeartion' aur 'get method' yeh dono single key value pair add karte hai.
# # isme age:24 add kar diye hai dictionary mai
# info.setdefault("age",24)
# print(info)
# Output:{'name': 'karan', 'email': 'azaid@gmail.com', 'password': '2234asdf', 'age': 24}
# # isme city:thane add kiye hai dictionary mai 
# info["city"]="thane"
# print(info)
# Output:{'name': 'karan', 'email': 'azaid@gmail.com', 'password': '2234asdf', 'age': 24, 'city': 'thane'}

# # update bhi used hota hai add karne ke liye 'key value' pair dictionary mai but edhar mutilpe key value pairs  add kar sakte hai

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
# set is a collection of unique values but without key value pairs and it is enclosed or surrounded by '{ }' and separated by ','
# set mai elemenet immutable datatypes hote hai but set mutable datatypes hota hai means element belong karte hai immutable datatypes se

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
# set ke elements immutable datatypes se belong karte hai esliye edhar error aara hai list ko set ke andarr daalne pai as an elements
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
# x=x+5   #edhar previous 'x' ki value laikai addition karega(x=10)
# print(x)
# Output:15
# x+=5      #edhar previous 'x' ki value laikai addition karega(x=10)
# print(x)
# Output:15

x=10
# x=x-5          #edhar previous 'x' ki value laikai subtraction karega(x=10)              
# print(x)
# Output:5
# x-=5           #edhar previous 'x' ki value laikai subtraction karega(x=10)     
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
# if,elif,else
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

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# if(a>b):
#     print("a is greater")
# else:
#     print("b is greater")    
# Output:Enter first number: 23
#        Enter second number: 2
#        a is greater

# Output:Enter first number: 2
#        Enter second number: 23
#        b is greater
    
# example of if,elif and else
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# if(a>b):
#      print("a>b")
# elif(b>a):
#      print("b>a")
# else:
#      print("a==b")    
# Output:Enter first number: 23
#        Enter second number: 20
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
# Output:enter first number23
#        enter second number3
#        a>b
#        a==b
# Output:enter first number2
#        enter second number23
#        b>a 
# Output:enter first number23
#        enter second number23
#        a==b  


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
# and operator(dono conditon true chahiye toh true milega otherwise false milega agar ek bhi false hai toh)
# print(True and True)    
# Output:True
# print(False and True)
# Output:False
# print(False and False)
# Output:False

# or operator(koi bhi ek condition true rahega toh true milega)
# print(True or True)    
# Output:True
# print(False or True)
# Output:True
# print(False or False)
# Output:False

# 'or' and 'and' operator combination
# print(True or False and True)
# Output:True 
# print(True or True and False)
# Output:True 

# and operator
# print(10>2 and 10<20)
# Output:True
# print(10>2 and 10<8)
# Output:False

# or operator
# print(10>2 or 10<20)
# Output:True
# print(10>2 or 10<8)
# Output:True

# not(true ka false hoga aur false ka true hoga means ulta hoga)
# print(not True)
# Output:False
# print(not 10>2)
# Output:False

# program
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

# Leap year program
# take year from user and check it is leap year or not
# basic leap year code but not valid
# year=1996
# if(year%4==0):
#     print(f'year{year} is leap year')
# else:
#     print(f'year{year} is not leap year')   
#  Output:year1996 is leap year
    
# Leap year code but valid(accurate method)
# if(year%4==0 and year%100!=0):
#     print(f'year{year} is leap year')
# elif(year%400==0):    
#     print(f'year{year} is leap year')
# else:
#         print(f'year{year} is not leap year')
# Output:year1996 is leap year

# Leap year code but valid( with 'or' operator) (accurate method)
# if(year%4==0 and year%100!=0)or (year%400==0):
#     print(f'year{year} is leap year')
# else:
#         print(f'year{year} is not leap year')
# Output:year1996 is leap year

# User input leap year code
# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f'Year {year} is a leap year.')
# else:
#     print(f'Year {year} is not a leap year.')
# Output:Enter a year: 2004
# Year 2004 is a leap year.

# Ternary operator 
# x=10
# result="hello" if x%2==0 else "bye"
# print(result)
# Output:hello

# User input
# x = int(input("Enter a number: "))
# result="hello" if x%2==0 else "bye"
# print(result)
# Output:Enter a number: 11
# bye

# Leap year using ternary operator
# year = int(input("Enter a year: "))

# result = "Leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a leap year"

# print(result)
# Output:Enter a year: 2024
# Leap year
# Enter a year: 2023
# Not a leap year

# write a program to check whether a person is eligible for voting or not(accept age from the user)
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote yet.")
# Output:Enter your age: 24
# You are eligible to vote.

# write a program to check whether a number entered by a user is even or odd
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")
# Output:Enter a number: 24
# 24 is an even number.

# write a program to check whether a number is divisible by 7 or not

# number = int(input("Enter a number: "))

# if number % 7 == 0:
#     print(f"{number} is divisible by 7.")
# else:
#     print(f"{number} is not divisible by 7.")
#Output: Enter a number: 49
# 49 is divisible by 7.

# write a program to display "Hello" if a number entered by user is a multiple of five otherwise print "Bye"

# number = int(input("Enter a number: "))

# if number % 5 == 0:
#     print("Hello")
# else:
#     print("Bye")
# Output:Enter a number: 25
# Hello
# Output:Enter a number: 63
# Bye

# write a program to calculate the electricity bill(accept number  of unit from user) according to the following criteria: 
# Unit:                           Price:
# first 100 units                 no charge
# next 100 units                  Rs 5 per unit
# after 200 units.                Rs 10 per unit.
# (For example if input unit is 350 then total bill amount is Rs 2000)

# units=350

#if (units>=0 and units<=100):  # first 100 units ka no charge hai means free 
#    print("no charge")
#elif (units>=101 and units<=200):  #yaha pai 100 units tak ke andarr ka joh bhi aayega woh no charge rahega aur baki ka 100 units ke uppar ka number multiply hojayega
# # 5 se
#     units=units-100
#     print("total price-: ",units*5)
#elif (units>=201): #edhar 101 se 200 tak ka joh number rahega woh multiply hojayega 5 se aur 200 units ke uppar ka number add hojayega 10 se aur dono add hoke 
# # aajayega answer 
#     fg=100*5
#     units=units-200
#     total_price=fg+(units*10)
#     print(f"Total Price : {total_price}")    
#else:
#     print("invalid units")    
#Output:Total Price : 2000
    
# write a program to check whether the last digit of a number(entered by user)is divisible by 3 or not

# number = int(input("Enter a number: "))

# last_digit = abs(number) % 10

# if last_digit % 3 == 0:
#     print(f"The last digit {last_digit} is divisible by 3.")
# else:
#     print(f"The last digit {last_digit} is not divisible by 3.")
# Output:Enter a number: 24
# The last digit 4 is not divisible by 3.
# Output:Enter a number: 23
# The last digit 3 is divisible by 3.

# write a program to determine whether a number(accepted from the user) is divisible by 2 and 3 both

# number = int(input("Enter a number: "))

# if number % 2 == 0 and number % 3 == 0:
#     print(f"{number} is divisible by both 2 and 3.")
# else:
#     print(f"{number} is not divisible by both 2 and 3.")
# Output:Enter a number: 24
# 24 is divisible by both 2 and 3.
# Output:Enter a number: 53
# 53 is not divisible by both 2 and 3.

# accept the age of 4 people and display the youngest one?

# age1 = int(input("Enter the age of person 1: "))
# age2 = int(input("Enter the age of person 2: "))
# age3 = int(input("Enter the age of person 3: "))
# age4 = int(input("Enter the age of person 4: "))

# if age1 <= age2 and age1 <= age3 and age1 <= age4:
#     youngest_age = age1
# elif age2 <= age1 and age2 <= age3 and age2 <= age4:
#     youngest_age = age2
# elif age3 <= age1 and age3 <= age2 and age3 <= age4:
#     youngest_age = age3
# else:
#     youngest_age = age4

# print(f"The youngest person is {youngest_age} years old.")
# Output:Enter the age of person 1: 24
# Enter the age of person 2: 43
# Enter the age of person 3: 20
# Enter the age of person 4: 100
# The youngest person is 20 years old.

# accept the age of 4 people and display the Oldest one?

# age1 = int(input("Enter the age of person 1: "))
# age2 = int(input("Enter the age of person 2: "))
# age3 = int(input("Enter the age of person 3: "))
# age4 = int(input("Enter the age of person 4: "))

# if age1 >= age2 and age1 >= age3 and age1 >= age4:
#     oldest_age = age1
# elif age2 >= age1 and age2 >= age3 and age2 >= age4:
#     oldest_age = age2
# elif age3 >= age1 and age3 >= age2 and age3 >= age4:
#     oldest_age = age3
# else:
#     oldest_age = age4

# print(f"The oldest person is {oldest_age} years old.")
# Output:Enter the age of person 1: 40
# Enter the age of person 2: 100
# Enter the age of person 3: 18
# Enter the age of person 4: 19           
# The oldest person is 100 years old.

# write a program to check whether a year is leap year or not

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# Output:Enter a year: 2024
# 2024 is a leap year.
# Output:Enter a year: 2023
# 2023 is not a leap year.

# write a program to check whether a number entered is three digit number or not

# number = int(input("Enter a number: "))

# if 100 <= number <= 999:
#     print(f"{number} is a three-digit number.")
# else:
#     print(f"{number} is not a three-digit number.")

# Output: Enter a number: 333
# 333 is a three-digit number.
# Output:Enter a number: 34
# 34 is not a three-digit number.
    
# match case(switch case) #possible values ke liye kaam aata hai yeh,isme logical operator type ka function operate nahi kar sakte hai means logical programs nahi kar
# sakte hai aur if,elif aur else statement mai logical opearator ka kaam kar sakte hai.

# n1=int(input("Enter first number: "))
# n2=int(input("Enter second number: "))
# op=input("Enter the operator(+,-,*): ")

# match op:
#     case "+":
#         print(n1+n2)
#     case "-":
#         print(n1-n2)
#     case "*":
#         print(n1*n2)  
#     case _:                       #default hai yeh
#         print("invalid operator") 
#Output:Enter first number: 2
# Enter second number: 3
# Enter the operator(+,-,*): +
# 5    

# if True:
#     print("hello")
# else:
#     print("bye")    
#Output: hello
    
# if 10:
#     print("hi")
# else:
#     print("bye")
#Output: hi

# if 0:
#     print("hi")
# else:
#     print("bye")
#Output: bye

# if -10:
#     print("hi")
# else:
#     print("bye")    
#Output: hi

# if "hi":
#     print("hi")
# else:
#     print("bye")
#Output:hi
    
# if "":
#     print("hi")
# else:
#     print("bye")    
# Output:bye
    
# if " ":
#     print("hi")
# else:
#     print("bye") 
# Output:hi
   

# if False:
#     print("hi")
# else:
#     print("bye")    
# Output:bye

# if None:
#     print("hi")
# else:
#     print("bye")    
# Output:bye

# #  0,false,None,"" or [] any

# name=input("enter name")

# if name:
#     print(f"hello {name}")
# else:
#     print("error") 
# Output:enter namezaid
# hello zaid

# data=[1]

# if data:
#     print("data exist")
# else:
#     print("error")    
# Output:data exist

# data=[]

# if data:
#     print("data exist")
# else:
#     print("error")    
# Output:error

# print(bool(""))
# Output:False

# print(bool(" "))
# Output:True

# print(bool(0)) 
# Output:False

# homework

# x=5
# if(x>10):
#     print("Done")
# else:
#     print("TY")    
# Output:TY

# if(x):
#     print("Done")
# else:
#     print("TY")    
# Output:Done

# if(" "):
#     print("Done")
# else:
#     print("TY")    
# Output:Done

# if(4):
#     print("Done")
# else:
#     print("TY")      
# Output:Done

# if(""):
#     print("Done")
# else:
#     print("TY")    
# Output:TY

# if(None):
#     print("Done")
# else:
#     print("TY")    
# Output:TY
    
# if(0):
#     print("Done")
# else:
#     print("TY") 
# Output:TY 

# if(pass):
#     print("Done")
# else:
#     print("TY")    
# Output:if(pass):
#           ^^^^
# SyntaxError: invalid syntax

# if("Hi"):
#     print("Done")
# else:
#     print("TY")
# Output:Done
    
# if("."):
#     print("Done")
# else:
#     print("TY")    
# Output:Done

# x=1
# if(x<5):
#     x=x+1
#     print(x)
#     continue
# Output:continue
#        ^^^^^^^^
# SyntaxError: 'continue' not properly in loop

# x=1
# if(x<5):
#     x=x+1
#     print(x)
#     if(x==3):
#         break 
#     continue
#  Output:break 
#         ^^^^^
# SyntaxError: 'break' outside loop

# x=5
# if(x>5):
#     if("Hi"):
#         print("Done")
#     else:
#         print("TY")
# else:
#     if(x>=5):
#         if(5):
#             print("five")
#         else:
#             print("Not True")
#     else:
#         print("yes")  
# Output: five

# x=5
# if(x<5):
#     if(x!=0):
#         print("me")
#     else:
#         print("this")
# else:
#     if(x<=5):
#             print("yes")
#             if(x==5):
#                  print("Done")
#             else:
#                  print("okay")
# Output: yes 
#         Done

# Again same code

# write a program to check whether a person is eligible for voting or not(accept age from the user)
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote yet.")
# Output:Enter your age: 24
# You are eligible to vote.

# write a program to check whether a number entered by a user is even or odd
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")
# Output:Enter a number: 24
# 24 is an even number.

# write a program to check whether a number is divisible by 7 or not

# number = int(input("Enter a number: "))

# if number % 7 == 0:
#     print(f"{number} is divisible by 7.")
# else:
#     print(f"{number} is not divisible by 7.")
#Output: Enter a number: 49
# 49 is divisible by 7.

# write a program to display "Hello" if a number entered by user is a multiple of five otherwise print "Bye"

# number = int(input("Enter a number: "))

# if number % 5 == 0:
#     print("Hello")
# else:
#     print("Bye")
# Output:Enter a number: 25
# Hello
# Output:Enter a number: 63
# Bye

# write a program to calculate the electricity bill(accept number  of unit from user) according to the following criteria: 
# Unit:                           Price:
# first 100 units                 no charge
# next 100 units                  Rs 5 per unit
# after 200 units.                Rs 10 per unit.
# (For example if input unit is 350 then total bill amount is Rs 2000)

# units=350

#if (units>=0 and units<=100):  # first 100 units ka no charge hai means free 
#    print("no charge")
#elif (units>=101 and units<=200):  #yaha pai 100 units tak ke andarr ka joh bhi aayega woh no charge rahega aur baki ka 100 units ke uppar ka number multiply hojayega
# # 5 se
#     units=units-100
#     print("total price-: ",units*5)
#elif (units>=201): #edhar 101 se 200 tak ka joh number rahega woh multiply hojayega 5 se aur 200 units ke uppar ka number add hojayega 10 se aur dono add hoke 
# # aajayega answer 
#     fg=100*5
#     units=units-200
#     total_price=fg+(units*10)
#     print(f"Total Price : {total_price}")    
#else:
#     print("invalid units")    
#Output:Total Price : 2000
    
# write a program to check whether the last digit of a number(entered by user)is divisible by 3 or not

# number = int(input("Enter a number: "))

# last_digit = abs(number) % 10

# if last_digit % 3 == 0:
#     print(f"The last digit {last_digit} is divisible by 3.")
# else:
#     print(f"The last digit {last_digit} is not divisible by 3.")
# Output:Enter a number: 24
# The last digit 4 is not divisible by 3.
# Output:Enter a number: 23
# The last digit 3 is divisible by 3.

# write a program to determine whether a number(accepted from the user) is divisible by 2 and 3 both

# number = int(input("Enter a number: "))

# if number % 2 == 0 and number % 3 == 0:
#     print(f"{number} is divisible by both 2 and 3.")
# else:
#     print(f"{number} is not divisible by both 2 and 3.")
# Output:Enter a number: 24
# 24 is divisible by both 2 and 3.
# Output:Enter a number: 53
# 53 is not divisible by both 2 and 3.

# accept the age of 4 people and display the youngest one?

# age1 = int(input("Enter the age of person 1: "))
# age2 = int(input("Enter the age of person 2: "))
# age3 = int(input("Enter the age of person 3: "))
# age4 = int(input("Enter the age of person 4: "))

# if age1 <= age2 and age1 <= age3 and age1 <= age4:
#     youngest_age = age1
# elif age2 <= age1 and age2 <= age3 and age2 <= age4:
#     youngest_age = age2
# elif age3 <= age1 and age3 <= age2 and age3 <= age4:
#     youngest_age = age3
# else:
#     youngest_age = age4

# print(f"The youngest person is {youngest_age} years old.")
# Output:Enter the age of person 1: 24
# Enter the age of person 2: 43
# Enter the age of person 3: 20
# Enter the age of person 4: 100
# The youngest person is 20 years old.

# accept the age of 4 people and display the Oldest one?

# age1 = int(input("Enter the age of person 1: "))
# age2 = int(input("Enter the age of person 2: "))
# age3 = int(input("Enter the age of person 3: "))
# age4 = int(input("Enter the age of person 4: "))

# if age1 >= age2 and age1 >= age3 and age1 >= age4:
#     oldest_age = age1
# elif age2 >= age1 and age2 >= age3 and age2 >= age4:
#     oldest_age = age2
# elif age3 >= age1 and age3 >= age2 and age3 >= age4:
#     oldest_age = age3
# else:
#     oldest_age = age4

# print(f"The oldest person is {oldest_age} years old.")
# Output:Enter the age of person 1: 40
# Enter the age of person 2: 100
# Enter the age of person 3: 18
# Enter the age of person 4: 19           
# The oldest person is 100 years old.

# write a program to check whether a year is leap year or not

# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")

# Output:Enter a year: 2024
# 2024 is a leap year.
# Output:Enter a year: 2023
# 2023 is not a leap year.

# write a program to check whether a number entered is three digit number or not

# number = int(input("Enter a number: "))

# if 100 <= number <= 999:
#     print(f"{number} is a three-digit number.")
# else:
#     print(f"{number} is not a three-digit number.")

# Output: Enter a number: 333
# 333 is a three-digit number.
# Output:Enter a number: 34
# 34 is not a three-digit number.

# A loop is used to execute a certain block of code until it's condition is met but if condition is not met it will automatically stopped looping.
# There are two types of loop in python are:
# 1)While loop
# 2)For loop
# While loop

# while(True):
#     print("hi")
#     print("hello")
#     print("bye")
# Output:hi
#        hello
#        bye
#        hi
#        hello
#        bye
#        hi
#        hello
#        bye
# aise aata rahega toh apne ko interrupt karna parega
# Traceback (most recent call last):
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 1786, in <module>
# print("bye")
# KeyboardInterrupt(ctrl+c in terminal)

# while(False):
#     print("hi")
#     print("hello")
#     print("bye")
# Output:"

# x=10
# while(x>2):
#     print("hi")
#     print("hello")
#     print("bye")
# Output:hi
#        hello
#        bye
#        hi
#        hello
#        bye
#        hi
#        hello
#        bye
# aise aata rahega toh apne ko interrupt karna parega
# Traceback (most recent call last):
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 1786, in <module>
# print("bye")
# KeyboardInterrupt

# x=1
# while(x<=10):
#     print("hi")
#     print("hello")
#     print("bye")
# Output:hi
#        hello
#        bye
#        hi
#        hello
#        bye
#        hi
#        hello
#        bye
# aise aata rahega toh apne ko interrupt karna parega
# Traceback (most recent call last):
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 1786, in <module>
# print("bye")
# KeyboardInterrupt

# Actual While loop code(means valid)(10 times print "hi","hello","bye")
# x=1
# while(x<=10):
#     print("hi")
#     print("hello")
#     print("bye")
#     x+=1                       # x=1  x<=10 ->True-> hi,hello,bye->  x+=1    x=2<-(aisa iterate hoga edhar aur check karega condition edhar)
# print("out of loop")    
# Output:hi   
#        hello
#        bye  
#        hi   
#        hello
#        bye  
#        hi   
#        hello
#        bye  
#        hi   
#        hello
#        bye
#        hi
#        hello
#        bye
#        hi
#        hello
#        bye
#        hi
#        hello
#        bye
#        hi
#        hello
#        bye
#        hi
#        hello
#        bye
#        hi
#        hello
#        bye
#        out of loop

# iterable(10 times run "hi","hello","bye")
# x=1  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=2

# x=2  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=3

# x=3  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=4

# x=4  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=5

# x=5  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=6

# x=6  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=6

# x=6  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=7

# x=7  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=8

# x=8  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=9

# x=9  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=10

# x=10  x<=10 ->True
#   hi,hello,bye
#   x+=1    x=11

# x=11  x<=10 ->False
#   out of loop

# print 1 to 10 number program
# counter = 1

# while counter <= 10:
#     print(counter)
#     counter += 1  # Increment the counter
# Output:1 
#        2 
#        3 
#        4 
#        5 
#        6 
#        7 
#        8 
#        9 
#       10

# iterable 1
# counter=1  
# 1<=10->True
# print(1)
# counter += 1      counter=2

# iterable 2
# counter=2 
# 2<=10->True
# print(2)
# counter += 1      counter=3

# iterable 3
# counter=3 
# 3<=10->True
# print(3)
# counter += 1      counter=4

# iterable 4
# counter=4
# 4<=10->True
# print(4)
# counter += 1      counter=5

# iterable 5
# counter=5 
# 5<=10->True
# print(5)
# counter += 1      counter=6

# iterable 6
# counter=6 
# 6<=10->True
# print(6)
# counter += 1      counter=7

# iterable 7
# counter=7
# 7<=10->True
# print(7)
# counter += 1      counter=8

# iterable 8
# counter=8 
# 8<=10->True
# print(8)
# counter += 1      counter=9

# iterable 9
# counter=9 
# 9<=10->True
# print(9)
# counter += 1      counter=`10

# iterable 10
# counter=10 
# 10<=10->True
# print(10)
# counter += 1      counter=11

# iterable 11
# counter=11 
# 11<=10->False

# print 10 to 1 reverse  number program
# counter = 10

# while counter >= 1:
#     print(counter)
#     counter -= 1  # Decrement the counter
# Output:10
#        9
#        8
#        7
#        6
#        5
#        4
#        3
#        2
#        1

# iterable(# print 10 to 1 reverse  number program)
# counter=10  counter>=1 ->True
#   10
#   counter-=1    counter=9

# counter=9  counter>=1 ->True
#   9
#   counter-=1    counter=8

# counter=8  counter>=1 ->True
#   8
#   counter-=1    counter=7

# counter=7  counter>=1 ->True
#   7
#   counter-=1    counter=6

# counter=6  counter>=1 ->True
#   6
#   counter-=1    counter=5

# counter=5 counter>=1 ->True
#   5
#   counter-=1    counter=4

# counter=4  counter>=1 ->True
#   4
#   counter-=1    counter=3

# counter=3  counter>=1 ->True
#   3
#   counter-=1    counter=2

# counter=2  counter>=1 ->True
#   2
#   counter-=1    counter=1

# counter=1  counter>=1 ->True
#   1
#   counter-=1    counter=0

# counter=0  counter>=1 ->False


# Use a while loop to print even numbers from 1 to 10

# counter = 1

# while counter <= 10:
#     if counter % 2 == 0:
#         print(counter)
#     counter += 1  # Increment the counter
# Output:2
#        4
#        6
#        8
#        10

# iterable
# counter=1  counter<=10->True
# 1%2==0->1 remainder->False
# counter +=1    counter=2

# counter=2  counter<=10->True
# 2%2==0->0 remainder->True
# print(counter)->2
# counter +=1    counter=3
    
# counter=3  counter<=10->True
# 3%2==0->1 remainder->False
# counter +=1    counter=4

# counter=4  counter<=10->True
# 4%2==0->0 remainder->True
# print(counter)->4
# counter +=1    counter=5

# counter=5  counter<=10->True
# 5%2==0->1 remainder->False
# counter +=1    counter=6

# counter=6  counter<=10->True
# 6%2==0->0 remainder->True
# print(counter)->6
# counter +=1    counter=7

# counter=7  counter<=10->True
# 7%2==0->1 remainder->False
# counter +=1    counter=8

# counter=8  counter<=10->True
# 8%2==0->0 remainder->True
# print(counter)->8
# counter +=1    counter=9

# counter=9  counter<=10->True
# 9%2==0->1 remainder->False
# counter +=1    counter=10
    
# counter=10  counter<=10->True
# 10%2==0->0 remainder->True
# print(counter)->10
# counter +=1    counter=11

# counter=11  counter<=10->False
    
# print even number from 1 to 10 and if even number is not occur then print "hello"

# n=1
# while(n<=10):
#     if(n%2==0):
#         print(n)
#     else:
#         print("hello")
#     n=n+1        
# Output:hello
#        2
#        hello
#        4
#        hello
#        6
#        hello
#        8
#        hello
#        10 
    
# iterable(# print even number from 1 to 10 and if even number is not occur then print "hello")
    
# n=1 n<=10->True
# 1%2==0->remainder 1->False
# print("hello")
# n=n+1 n=2
    
# n=2 n<=10->True
# 2%2==0->remainder 0->True
# print(2)
# n=n+1 n=3
    
# n=3 n<=10->True
# 3%2==0->remainder 1->False
# print("hello")
# n=n+1 n=4

# n=4 n<=10->True
# 4%2==0->remainder 0->True
# print(4)
# n=n+1 n=5

# n=5 n<=10->True
# 5%2==0->remainder 1->False
# print("hello")
# n=n+1 n=6

# n=6 n<=10->True
# 6%2==0->remainder 0->True
# print(6)
# n=n+1 n=7

# n=7 n<=10->True
# 7%2==0->remainder 1->False
# print("hello")
# n=n+1 n=8

# n=8 n<=10->True
# 8%2==0->remainder 0->True
# print(8)
# n=n+1 n=9

# n=9 n<=10->True
# 9%2==0->remainder 1->False
# print("hello")
# n=n+1 n=10

# n=10 n<=10->True
# 10%2==0->remainder 0->True
# print(10)
# n=n+1 n=11

# n=11 n<=10->False

# Use a while loop to print numbers from 1 to 20 that are divisible by both 2 and 3

# number = 1

# while number <= 20:
#     if number % 2 == 0 and number % 3 == 0:
#         print(number)
#     number += 1  # Increment the number in each iteration
# Output:6
#        12
#        18

# iterable 1(# Use a while loop to print numbers from 1 to 20 that are divisible by both 2 and 3)
# number=1 
# 1<=20->True
# 1%2==0->1remainder->False 
# number +=1   number=2

# iterable 2 
# number=2 
# 2<=20->True
# 2%2==0->0remainder->True and 2%3==0->2remainder->False
# number +=1   number=3

# iterable 3 
# number=3 
# 3<=20->True
# 3%2==0->1remainder->False
# number +=1   number=4

# iterable 4 
# number=4 
# 4<=20->True
# 4%2==0->0remainder->True and 4%3==0->1remainder->False
# number +=1   number=5

# iterable 5 
# number=5 
# 5<=20->True
# 5%2==0->1remainder->False
# number +=1   number=6

# iterable 6 
# number=6 
# 6<=20->True
# 6%2==0->0remainder->True and 6%3==0->0remainder->True
# print(6)
# number +=1   number=7

# iterable 7 
# number=7
# 7<=20->True
# 7%2==0->1remainder->False
# number +=1   number=8

# iterable 8 
# number=8
# 8<=20->True
# 8%2==0->0remainder->True and 8%3==0->2remainder->False
# number +=1   number=9

# iterable 9
# number=9
# 9<=20->True
# 9%2==0->1remainder->False
# number +=1   number=10

# iterable 10
# number=10
# 10<=20->True
# 10%2==0->0remainder->True and 10%3==0->1remainder->False
# number +=1   number=11

# iterable 11
# number=11
# 11<=20->True
# 11%2==0->1remainder->False
# number +=1   number=12

# iterable 12
# number=12
# 12<=20->True
# 12%2==0->0remainder->True and 6%3==0->0remainder->True
# print(12)
# number +=1   number=13

# iterable 13
# number=13
# 13<=20->True
# 13%2==0->1remainder->False
# number +=1   number=14

# iterable 14
# number=14
# 14<=20->True
# 14%2==0->0remainder->True and 14%3==0->2remainder->False
# number +=1   number=15

# iterable 15
# number=15
# 15<=20->True
# 15%2==0->1remainder->False
# number +=1   number=16

# iterable 16
# number=16
# 16<=20->True
# 16%2==0->0remainder->True and 16%3==0->1remainder->False
# number +=1   number=17

# iterable 17
# number=17
# 17<=20->True
# 17%2==0->1remainder->False
# number +=1   number=18

# iterable 18
# number=18
# 18<=20->True
# 18%2==0->0remainder->True and 18%3==0->0remainder->True
# print(18)
# number +=1   number=19

# iterable 19
# number=19
# 19<=20->True
# 19%2==0->1remainder->False
# number +=1   number=20

# iterable 20
# number=20
# 20<=20->True
# 20%2==0->0remainder->True and 20%3==0->2remainder->False
# number +=1   number=21

# iterable 21
# number=21
# 21<=20->False

# Use a while loop to iterate through numbers from 1 to 20(count how much times numbers occurs which is divisible by 2 and 3 both)

# Initialize variables
# number = 1
# count = 0

# while number <= 20:
#     # Check if the number is divisible by both 2 and 3
#     if number % 2 == 0 and number % 3 == 0:
#         print(number)
#         count += 1  # Increment the count
#     number += 1  # Increment the number in each iteration

# # Print the total count of numbers divisible by both 2 and 3
# print(f"Total count: {count}")

# output:6
#        12
#        18
#        Total count: 3

# iterble(# Use a while loop to iterate through numbers from 1 to 20)(count how much times numbers occurs which is divisible by 2 and 3 both)
# number=1  count=0
# 1<=20->True
# 1%2==0->remainder1->False
# number+=1  number=2

# number=2  count=0
# 2<=20->True
# 2%2==0->remainder0->True and 2%3==0->remainder1->False
# False
# number+=1  number=3

# number=3  count=0
# 3<=20->True
# 3%2==0->remainder1->False
# number+=1  number=4

# number=4  count=0
# 4<=20->True
# 4%2==0->remainder0->True and 4%3==0->remainder1->False
# False
# number+=1  number=5

# number=5  count=0
# 5<=20->True
# 5%2==0->remainder1->False
# number+=1  number=6

# number=6  count=0
# 6<=20->True
# 6%2==0->remainder0->True and 6%3==0->remainder0->True
# True
# print(6)
# count=1
# number+=1  number=7

# number=7  count=0
# 7<=20->True
# 7%2==0->remainder1->False
# number+=1  number=8

# number=8  count=0
# 8<=20->True
# 8%2==0->remainder0->True and 8%3==0->remainder1->False
# False
# number+=1  number=9

# number=9  count=0
# 9<=20->True
# 9%2==0->remainder1->False
# number+=1  number=10

# number=10  count=0
# 10<=20->True
# 10%2==0->remainder0->True and 10%3==0->remainder1->False
# False
# number+=1  number=11

# number=11  count=0
# 11<=20->True
# 11%2==0->remainder1->False
# number+=1  number=12

# number=12  count=0
# 12<=20->True
# 12%2==0->remainder0->True and 12%3==0->remainder0->True
# True
# print(12)
# count=2
# number+=1  number=13

# number=13  count=0
# 13<=20->True
# 13%2==0->remainder1->False
# number+=1  number=14

# number=14  count=0
# 14<=20->True
# 14%2==0->remainder0->True and 14%3==0->remainder1->False
# False
# number+=1  number=15

# number=15  count=0
# 15<=20->True
# 15%2==0->remainder1->False
# number+=1  number=16

# number=16  count=0
# 16<=20->True
# 16%2==0->remainder0->True and 16%3==0->remainder1->False
# False
# number+=1  number=17

# number=17  count=0
# 17<=20->True
# 17%2==0->remainder1->False
# number+=1  number=18

# number=18  count=0
# 18<=20->True
# 18%2==0->remainder0->True and 18%3==0->remainder0->True
# True
# print(18)
# count=3
# number+=1  number=19

# number=19  count=0
# 19<=20->True
# 19%2==0->remainder1->False
# number+=1  number=20

# number=20  count=0
# 20<=20->True
# 20%2==0->remainder0->True and 20%3==0->remainder1->False
# False
# number+=1  number=21

# number=21  count=0
# 21<=20->False

# Use a while loop to print each number separately using index number

# my_list = [12, 24, 25, 18, 19, 40, 55]

# # Initialize an index variable
# index = 0

# while index < len(my_list):
#     print(my_list[index])
#     index += 1  # Increment the index in each iteration

# iterable
# index=0
# index=0<len(7)->True
# print(12[0])
# index +=1   index=1

# index=1
# index=1<len(7)->True
# print(24[1])
# index +=1   index=2

# index=2
# index=2<len(7)->True
# print(25[2])
# index +=1   index=3

# index=3
# index=3<len(7)->True
# print(18[3])
# index +=1   index=4

# index=4
# index=4<len(7)->True
# print(19[4])
# index +=1   index=5

# index=5
# index=5<len(7)->True
# print(40[5])
# index +=1   index=6

# index=6
# index=6<len(7)->True
# print(55[6])
# index +=1   index=7

# index=7
# index=7<len(7)->False

# Homework 
# print sum of 1 to 10 number(previous number se sum hoga)

# # Use a while loop to calculate the cumulative sum
# # Initialize variables
# current_number = 1
# cumulative_sum = 0

# while current_number <= 10:
#     cumulative_sum += current_number
#     current_number += 1

# # Print the cumulative sum
# print(f"The cumulative sum of numbers from 1 to 10 is: {cumulative_sum}")
# Output:The cumulative sum of numbers from 1 to 10 is: 55
# Iteration 1: cumulative_sum = 1 (0 + 1)
# Iteration 2: cumulative_sum = 3 (1 + 2)
# Iteration 3: cumulative_sum = 6 (3 + 3)
# Iteration 4: cumulative_sum = 10 (6 + 4)
# ... and so on, until current_number becomes 11. The final result is the cumulative sum of numbers from 1 to 10, which is 55.

# iterable 1
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=1     cumulative_sum=0
# 1<=10->True
# cumulative_sum += 0+1->1
# current_number +=1   current_number=2

# iterable 2
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=2     cumulative_sum=1
# 2<=10->True
# cumulative_sum +=1+2->3
# current_number +=1   current_number=3

# iterable 3
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=3     cumulative_sum=3
# 3<=10->True
# cumulative_sum +=3+3->6
# current_number +=1   current_number=4

# iterable 4
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=4     cumulative_sum=6
# 4<=10->True
# cumulative_sum +=6+4->10
# current_number +=1   current_number=5

# iterable 5
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=5     cumulative_sum=10
# 5<=10->True
# cumulative_sum +=10+5->15
# current_number +=1   current_number=6

# iterable 6
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=6     cumulative_sum=15
# 6<=10->True
# cumulative_sum +=15+6->21
# current_number +=1   current_number=7

# iterable 7
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=7     cumulative_sum=21
# 7<=10->True
# cumulative_sum +=21+7->28
# current_number +=1   current_number=8

# iterable 8
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=8     cumulative_sum=28
# 8<=10->True
# cumulative_sum +=28+8->36
# current_number +=1   current_number=9

# iterable 9
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=9     cumulative_sum=36
# 9<=10->True
# cumulative_sum +=36+9->45
# current_number +=1   current_number=10

# iterable 10
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=10     cumulative_sum=45
# 10<=10->True
# cumulative_sum +=45+10->55
# current_number +=1   current_number=11

# iterable 11
# while current_number <= 10:
# cumulative_sum += current_number
# current_number += 1

# current_number=11    cumulative_sum=55
# 11<=10->False

# print 1 to 40 number which is divisble by 2 and 3 both and print sum of 1 to 40 which is divisible by 2 and 3 both
# Initialize variables
# number = 1
# count = 0
# total_sum = 0

# Use a while loop to iterate through numbers from 1 to 40
# while number <= 40:
#     # Check if the number is divisible by both 2 and 3
#     if number % 2 == 0 and number % 3 == 0:
#         print(number)
#         total_sum += number  # Add the number to the total sum
#         count += 1  # Increment the count
#     number += 1  # Increment the number in each iteration

# # Print the total count of numbers divisible by both 2 and 3
# print(f"Total count: {count}")

# # Print the sum of numbers divisible by both 2 and 3
# print(f"Sum of numbers divisible by both 2 and 3: {total_sum}")
# Output:6
# 12
# 18
# 24
# 30
# 36
# Total count: 6
# Sum of numbers divisible by both 2 and 3: 126

# iterable 1(# print 1 to 40 number which is divisble by 2 and 3 both and print sum of 1 to 40 which is divisible by 2 and 3 both)
# number=1 count=0  total_sum=0
# 1<=40->True
# 1%2==0->remainder1->False
# number+=1  number=2

# number=2  count=0  total_sum=0
# 2<=40->True
# 2%2==0->remainder0->True and 2%3==0->remainder2->False
# False
# number+=1  number=3

# number=3  count=0  total_sum=0
# 3<=40->True
# 3%2==0->remainder1->False
# number+=1  number=4

# number=4  count=0  total_sum=0
# 4<=40->True
# 4%2==0->remainder0->True and 4%3==0->remainder1->False
# False
# number+=1  number=5

# number=5  count=0  total_sum=0
# 5<=40->True
# 5%2==0->remainder1->False
# number+=1  number=6

# number=6  count=0  total_sum=0
# 6<=40->True
# 6%2==0->remainder0->True and 6%3==0->remainder0->True
# True
# print(6)
# total_sum=0+6->6
# count=1
# number+=1  number=7

# number=7  count=1   total_sum=6
# 7<=40->True
# 7%2==0->remainder1->False
# number+=1  number=8

# number=8  count=1   total_sum=6
# 8<=40->True
# 8%2==0->remainder0->True and 8%3==0->remainder1->False
# False
# number+=1  number=9

# number=9  count=1   total_sum=6
# 9<=40->True
# 9%2==0->remainder1->False
# number+=1  number=10

# number=10  count=1  total_sum=6
# 10<=40->True
# 10%2==0->remainder0->True and 10%3==0->remainder1->False
# False
# number+=1  number=11

# number=11  count=1  total_sum=6
# 11<=40->True
# 11%2==0->remainder1->False
# number+=1  number=12

# number=12  count=1  total_sum=6
# 12<=40->True
# 12%2==0->remainder0->True and 12%3==0->remainder0->True
# True
# print(12)
# total_sum=6+12->18
# count=2
# number+=1  number=13

# number=13  count=2  total_sum=18
# 13<=40->True
# 13%2==0->remainder1->False
# number+=1  number=14

# number=14  count=2  total_sum=18
# 14<=40->True
# 14%2==0->remainder0->True and 14%3==0->remainder1->False
# False
# number+=1  number=15

# number=15  count=2  total_sum=18
# 15<=40->True
# 15%2==0->remainder1->False
# number+=1  number=16

# number=16  count=2  total_sum=18
# 16<=40->True
# 16%2==0->remainder0->True and 16%3==0->remainder1->False
# False
# number+=1  number=17

# number=17  count=2  total_sum=18
# 17<=40->True
# 17%2==0->remainder1->False
# number+=1  number=18

# number=18  count=2   total_sum=18
# 18<=40->True
# 18%2==0->remainder0->True and 18%3==0->remainder0->True
# True
# print(18)
# total_sum=18+18->36
# count=3
# number+=1  number=19

# number=19  count=3   total_sum=36
# 19<=40->True
# 19%2==0->remainder1->False
# number+=1  number=20

# number=20  count=3   total_sum=36
# 20<=40->True
# 20%2==0->remainder0->True and 20%3==0->remainder2->False
# False
# number+=1  number=21

# number=21  count=3   total_sum=36
# 21<=40->True
# 21%2==0->remainder1->False
# number+=1  number=22

# number=22  count=3   total_sum=36
# 22<=40->True
# 22%2==0->remainder0->True and 22%3==0->remainder1->False
# False
# number+=1  number=23

# number=23  count=3   total_sum=36
# 23<=40->True
# 23%2==0->remainder1->False 
# number+=1  number=24

# number=24  count=3   total_sum=36
# 24<=40->True
# 24%2==0->remainder0->True and 24%3==0->remainder0->True
# True
# print(24)
# total_sum=36+24->60
# count=4
# number+=1  number=25

# number=25  count=4   total_sum=60
# 25<=40->True
# 25%2==0->remainder1->False 
# number+=1  number=26

# number=26  count=4   total_sum=60
# 26<=40->True
# 26%2==0->remainder0->True and 26%3==0->remainder2->False
# False
# number+=1  number=27

# number=27  count=4   total_sum=60
# 27<=40->True
# 27%2==0->remainder1->False 
# number+=1  number=28

# number=28  count=4   total_sum=60
# 28<=40->True
# 28%2==0->remainder0->True and 28%3==0->remainder1->False 
# False
# number+=1  number=29

# number=29  count=4   total_sum=60
# 29<=40->True
# 29%2==0->remainder1->False 
# number+=1  number=30

# number=30  count=4   total_sum=60
# 30<=40->True
# 30%2==0->remainder0->True  and 30%3==0->remainder0->True
# True
# print(30)
# total_sum=60+30->90
# count=5
# number+=1  number=31

# number=31  count=5   total_sum=90
# 31<=40->True
# 31%2==0->remainder1->False 
# number+=1  number=32

# number=32  count=5   total_sum=90
# 32<=40->True
# 32%2==0->remainder0->True  and 30%3==0->remainder2->False
# False
# number+=1  number=33
# number=33  count=5   total_sum=90
# 33<=40->True
# 33%2==0->remainder1->False
# number+=1  number=34

# number=34  count=5   total_sum=90
# 34<=40->True
# 34%2==0->remainder0->True  and 34%3==0->remainder1->False
# False
# number+=1  number=35

# number=35  count=5   total_sum=90
# 35<=40->True
# 35%2==0->remainder1->False 
# number+=1  number=36

# number=36  count=5   total_sum=90
# 36<=40->True
# 36%2==0->remainder0->True  and 36%3==0->remainder0->True
# True
# print(36)
# total_sum=90+36->126
# count=6
# number+=1  number=37

# number=37  count=6   total_sum=126
# 37<=40->True
# 37%2==0->remainder1->False 
# number+=1  number=38

# number=38  count=6   total_sum=126
# 38<=40->True
# 38%2==0->remainder0->True and 38%3==0->remainder2->False
# number+=1  number=39

# number=39  count=6   total_sum=126
# 39<=40->True
# 39%2==0->remainder1->False
# number+=1  number=40

# number=40  count=6   total_sum=126
# 40<=40->True
# 40%2==0->remainder0->True and 40%3==0->remainder1->False
# False
# number+=1  number=41

# number=41  count=6   total_sum=126
# 41<=40->False

# print even number from this list program

# Given list
# a = [12, 23, 4, 8, 18, 8]

# Initialize variables
# index = 0

# Use a while loop to print even numbers from the list
# while index < len(a):
#     if a[index] % 2 == 0:
#         print(a[index])
#     index += 1  # Increment the index in each iteration
# Output:12
# 4 
# 8 
# 18
# 8  

# iterable1(# Use a while loop to print even numbers from the list)
# a = [12, 23, 4, 8, 18, 8]
# index = 0
# 0 < len(6):->True
# a[0]12%2==0->remainder 0->True
# print(12)
# index +=1  index=1

# iterable2
# a = [12, 23, 4, 8, 18, 8]
# index = 1
# 1 < len(6):->True
# a[1]23%2==0->remainder 1->False
# index +=1  index=2

# iterable3
# a = [12, 23, 4, 8, 18, 8]
# index = 2
# 2 < len(6):->True
# a[2]4%2==0->remainder 0->True
# index +=1  index=3

# iterable4
# a = [12, 23, 4, 8, 18, 8]
# index = 3
# 3 < len(6):->True
# a[3]8%2==0->remainder 0->True
# index +=1  index=4

# iterable5
# a = [12, 23, 4, 8, 18, 8]
# index = 4
# 4 < len(6):->True
# a[4]18%2==0->remainder 0->True
# index +=1  index=5

# iterable6
# a = [12, 23, 4, 8, 18, 8]
# index = 5
# 5 < len(6):->True
# a[5]8%2==0->remainder 0->True
# index +=1  index=6

# iterable7
# a = [12, 23, 4, 8, 18, 8]
# index = 6
# 6 < len(6):->False

# Use a while loop to count and print leap years from the list
# Given list of years
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

# Initialize variables
# index = 0
# leap_year_count = 0

# while index < len(year):
#     y = year[index]
#     if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#         print(y)
#         leap_year_count += 1  # Increment the leap year count
#     index += 1  # Increment the index in each iteration

# # Print the total count of leap years
# print(f"Total count of leap years: {leap_year_count}")
# Output:2012
#        2016
#        2020
#        2024
#        Total count of leap years: 4

# iterable 1(# Use a while loop to count and print leap years from the list)
# index=0   leap_year_count=0
# 0<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][0]->2010
# if(2010%4==0->remainder2->False and 2010%100!=0->remainder10->True)->False or (2010%400==0)->remainder10->False
# index +=1   index=1


# Use a while loop to count and store leap years from the list
# Given list of years
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

# Initialize variables
# index = 0
# leap_year_count = 0
# leap_years = []  # Empty list to store leap years

# while index < len(year):
#     y = year[index]
#     if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#         print(y)
#         leap_years.append(y)  # Append the leap year to the list
#         leap_year_count += 1  # Increment the leap year count
#     index += 1  # Increment the index in each iteration

# # Print the total count of leap years
# print(f"Total count of leap years: {leap_year_count}")

# # Print the list of leap years
# print("List of leap years:", leap_years)
# Output:2012
#        2016
#        2020
#        2024
#        Total count of leap years: 4
#        List of leap years: [2012, 2016, 2020, 2024]


# iterable 1(# Use a while loop to count and store leap years from the list )
# index=0   leap_year_count=0   leap_years = []
# 0<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][0]->2010
# if(2010%4==0->remainder2->False and 2010%100!=0->remainder10->True)->False or (2010%400==0)->remainder10->False
# index +=1   index=1

# iterable 2
# index=1   leap_year_count=0   leap_years = []
# 1<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][1]->2011
# if(2011%4==0->remainder3->False and 2011%100!=0->remainder11->True)->False or (2011%400==0)->remainder11->False
# index +=1   index=2

# iterable 3
# index=2   leap_year_count=0   leap_years = []
# 2<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][2]->2012
# if(2012%4==0->remainder0->True and 2012%100!=0->remainder12->True)->True 
# print(2012)
# leap_years = [].append(2012)->[2012]
# leap_year_count=1
# index +=1   index=3

# iterable 4
# index=3   leap_year_count=1   leap_years = [2012]
# 3<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][3]->2013
# if(2013%4==0->remainder1->False and 2013%100!=0->remainder13->True)->False or (2013%400==0)->remainder13->False
# index +=1   index=4

# iterable 5
# index=4   leap_year_count=1   leap_years = [2012]
# 4<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][4]->2014
# if(2014%4==0->remainder2->False and 2014%100!=0->remainder14->True)->False or (2014%400==0)->remainder14->False
# index +=1   index=5

# iterable 6
# index=5   leap_year_count=1   leap_years = [2012]
# 5<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][5]->2015
# if(2015%4==0->remainder3->False and 2015%100!=0->remainder15->True)->False or (2015%400==0)->remainder15->False
# index +=1   index=6

# iterable 6
# index=6   leap_year_count=1   leap_years = [2012]
# 6<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][6]->2016
# if(2016%4==0->remainder0->True and 2016%100!=0->remainder16->True)->True 
# print(2016)
# leap_years = [2012].append(2016)->[2012,2016]
# leap_year_count=2
# index +=1   index=7

# iterable 7
# index=7   leap_year_count=2   leap_years = [2012,2016]
# 7<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][7]->2017
# if(2017%4==0->remainder1->False and 2017%100!=0->remainder17->True)->False or (2017%400==0)->remainder17->False
# index +=1   index=8

# iterable 8
# index=8   leap_year_count=2   leap_years = [2012,2016]
# 8<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][8]->2018
# if(2018%4==0->remainder2->False and 2018%100!=0->remainder18->True)->False or (2018%400==0)->remainder18->False
# index +=1   index=9

# iterable 9
# index=9   leap_year_count=2   leap_years = [2012,2016]
# 9<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][9]->2019
# if(2019%4==0->remainder3->False and 2019%100!=0->remainder19->True)->False or (2019%400==0)->remainder19->False
# index +=1   index=10

# iterable 10
# index=10   leap_year_count=2   leap_years = [2012,2016]
# 10<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][10]->2020
# if(2020%4==0->remainder0->True and 2020%100!=0->remainder20->True)->True 
# print(2020)
# leap_years = [2012,2016].append(2020)->[2012,2016,2020]
# leap_year_count=3
# index +=1   index=11

# iterable 11
# index=11   leap_year_count=3   leap_years = [2012,2016,2020]
# 11<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][11]->2021
# if(2021%4==0->remainder1->False and 2021%100!=0->remainder21->True)->False or (2021%400==0)->remainder21->False
# index +=1   index=12

# iterable 12
# index=12   leap_year_count=3   leap_years = [2012,2016,2020]
# 12<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][12]->2022
# if(2022%4==0->remainder4->False and 2022%100!=0->remainder22->True)->False or (2022%400==0)->remainder22->False 
# index +=1   index=13

# iterable 13
# index=13   leap_year_count=3   leap_years = [2012,2016,2020]
# 13<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][13]->2023
# if(2023%4==0->remainder3->False and 2023%100!=0->remainder23->True)->False or (2023%400==0)->remainder23->False
# index +=1   index=14

# iterable 14
# index=14   leap_year_count=3   leap_years = [2012,2016,2020]
# 14<len(15)->True
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# y=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024][14]->2024
# if(2024%4==0->remainder0->True and 2024%100!=0->remainder24->True)->True 
# print(2024)
# leap_years = [2012,2016,2020].append(2024)->[2012,2016,2020,2024]
# leap_year_count=4
# index +=1   index=15

# iterable 15
# index=15   leap_year_count=4   leap_years = [2012,2016,2020,2024]
# 15<len(15)->False

# Use a while loop to remove leap years from the list
#  Given list of years
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

# Initialize variables
# index = 0
# leap_years = []  # Empty list to store leap years

# while index < len(year):
#     y = year[index]
#     if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#         leap_years.append(year.pop(index))  # Remove and append the leap year from the list
#     else:
#         index += 1  # Increment the index if not a leap year

# Print the modified list without leap years
# print("List without leap years:", year)

# Print the list of leap years
# print("List of leap years removed:", leap_years)
# Output:
# List without leap years: [2010, 2011, 2013, 2014, 2015, 2017, 2018, 2019, 2021, 2022, 2023]
# List of leap years removed: [2012, 2016, 2020, 2024]

# iterable
# year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
# index=0      leap_years = []
# 0<15->True

# reverse program
# n=123
# rev=0
# temp=n
# while(temp>0):
#     rem=temp%10
#     rev=rev*10+rem
#     temp=temp // 10
# print("Reverse of ", n , "is : ", rev)    
# Output:
# Reverse of  123 is :  321

# iterable 1
# n=123  rev=0   temp=n
# 123>0->True
# rem=temp%10->123%10->3(last digit)
# rev=rev*10+rem->0*10+3->3
# temp=temp // 10->123//10->12(quotient)

# iterable 2
# n=12  rev=3   temp=12
# 12>0->True
# rem=temp%10->12%10->2(last digit)
# rev=rev*10+rem->3*10+2->32
# temp=temp // 10->12//10->1(quotient)

# iterable 3
# n=1  rev=32   temp=1
# 1>0->True
# rem=temp%10->1%10->1(last digit)
# rev=rev*10+rem->32*10+1->321
# temp=temp // 10->1//10->0(quotient)

# iterable 4
# n=0  rev=321   temp=0
# 0>0->False

# print(321)

# palindrome program
# Number to check
# n = 121

# # Initialize variables
# rev = 0
# temp = n

# Reverse the digits of the number
# while temp > 0:
#     rem = temp % 10
#     rev = rev * 10 + rem
#     temp = temp // 10

# Check if the original number is equal to its reversed version
# if n == rev:
#     print(f"{n} is a palindrome.")
# else:
#     print(f"{n} is not a palindrome.")
# Output:
# 121 is a palindrome.

# iterable 1
# n=121  rev=0  temp=121
# 121>0->True
# rem = temp % 10->121%10->1(last digit)
# rev = rev * 10 + rem->0*10+1->1
# temp = temp // 10->121//10->12(quotient)

# iterable 2
# n=12  rev=1  temp=12
# 12>0->True
# rem = temp % 10->12%10->2(last digit)
# rev = rev * 10 + rem->1*10+2->12
# temp = temp // 10->12//10->1(quotient)

# iterable 3
# n=1  rev=12  temp=1
# 1>0->True
# rem = temp % 10->1%10->1(last digit)
# rev = rev * 10 + rem->12*10+1->121
# temp = temp // 10->1//10->0(quotient)

# iterable 4
# n=0  rev=121  temp=0
# 0>0->False

# print(121)

# sum program

# n=123
# sum=0
# temp=n
# while(temp>0):
#     rem=temp%10
#     sum=sum+rem
#     temp=temp // 10
# print(f"sum of {n} is {sum}")    
# Output:
# sum of 123 is 6

# iterable 1
# n=123  sum=0  temp=123
# 123>0->True
# rem=temp%10->123%10->3(last digit)
# sum=sum+rem->sum=0+3->3
# temp=temp // 10->123//10->12(quotient)

# iterable 2
# n=12  sum=3  temp=12
# 12>0->True
# rem=temp%10->12%10->2(last digit)
# sum=sum+rem->sum=3+2->5
# temp=temp // 10->12//10->1(quotient)

# iterable 3
# n=1  sum=5  temp=1
# 1>0->True
# rem=temp%10->1%10->1(last digit)
# sum=sum+rem->sum=5+1->6
# temp=temp // 10->1//10->0(quotient)

# iterable 4
# n=0  sum=6  temp=0
# 0>0->False

# print(6)

# hw
# Reverse the digits of each number in the list using while loop
# a = [23, 45, 67, 8]

# reversed_list = []
# index = 0

# while index < len(a):
#     num = a[index]
#     reversed_num = 0

#     while num > 0:
#         rem = num % 10
#         reversed_num = reversed_num * 10 + rem
#         num = num // 10

#     reversed_list.append(reversed_num)
#     index += 1

# print(reversed_list)
# Output:[32, 54, 76, 8]

# iterable 1
# a=[23,45,67,8]
# reversed_list=[]   index=0
# 0<4->True
# num=a[index]=[23, 45, 67, 8][0]->23
# reversed_num=0 
# 23>0->True
# rem=23%10->3(last digit)
# reversed_num=0*10+3->3
# num=23 // 10->2(quotient)
# 2>0->True
# rem=2%10->2(last digit)
# reversed_num=3*10+2->32
# num=2 // 10->0
# 0>0->False
# [ ].append(32)->[32]
# index +=1    index=1

# iterable 2
# 1<4->True
# num=a=[23, 45, 67, 8][1]->45
# reversed_num=32
# 45>0->True
# rem=45%10->5
# reversed_num=0*10+5->5
# num=45 // 10->4
# 4>0->True
# rem=4%10->4
# reversed_num = 5 * 10 + 4->54
# num=4 // 10->0
# 0>0->False
# [32].append(54)->[32,54]
# index +=1    index=2

# iterable 3
# 2<4->True
# num=a=[23, 45, 67, 8][1]->67
# reversed_num=0 
# 67>0->True
# rem=67%10->7
# reversed_num=0*10+7->7
# num=67 // 10->6
# 6>0->True
# rem=6%10->6
# reversed_num = 7 * 10 + 6->76
# num=6 // 10->0
# 0>0->False
# [32,54].append(76)->[32,54,76]
# index +=1    index=3

# iterable 4
# 3<4->True
# num=a=[23, 45, 67, 8][3]->8
# rev

# print only palindrome number in another list
# numbers = [102, 101, 201, 232]

# palindrome_list = []
# index = 0

# while index < len(numbers):
#     current_num = numbers[index]

#     original_num = current_num
#     reversed_num = 0

#     while current_num > 0:
#         rem = current_num % 10
#         reversed_num = reversed_num * 10 + rem
#         current_num = current_num // 10

#     if original_num == reversed_num:
#         palindrome_list.append(original_num)

#     index += 1

# print("Palindrome numbers in the list:", palindrome_list)
# Output:Palindrome numbers in the list: [101, 232]

# iterable 1
# numbers = [102, 101, 201, 232]
# palindrome_list = []     index = 0
# 0<4->True
# current_num = [102,101,201,232][0]->102
# original_num = 102
# reversed_num = 0
# 102>0->True
# rem = 102 % 10->2
# reversed_num = 0 * 10 + 2->2
# current_num = 102 // 10->10
# 10>0->True
# rem = 10 % 10->0
# reversed_num = 2 * 10 + 0->20
# current_num = 10 // 10->1
# 1>0->True
# rem = 1 % 10->1
# reversed_num = 20 * 10 + 1->201
# current_num = 1 // 10->0
# 0>0->False
# if 102 == 201:->False
# index +=1     index=1

# range
# (start,end,step=1)(start->inclusive,end->exclusive)
# for loop
# for variable in(membership operator) (iterable_objects)->string,tuple,list,dictionary,set except numeric:
#      body
# for loop:when we know the number of iteration then we use for loop
# for loop:it is a finite loop
# for loop works on iterable object
# while loop:when we don't know the number of iteration then we use while loop
# while loop:it is an infinite loop
# while loop works on specific condition 

# for i in range(1,11):
#     print(i)
# Output:1
#        3
#        2
#        4
#        5
#        6
#        7
#        8
#        9
#        10

# l=[23,45,34,22,1]
# for i in l:
#     print(i)
#     print("hello")
# Output:23
#        hello
#        45
#        hello
#        34
#        hello
#        22
#        hello
#        1
#        hello

# s="hello world"
# for i in s:
#     print(i)
# Output:h
#        e
#        l
#        l
#        o
 
#        w
#        o
#        r
#        l
#        d

# for i in 28:
#     print(i)    
# Output:
#     for i in 28:
# TypeError: 'int' object is not iterable

# for i in "28":
#     print(i)    
# Output:
# 2
# 8
    
# for i in (28,1):
#     print(i)  
# Output:
# 28
# 1  

# for i in (28,"hello world") [-1]:
#     print(i)
# Output:
# h
# e
# l
# l
# o
 
# w
# o
# r
# l
# d

# for i in (28,"hello world") [0]:
#     print(i)
# Output:
#     for i in (28,"hello world") [0]:
# TypeError: 'int' object is not iterable

# for i in (28,"hello world") [-1].split(" "):
#     print(i)
# Output:
# hello
# world

# for i in (28,"hello world") [-1].split(" ")[0]:
#     print(i)
# Output:
# h
# e
# l
# l
# o
    
# Using a for loop to print even numbers from 1 to 10
# for number in range(1, 11):
#     if number % 2 == 0:
#         print(number)
# Output:
# 2
# 4 
# 6 
# 8 
# 10

# take year 1900 to 2050 and print leap year in list
# Initialize variables
# leap_years = []

# Check for leap years from 1900 to 2050
# for year in range(1900, 2051):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         leap_years.append(year)

# Print the leap years
# print("Leap years between 1900 and 2050:", leap_years)
# Output:
# Leap years between 1900 and 2050: [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976,
# 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048]


# prime number using while loop

# n=8
# i=2
# end=n-1
# c=0
# while i<end:
#     if(n%i==0):
#         c+=1
#     i+=1

# if(c>0):
#     print(f'{n} is not prime number')    
# else:
#     print(f'{n} is a prime number')    
# Output:
# 8 is not prime number    

# iterable 1
# n=8  i=2  end=8-1=7   c=0
# 2<7->True
# if(8%2==0)->remainder0->True   
# c+=1   c=0+1=1
# i+=1   i=2+1=3

# iterable 2
# 3<7->True
# if(8%3==0)->remainder2->False
# i+=1   i=3+1=4 

# iterable 3
# 4<7->True
# if(8%4==0)->remainder0->True
# c+=1   c=1+1=2
# i+=1   i=4+1=5

# iterable 4
# 5<7->True
# if(8%5==0)->remainder3->False
# i+=1   i=5+1=6

# iterable 5
# 6<7->True
# if(8%6==0)->remainder2->False
# i+=1   i=6+1=7

# iterable 6
# 7<7->False

# iterable 7
# if(2>0)->True
# print(8 is not prime number)    

# using ternary operator prime number program
# result=f'{n} is not prime number'  if(c>0) else f'{n} is a prime number'
# print(result)
# print(c)
# Output:
# 8 is not prime number
# 2
    
# prime number using for loop
# n=7
# c=0
# for i in range(2,n):
#     if(n%i==0):
#         c+=1

# result=f'{n} is not prime number'  if(c>0) else f'{n} is a prime number'
# print(result)
# print(c)
# Output:
# 7 is a prime number
# 0

# iterable 1(# prime number using for loop)
# n=7  c=0
# for i in range(2,7)
# for i in 2
# if(7%2==0)->remainder1->False

# iterable 2
# for i in 3
# if(7%3==0)->remainder1->False

# iterable 3
# for i in 4
# if(7%4==0)->remainder3->False

# iterable 4
# for i in 5
# if(7%5==0)->remainder2->False

# iterable 5
# for i in 6
# if(7%6==0)->remainder1->False

# iterable 6
# result=f'{n} is not prime number'  if(c>0) else f'{n} is a prime number'
# result=f'{n} is not prime number'  if(0>0)->False else 7 is a prime number'
# result=7 is a prime number
# print(7 is a prime number)
# print(0)

# print 1 to 100 prime numbers using for loop and also count total prime numbers
# Initialize variables
# total_primes = 0

# # Loop to print and count prime numbers from 1 to 100
# for number in range(2, 101):
#     c = 0
    # Loop to check for factors of number
    # for i in range(2, number):
    #     if number % i == 0:
    #         c += 1

    # Determine if the current number is prime based on the value of c
    # result = f'{number} is not a prime number' if c > 0 else f'{number} is a prime number'
    
    # Print the result
    # print(result)

    # Increment the total_primes count if the current number is prime
    # if c == 0:
        # total_primes += 1

# Print the total count of prime numbers
# print(f"Total prime numbers from 1 to 100: {total_primes}")
# Output:
# 2 is a prime number
# 3 is a prime number     
# 4 is not a prime number 
# 5 is a prime number     
# 6 is not a prime number 
# 7 is a prime number     
# 8 is not a prime number 
# 9 is not a prime number 
# 10 is not a prime number
# 11 is a prime number    
# 12 is not a prime number
# 13 is a prime number
# 14 is not a prime number
# 15 is not a prime number
# 16 is not a prime number
# 17 is a prime number
# 18 is not a prime number
# 19 is a prime number
# 20 is not a prime number
# 21 is not a prime number
# 22 is not a prime number
# 23 is a prime number
# 24 is not a prime number
# 25 is not a prime number
# 26 is not a prime number
# 27 is not a prime number
# 28 is not a prime number
# 29 is a prime number
# 30 is not a prime number
# 31 is a prime number
# 32 is not a prime number
# 33 is not a prime number
# 34 is not a prime number
# 35 is not a prime number
# 36 is not a prime number
# 37 is a prime number
# 38 is not a prime number
# 39 is not a prime number
# 40 is not a prime number
# 41 is a prime number
# 42 is not a prime number
# 43 is a prime number
# 44 is not a prime number
# 45 is not a prime number
# 46 is not a prime number
# 47 is a prime number
# 48 is not a prime number
# 49 is not a prime number
# 50 is not a prime number
# 51 is not a prime number
# 52 is not a prime number
# 53 is a prime number
# 54 is not a prime number
# 55 is not a prime number
# 56 is not a prime number
# 57 is not a prime number
# 58 is not a prime number
# 59 is a prime number
# 60 is not a prime number
# 61 is a prime number
# 62 is not a prime number
# 63 is not a prime number
# 64 is not a prime number
# 65 is not a prime number
# 66 is not a prime number
# 67 is a prime number
# 68 is not a prime number
# 69 is not a prime number
# 70 is not a prime number
# 71 is a prime number
# 72 is not a prime number
# 73 is a prime number
# 74 is not a prime number
# 75 is not a prime number
# 76 is not a prime number
# 77 is not a prime number
# 78 is not a prime number
# 79 is a prime number
# 80 is not a prime number
# 81 is not a prime number
# 82 is not a prime number
# 83 is a prime number
# 84 is not a prime number
# 85 is not a prime number
# 86 is not a prime number
# 87 is not a prime number
# 88 is not a prime number
# 89 is a prime number
# 90 is not a prime number
# 91 is not a prime number
# 92 is not a prime number
# 93 is not a prime number
# 94 is not a prime number
# 95 is not a prime number
# 96 is not a prime number
# 97 is a prime number
# 98 is not a prime number
# 99 is not a prime number
# 100 is not a prime number
# Total prime numbers from 1 to 100: 25

# iterable 1
# total_primes = 0
# for number in range(2, 101):
# for number in 2
# c=0
# for i in range(2,2):
# result = f'{number} is not a prime number' if c > 0 else f'{number} is a prime number'
# result = f'{number} is not a prime number' if 0 > 0->False else 2 is a prime number
# result=2 is a prime number
# print(2 is a prime number)
# if c == 0:->0==0->True
# total_primes += 1   total_primes=0+1=1

# iterable 2
# total_primes = 1
# for number in range(2, 101):
# for number in 3
# c=0
# for i in range(2,3):
# for i in 2
# if number % i == 0:
# c += 1
# if 3 % 2 == 0:->remainder1->False
# result = f'{number} is not a prime number' if c > 0 else f'{number} is a prime number'
# result = f'{number} is not a prime number' if 0 > 0->False else 3 is a prime number
# result=3 is a prime number
# print(3 is a prime number)
# if c == 0:->0==0->True
# total_primes += 1  total_primes=1+1=2

# iterable 3
# total_primes = 2
# for number in range(2, 101):
# for number in 4
# c=0
# for i in range(2,4):
# for i in 2
# if 4 % 2 == 0:->remainder0->True
# c += 1


