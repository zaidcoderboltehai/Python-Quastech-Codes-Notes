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
# Output:
# 12
# 24
# 25
# 18
# 19
# 40
# 55
    
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
# Output:
# 12
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

# Use a while loop to count and store leap years in the list
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

# # Reverse the digits of the number
# while temp > 0:
#     rem = temp % 10
#     rev = rev * 10 + rem
#     temp = temp // 10

# # Check if the original number is equal to its reversed version
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

# if 121==121
# print(121 is a palindrome number)

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

# print(sum of 123 is 6)

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


# fibonacci series
#  1
#  2
#  3               0   1    1   2   3   5
#  4               a   b    c
#  5                   a    b   c
#  6                        a   b   c
#                               a   b   c

# a=0
# b=1
# for i in range(1,11):
#     print(a)
#     c=a+b
#     a=b
#     b=c
# Output:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34    
    
# iterbale 1
# a=0:->a=0
# b=1:->b=1
# for i in range(1,11):->for i in 1
#     print(a):->print(0)
#     c=a+b:->0+1->c=1
#     a=b:->a=1
#     b=c:->b=1

# iterable 2
# for i in range(1,11):->for i in 2
#     print(a):->print(1)
#     c=a+b:->1+1->c=2
#     a=b:->a=1
#     b=c:->b=2

# iterable 3
# for i in range(1,11):->for i in 3
#     print(a):->print(1)
#     c=a+b:->1+2->c=3
#     a=b:->a=2
#     b=c:->b=3

 
# Nested for loop

# for i in range(1,6):
#     for j in range(11,16):
#         print(i,j) 

# for i in range(1,6):
#     for j in range(11,16):
#         print(i,j)

#     for k in range(21,26):
#         print(i,k)
#         for x in range(31,36):
#             print(i,k,x)        

# iterable 1

# for i in range(1,6):->for i in 1
#     for j in range(11,16):->for j in 11
#         print(i,j):->print(1,11)

# iterable 2
#     for j in range(11,16):->for j in 12
#         print(i,j):->print(1,12)

# iterable 3
#     for j in range(11,16):->for j in 13
#         print(i,j):->print(1,13)

# iterable 4
#     for j in range(11,16):->for j in 14
#         print(i,j):->print(1,14)

# iterable 5
#     for j in range(11,16):->for j in 15
#         print(i,j):->print(1,15)

# iterable 6
# for i in range(1,6):->for i in 2
#     for j in range(11,16):->for j in 11
#         print(i,j):->print(2,11)

# iterable 7
#     for j in range(11,16):->for j in 12
#         print(i,j):->print(2,12)

# iterable 8
#      for j in range(11,16):->for j in 13
#         print(i,j):->print(2,13)

# iterable 9
#      for j in range(11,16):->for j in 14
#         print(i,j):->print(2,14)

# iterable 10
#      for j in range(11,16):->for j in 15
#         print(i,j):->print(2,15)


# for i in range(1,6):
#     for j in range(11,16):
#         print(i,j)

#     for k in range(21,26):
#         print(i,k)
#         for x in range(31,36):
#             print(i,k,x)        

# Output:
# 1 11
# 1 12
# 1 13
# 1 14
# 1 15
# 2 11
# 2 12
# 2 13
# 2 14
# 2 15
# 3 11
# 3 12
# 3 13
# 3 14
# 3 15
# 4 11
# 4 12
# 4 13
# 4 14
# 4 15
# 5 11
# 5 12
# 5 13
# 5 14
# 5 15
# 1 11
# 1 12
# 1 13
# 1 14
# 1 15
# 1 21
# 1 21 31
# 1 21 32
# 1 21 33
# 1 21 34
# 1 21 35
# 1 22
# 1 22 31
# 1 22 32
# 1 22 33
# 1 22 34
# 1 22 35
# 1 23
# 1 23 31
# 1 23 32
# 1 23 33
# 1 23 34
# 1 23 35
# 1 24
# 1 24 31
# 1 24 32
# 1 24 33
# 1 24 34
# 1 24 35
# 1 25
# 1 25 31
# 1 25 32
# 1 25 33
# 1 25 34
# 1 25 35
# 2 11
# 2 12
# 2 13
# 2 14
# 2 15
# 2 21
# 2 21 31
# 2 21 32
# 2 21 33
# 2 21 34
# 2 21 35
# 2 22
# 2 22 31
# 2 22 32
# 2 22 33
# 2 22 34
# 2 22 35
# 2 23
# 2 23 31
# 2 23 32
# 2 23 33
# 2 23 34
# 2 23 35
# 2 24
# 2 24 31
# 2 24 32
# 2 24 33
# 2 24 34
# 2 24 35
# 2 25
# 2 25 31
# 2 25 32
# 2 25 33
# 2 25 34
# 2 25 35
# 3 11
# 3 12
# 3 13
# 3 14
# 3 15
# 3 21
# 3 21 31
# 3 21 32
# 3 21 33
# 3 21 34
# 3 21 35
# 3 22
# 3 22 31
# 3 22 32
# 3 22 33
# 3 22 34
# 3 22 35
# 3 23
# 3 23 31
# 3 23 32
# 3 23 33
# 3 23 34
# 3 23 35
# 3 24
# 3 24 31
# 3 24 32
# 3 24 33
# 3 24 34
# 3 24 35
# 3 25
# 3 25 31
# 3 25 32
# 3 25 33
# 3 25 34
# 3 25 35
# 4 11
# 4 12
# 4 13
# 4 14
# 4 15
# 4 21
# 4 21 31
# 4 21 32
# 4 21 33
# 4 21 34
# 4 21 35
# 4 22
# 4 22 31
# 4 22 32
# 4 22 33
# 4 22 34
# 4 22 35
# 4 23
# 4 23 31
# 4 23 32
# 4 23 33
# 4 23 34
# 4 23 35
# 4 24
# 4 24 31
# 4 24 32
# 4 24 33
# 4 24 34
# 4 24 35
# 4 25
# 4 25 31
# 4 25 32
# 4 25 33
# 4 25 34
# 4 25 35
# 5 11
# 5 12
# 5 13
# 5 14
# 5 15
# 5 21
# 5 21 31
# 5 21 32
# 5 21 33
# 5 21 34
# 5 21 35
# 5 22
# 5 22 31
# 5 22 32
# 5 22 33
# 5 22 34
# 5 22 35
# 5 23
# 5 23 31
# 5 23 32
# 5 23 33
# 5 23 34
# 5 23 35
# 5 24
# 5 24 31
# 5 24 32
# 5 24 33
# 5 24 34
# 5 24 35
# 5 25
# 5 25 31
# 5 25 32
# 5 25 33
# 5 25 34
# 5 25 35            
            
# Calculate the sum using a while loop
# my_list = [1, 2, 14, 9, 6]

# Initialize variables
# list_sum = 0
# index = 0

# while index < len(my_list):
#     list_sum += my_list[index]
#     index += 1

# print(f"The sum of the list is: {list_sum}")

# Output:
# The sum of the list is: 32

# iterable 1
# my_list = [1, 2, 14, 9, 6]
# list_sum = 0
# index = 0
# while index < len(my_list):->while 0<5->True
#     list_sum += my_list[index]:->list_sum =[1,2,14,9,6][0]->1
#     index += 1    index=0+1=1

# iterable 2
# while index < len(my_list):->while 1<5->True
#     list_sum += my_list[index]:->list_sum =[1,2,14,9,6][1]->2
#     index += 1    index=1+1=2

# Calculate the sum using a for loop

# my_list = [1, 2, 14, 9, 6]

#  Initialize variable
# list_sum = 0

# for element in my_list:
#     list_sum += element

#  Print the result
# print(f"The sum of the list is: {list_sum}")
# Output:
# The sum of the list is: 32

# iterable 1
# my_list = [1, 2, 14, 9, 6]

# list_sum = 0

# for element in my_list:->for element in 1
#     list_sum += element:->list_sum +=0+1=1

# iterable 2
# for element in my_list:->for element in 2
#     list_sum += element:->list_sum +=1+2=3

# iterable 3
# for element in my_list:->for element in 14
#     list_sum += element:->list_sum +=3+14=17

# iterable 4
# for element in my_list:->for element in 9
#     list_sum += element:->list_sum +=17+9=26

# iterable 5
# for element in my_list:->for element in 6
#     list_sum += element:->list_sum +=26+6=32

# Calculate the sum using a for loop

# sn=[3,4,56,7,8]
# s=0
# for i in sn:
#     s=s+1
# print(s)

# sum [1,20]->21 program 
# sn=[[1,20],[23,7],[87,3]]
# snl=[]
# for i in sn:
#     print(i)
#     s=0
#     for j in i:
#         s=s+j
#     print(s)
#     snl.append(s)

# print(snl)    
# Output:
# [1, 20]
# 21
# [23, 7]
# 30
# [87, 3]
# 90
# [21, 30, 90]

# iterable 1
# sn=[[1,20],[23,7],[87,3]]
# snl=[]
# for i in sn:->for i in [1,20]
#     print(i):->print([1,20])
#     s=0
#    for j in i:->for j in [1,20]->for j in 1
#        s=s+j:->0+1->s=1

# iterable 2
#    for j in i:->for j in 20
#        s=s+j:->0+1->s=1

# print greater number from list
# my_list = [1, 2, 14, 9, 6]

# Initialize variables
# index = 0
# max_number = my_list[0]  # Assume the first element is the maximum

# Iterate through the list using a while loop
# while index < len(my_list):
#     if my_list[index] > max_number:
#         max_number = my_list[index]
#     index += 1

# Print the result
# print(f"The greatest number in the list is: {max_number}")

# print maximum number from list
# data=[1, 2, 14, 9, 6]
# max=data[0]
# for i in data:
#     if i>max:
#         max=i
# print(max)    

# Output:14

# print minimum number from list
# data = [1, 2, 14, 9, 6]

# Assume the first element is the minimum
# min_number = data[0]

# Iterate through the list using a for loop
# for i in data:
#     if i < min_number:
#         min_number = i

# Print the result
# print(f"The minimum number in the list is: {min_number}")

# Output:The minimum number in the list is: 1

# print all number which is not divisible by 3 and 7 but if any number occur which is divisible by 3 and 7 then loop should be stopped(break used)
# data = [1, 2, 9,21, 6]
# for i in data:
#     if(i%3==0 and i%7==0):
#         break
#     print(i)
# Output:
# 1
# 2
# 9    
    
# data = [1, 2, 9,21, 6]
# for i in data:
#         print(i)
#         if(i%3==0 and i%7==0):
#              break
# Output:
# 1
# 2 
# 9 
# 21 
       
# break loop ko terminate karne ka kaam karta hai
# continue is used to revaluate means ghumata hai 
# for i in range(1,11):
#     print(i)
#     break
# Output:1 

# continue used
# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i)
# Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

# for i in range(1,11):
#     print(i)
#     continue
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# for i in range(1,11):
#     continue
#     print(i)
# Output:"

# for i in range(1,6):
#     for j in range(1,6):
#         print(i)
# Output:
# 1
# 1
# 1
# 1
# 1
# 2
# 2
# 2
# 2
# 2
# 3
# 3
# 3
# 3
# 3
# 4
# 4
# 4
# 4
# 4
# 5
# 5
# 5
# 5
# 5

# iterable 1
# for i in range(1,6):->for i in 1
#     for j in range(1,6):->for j in 1 
#         print(i):->print(1)

# iterable 2
#     for j in range(1,6):->for j in 2 
#         print(i):->print(1)

# iterable 3
#     for j in range(1,6):->for j in 3 
#         print(i):->print(1)

# iterable 4
#     for j in range(1,6):->for j in 4
#         print(i):->print(1)

# iterable 5
#     for j in range(1,6):->for j in 5 
#         print(i):->print(1)

# iterable 6
# for i in range(1,6):->for i in 2
#     for j in range(1,6):->for j in 1 
#         print(i):->print(2)

# iterable 7
#     for j in range(1,6):->for j in 2 
#         print(i):->print(2)

# iterable 8
#     for j in range(1,6):->for j in 3 
#         print(i):->print(2)

# iterable 9
#     for j in range(1,6):->for j in 4 
#         print(i):->print(2)

# iterable 10
#     for j in range(1,6):->for j in 5
#         print(i):->print(2)


# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end="")  #by default \n rehta hai print mai esliye end="" laikai hata diye hai taki next line mai naa aa jaye
#     print()
# Output:
# 1111
# 2222
# 3333
# 4444

# iterable 1
# for i in range(1,5):-> for i in 1
#     for j in range(1,5):->for j in 1
#         print(i,end=""):->print(1,end="")->print(1)
#     print()

# iterable 2
#     for j in range(1,5):->for j in 2
#         print(i,end=""):->print(1,end="")->print(1)
#     print()

# iterable 3
#     for j in range(1,5):->for j in 3
#         print(i,end=""):->print(1,end="")->print(1)
#     print()

# iterable 4
#     for j in range(1,5):->for j in 4
#         print(i,end=""):->print(1,end="")->print(1)->1111
#     print()->execute hoga aur next line change hoga

# iterable 5
# for i in range(1,5):-> for i in 2
#     for j in range(1,5):->for j in 1
#         print(i,end=""):->print(2,end="")->print(2)
#     print()

# iterable 6
#     for j in range(1,5):->for j in 2
#         print(i,end=""):->print(2,end="")->print(2)
#     print()

# iterable 7
#     for j in range(1,5):->for j in 3
#         print(i,end=""):->print(2,end="")->print(2)
#     print()

# iterable 8
#     for j in range(1,5):->for j in 4
#         print(i,end=""):->print(2,end="")->print(2)->2222
#     print()->execute hoga aur next line pai jayega

# for i in range(1, 5):
#     for j in range(1, 5):
#         print(j, end="")
#     print()
# Output:
# 1234
# 1234
# 1234
# 1234

# iterable 1 
# for i in range(1, 5):->for i in 1
#     for j in range(1, 5):->for j in 1
#         print(j, end=""):->print(1,end="")->print(1)
#     print()

# iterable 2
#     for j in range(1, 5):->for j in 2
#         print(j, end=""):->print(2,end="")->print(2)
#     print()

# iterable 3
#     for j in range(1, 5):->for j in 3
#         print(j, end=""):->print(3,end="")->print(3)
#     print()

# iterable 4
#     for j in range(1, 5):->for j in 4
#         print(j, end=""):->print(4,end="")->print(4)->1234
#     print()->execute hoga aur next line pai jayega

# iterable 5
# for i in range(1, 5):->for i in 2
#     for j in range(1, 5):->for j in 1
#         print(j, end=""):->print(1,end="")->print(1)
#     print()

# iterable 6 
#     for j in range(1, 5):->for j in 2
#         print(j, end=""):->print(2,end="")->print(2)
#     print()

# iterable 7
#     for j in range(1, 5):->for j in 3
#         print(j, end=""):->print(3,end="")->print(3)
#     print()

# iterable 8
#     for j in range(1, 5):->for j in 4
#         print(j, end=""):->print(4,end="")->print(4)->1234
#     print()->execute hoga aur next line pai jayega

    
# for i in range(1, 5):
#     for j in range(1, 5):
#         print("*", end="")
#     print()
# Output:
# ****
# ****
# ****
# **** 

# iterable 1 
# for i in range(1, 5):->for i in 1
#     for j in range(1, 5):->for j in 1 
#         print("*", end=""):->print(*)
#     print()

# iterable 2
#     for j in range(1, 5):->for j in 2 
#         print("*", end=""):->print(*)
#     print()

# iterable 3
#     for j in range(1, 5):->for j in 3 
#         print("*", end=""):->print(*)
#     print()

# iterable 4
#     for j in range(1, 5):->for j in 4
#         print("*", end=""):->print(*)->****
#     print()->execute hoga aur next line pai jayega

# n=1
# for i in range(1, 5):
#     for j in range(1, 5):
#         print(n, end=" ")
#         n+=1
#     print()
# Output:
# 1 2 3 4 
# 5 6 7 8 
# 9 10 11 12 
# 13 14 15 16

# iterable 1
# n=1:->n=1 
# for i in range(1, 5):-> for i in 1 
#     for j in range(1, 5):-> for j in 1 
#         print(n, end=" "):->print(1,end=" ")->print(1)
#         n+=1:->n=1+1->n=2
#     print()

# iterable 2
#     for j in range(1, 5):-> for j in 2
#         print(n, end=" "):->print(2,end=" ")->print(2)
#         n+=1:->n=2+1->n=3
#     print()

# for i in range(1,4):
#     for j in range(1,5):
#         print("*", end=" ")
#     print()
# Output:
# * * * * 
# * * * * 
# * * * *

# print(ord("A"))  #->return ascii value of character
# Output:65

# print(chr(65))   #->return character of ascii
# Output:A

# for i in range(10001):
#     print(chr(i),end=" ")
# Output:
# ☺ ☻ ♥ ♦ ♣ ♠     
#  ♫ ☼ ► ◄ ↕ ‼ ¶ § ▬ ↨ ↑ ↓ → ∟↔▲▼ 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~ ⌂     
                                                                                                                                                                                                   

#                       ¡ ¢ £ ¤ ¥ ¦ § ¨ © ª « ¬ ­ ® ¯ ° ± ² ³ ´ µ ¶ · ¸ ¹ º » ¼ ½ ¾ ¿ À Á Â Ã Ä Å Æ Ç È É Ê Ë Ì Í Î Ï Ð Ñ Ò Ó Ô Õ Ö × Ø Ù Ú Û Ü Ý Þ ß à á â ã ä å æ ç è é ê ë
#  ì í î ï ð ñ ò ó ô õ ö ÷ ø ù ú û ü ý þ ÿ Ā ā Ă ă Ą ą Ć ć Ĉ ĉ Ċ ċ Č č Ď ď Đ đ Ē ē Ĕ ĕ Ė ė Ę ę Ě ě Ĝ ĝ Ğ ğ Ġ ġ Ģ ģ Ĥ ĥ Ħ ħ Ĩ ĩ Ī ī Ĭ ĭ Į į İ ı Ĳ ĳ Ĵ ĵ Ķ ķ ĸ Ĺ ĺ Ļ ļ Ľ ľ Ŀ ŀ Ł ł Ń ń Ņ ņ Ň ň ŉ Ŋ ŋ Ō ō Ŏ ŏ 
# Ő ő Œ œ Ŕ ŕ Ŗ ŗ Ř ř Ś ś Ŝ ŝ Ş ş Š š Ţ ţ Ť ť Ŧ ŧ Ũ ũ Ū ū Ŭ ŭ Ů ů Ű ű Ų ų Ŵ ŵ Ŷ ŷ Ÿ Ź ź Ż ż Ž ž ſ ƀ Ɓ Ƃ ƃ Ƅ ƅ Ɔ Ƈ ƈ Ɖ Ɗ Ƌ ƌ ƍ Ǝ Ə Ɛ Ƒ ƒ Ɠ Ɣ ƕ Ɩ Ɨ Ƙ ƙ ƚ ƛ Ɯ Ɲ ƞ Ɵ Ơ ơ Ƣ ƣ Ƥ ƥ Ʀ Ƨ ƨ Ʃ ƪ ƫ Ƭ ƭ Ʈ Ư ư Ʊ Ʋ Ƴ ƴ Ƶ ƶ Ʒ Ƹ ƹ ƺ ƻ Ƽ ƽ ƾ ƿ ǀ ǁ ǂ ǃ Ǆ ǅ ǆ Ǉ ǈ ǉ Ǌ ǋ ǌ Ǎ ǎ Ǐ ǐ Ǒ ǒ Ǔ ǔ Ǖ ǖ Ǘ ǘ Ǚ ǚ Ǜ ǜ ǝ Ǟ ǟ Ǡ ǡ Ǣ ǣ Ǥ ǥ Ǧ ǧ Ǩ ǩ Ǫ ǫ Ǭ ǭ Ǯ ǯ ǰ Ǳ ǲ ǳ Ǵ ǵ Ƕ Ƿ Ǹ ǹ Ǻ ǻ Ǽ ǽ Ǿ ǿ Ȁ ȁ Ȃ ȃ Ȅ ȅ Ȇ ȇ Ȉ ȉ Ȋ ȋ Ȍ ȍ Ȏ ȏ Ȑ ȑ Ȓ ȓ Ȕ ȕ Ȗ ȗ Ș 
# ș Ț ț Ȝ ȝ Ȟ ȟ Ƞ ȡ Ȣ ȣ Ȥ ȥ Ȧ ȧ Ȩ ȩ Ȫ ȫ Ȭ ȭ Ȯ ȯ Ȱ ȱ Ȳ ȳ ȴ ȵ ȶ ȷ ȸ ȹ Ⱥ Ȼ ȼ Ƚ Ⱦ ȿ ɀ Ɂ ɂ Ƀ Ʉ Ʌ Ɇ ɇ Ɉ ɉ Ɋ ɋ Ɍ ɍ Ɏ ɏ ɐ ɑ ɒ ɓ ɔ ɕ ɖ ɗ ɘ ə ɚ ɛ ɜ ɝ ɞ ɟ ɠ ɡ ɢ ɣ ɤ ɥ ɦ ɧ ɨ ɩ ɪ ɫ ɬ ɭ ɮ ɯ ɰ ɱ ɲ ɳ ɴ ɵ ɶ ɷ ɸ ɹ ɺ ɻ ɼ ɽ ɾ ɿ ʀ ʁ ʂ ʃ ʄ ʅ ʆ ʇ ʈ ʉ ʊ ʋ ʌ ʍ ʎ ʏ ʐ ʑ ʒ ʓ ʔ ʕ ʖ ʗ ʘ ʙ ʚ ʛ ʜ ʝ ʞ ʟ ʠ ʡ ʢ ʣ ʤ ʥ ʦ ʧ ʨ ʩ ʪ ʫ ʬ ʭ ʮ ʯ ʰ ʱ ʲ ʳ ʴ ʵ ʶ ʷ ʸ ʹ ʺ ʻ ʼ ʽ ʾ ʿ ˀ ˁ ˂ ˃ ˄ ˅ ˆ ˇ ˈ ˉ ˊ ˋ ˌ ˍ ˎ ˏ ː ˑ ˒ ˓ ˔ ˕ ˖ ˗ ˘ ˙ ˚ ˛ ˜ ˝ ˞ ˟ ˠ ˡ 
# ˢ ˣ ˤ ˥ ˦ ˧ ˨ ˩ ˪ ˫ ˬ ˭ ˮ ˯ ˰ ˱ ˲ ˳ ˴ ˵ ˶ ˷ ˸ ˹ ˺ ˻ ˼ ˽ ˾ ˿ ̀ ́ ̂ ̃ ̄ ̅ ̆ ̇ ̈ ̉ ̊ ̋ ̌ ̍ ̎ ̏ ̐ ̑ ̒ ̓ ̔ ̕ ̖ ̗ ̘ ̙ ̚ ̛ ̜ ̝ ̞ ̟ ̠ ̡ ̢ ̣ ̤ ̥ ̦ ̧ ̨ ̩ ̪ ̫ ̬ ̭ ̮ ̯ ̰ ̱ ̲ ̳ ̴ ̵ ̶ ̷ ̸ ̹ ̺ ̻ ̼ ̽ ̾ ̿ ̀ ́ ͂ ̓ ̈́ ͅ ͆
#  ͇ ͈ ͉ ͊ ͋ ͌ ͍ ͎ ͏ ͐ ͑ ͒ ͓ ͔ ͕ ͖ ͗ ͘ ͙ ͚ ͛ ͜ ͝ ͞ ͟ ͠ ͡ ͢ ͣ ͤ ͥ ͦ ͧ ͨ ͩ ͪ ͫ ͬ ͭ ͮ ͯ Ͱ ͱ Ͳ ͳ ʹ ͵ Ͷ ͷ ͸ ͹ ͺ ͻ ͼ ͽ ; Ϳ ΀ ΁ ΂ ΃ ΄ ΅ Ά · Έ Ή Ί ΋ Ό ΍ Ύ Ώ ΐ Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ ΢ Σ Τ Υ Φ Χ Ψ Ω Ϊ 
# Ϋ ά έ ή ί ΰ α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ ς σ τ υ φ χ ψ ω ϊ ϋ ό ύ ώ Ϗ ϐ ϑ ϒ ϓ ϔ ϕ ϖ ϗ Ϙ ϙ Ϛ ϛ Ϝ ϝ Ϟ ϟ Ϡ ϡ Ϣ ϣ Ϥ ϥ Ϧ ϧ Ϩ ϩ Ϫ ϫ Ϭ ϭ Ϯ ϯ ϰ ϱ ϲ ϳ ϴ ϵ ϶ Ϸ ϸ Ϲ Ϻ ϻ ϼ Ͻ Ͼ Ͽ Ѐ Ё Ђ Ѓ Є Ѕ І Ї Ј Љ Њ Ћ Ќ Ѝ Ў Џ А Б В Г Д Е Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я ѐ ё ђ ѓ є ѕ і ї ј љ њ ћ ќ ѝ ў џ Ѡ ѡ Ѣ ѣ Ѥ ѥ Ѧ ѧ Ѩ ѩ Ѫ ѫ Ѭ ѭ Ѯ ѯ Ѱ ѱ Ѳ ѳ 
# Ѵ ѵ Ѷ ѷ Ѹ ѹ Ѻ ѻ Ѽ ѽ Ѿ ѿ Ҁ ҁ ҂ ҃ ҄ ҅ ҆ ҇ ҈ ҉ Ҋ ҋ Ҍ ҍ Ҏ ҏ Ґ ґ Ғ ғ Ҕ ҕ Җ җ Ҙ ҙ Қ қ Ҝ ҝ Ҟ ҟ Ҡ ҡ Ң ң Ҥ ҥ Ҧ ҧ Ҩ ҩ Ҫ ҫ Ҭ ҭ Ү ү Ұ ұ Ҳ ҳ Ҵ ҵ Ҷ ҷ Ҹ ҹ Һ һ Ҽ ҽ Ҿ ҿ Ӏ Ӂ ӂ Ӄ ӄ Ӆ ӆ Ӈ ӈ Ӊ ӊ Ӌ ӌ Ӎ ӎ ӏ Ӑ ӑ Ӓ ӓ Ӕ ӕ Ӗ ӗ Ә
#  ә Ӛ ӛ Ӝ ӝ Ӟ ӟ Ӡ ӡ Ӣ ӣ Ӥ ӥ Ӧ ӧ Ө ө Ӫ ӫ Ӭ ӭ Ӯ ӯ Ӱ ӱ Ӳ ӳ Ӵ ӵ Ӷ ӷ Ӹ ӹ Ӻ ӻ Ӽ ӽ Ӿ ӿ Ԁ ԁ Ԃ ԃ Ԅ ԅ Ԇ ԇ Ԉ ԉ Ԋ ԋ Ԍ ԍ Ԏ ԏ Ԑ ԑ Ԓ ԓ Ԕ ԕ Ԗ ԗ Ԙ ԙ Ԛ ԛ Ԝ ԝ Ԟ ԟ Ԡ ԡ Ԣ ԣ Ԥ ԥ Ԧ ԧ Ԩ ԩ Ԫ ԫ Ԭ ԭ Ԯ ԯ ԰ Ա Բ Գ Դ Ե Զ Է Ը Թ Ժ Ի Լ 
# Խ Ծ Կ Հ Ձ Ղ Ճ Մ Յ Ն Շ Ո Չ Պ Ջ Ռ Ս Վ Տ Ր Ց Ւ Փ Ք Օ Ֆ ՗ ՘ ՙ ՚ ՛ ՜ ՝ ՞ ՟ ՠ ա բ գ դ ե զ է ը թ ժ ի լ խ ծ կ հ ձ ղ ճ մ յ ն շ ո չ պ ջ ռ ս վ տ ր ց ւ փ ք օ ֆ և ֈ ։ ֊ ֋ ֌ ֍ ֎ ֏ ֐ ֑ ֒ ֓ ֔ ֕ ֖ ֗ ֘ ֙ ֚ ֛ ֜ ֝ ֞ ֟ ֠ ֡
#  ֢ ֣ ֤ ֥ ֦ ֧ ֨ ֩ ֪ ֫ ֬ ֭ ֮ ֯ ְ ֱ ֲ ֳ ִ ֵ ֶ ַ ָ ֹ ֺ ֻ ּ ֽ ־ ֿ ׀ ׁ ׂ ׃ ׄ ׅ ׆ ׇ ׈ ׉ ׊ ׋ ׌ ׍ ׎ ׏ א ב ג ד ה ו ז ח ט י ך כ ל ם מ ן נ ס ע ף פ ץ צ ק ר ש ת ׫ ׬ ׭ ׮ ׯ װ ױ ײ ׳ ״ ׵ ׶ ׷ ׸ ׹ ׺ ׻ ׼ ׽ ׾ ׿ ؀ ؁ ؂ ؃ ؄ ؅ 
# ؆ ؇ ؈ ؉ ؊ ؋ ، ؍ ؎ ؏ ؐ ؑ ؒ ؓ ؔ ؕ ؖ ؗ ؘ ؙ ؚ ؛ ؜ ؝ ؞ ؟ ؠ ء آ أ ؤ إ ئ ا ب ة ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ػ ؼ ؽ ؾ ؿ ـ ف ق ك ل م ن ه و ى ي ً ٌ ٍ َ ُ ِ ّ ْ ٓ ٔ ٕ ٖ ٗ ٘ ٙ ٚ ٛ ٜ ٝ ٞ ٟ ٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ ٪
#  ٫ ٬ ٭ ٮ ٯ ٰ ٱ ٲ ٳ ٴ ٵ ٶ ٷ ٸ ٹ ٺ ٻ ټ ٽ پ ٿ ڀ ځ ڂ ڃ ڄ څ چ ڇ ڈ ډ ڊ ڋ ڌ ڍ ڎ ڏ ڐ ڑ ڒ ړ ڔ ڕ ږ ڗ ژ ڙ ښ ڛ ڜ ڝ ڞ ڟ ڠ ڡ ڢ ڣ ڤ ڥ ڦ ڧ ڨ ک ڪ ګ ڬ ڭ ڮ گ ڰ ڱ ڲ ڳ ڴ ڵ ڶ ڷ ڸ ڹ ں ڻ ڼ ڽ ھ ڿ ۀ ہ ۂ ۃ ۄ ۅ ۆ ۇ ۈ ۉ ۊ ۋ ی ۍ ێ 
# ۏ ې ۑ ے ۓ ۔ ە ۖ ۗ ۘ ۙ ۚ ۛ ۜ ۝ ۞ ۟ ۠ ۡ ۢ ۣ ۤ ۥ ۦ ۧ ۨ ۩ ۪ ۫ ۬ ۭ ۮ ۯ ۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹ ۺ ۻ ۼ ۽ ۾ ۿ ܀ ܁ ܂ ܃ ܄ ܅ ܆ ܇ ܈ ܉ ܊ ܋ ܌ ܍ ܎ ܏ ܐ ܑ ܒ ܓ ܔ ܕ ܖ ܗ ܘ ܙ ܚ ܛ ܜ ܝ ܞ ܟ ܠ ܡ ܢ ܣ ܤ ܥ ܦ ܧ ܨ ܩ ܪ ܫ ܬ ܭ ܮ ܯ ܰ ܱ ܲ ܳ
#  ܴ ܵ ܶ ܷ ܸ ܹ ܺ ܻ ܼ ܽ ܾ ܿ ݀ ݁ ݂ ݃ ݄ ݅ ݆ ݇ ݈ ݉ ݊ ݋ ݌ ݍ ݎ ݏ ݐ ݑ ݒ ݓ ݔ ݕ ݖ ݗ ݘ ݙ ݚ ݛ ݜ ݝ ݞ ݟ ݠ ݡ ݢ ݣ ݤ ݥ ݦ ݧ ݨ ݩ ݪ ݫ ݬ ݭ ݮ ݯ ݰ ݱ ݲ ݳ ݴ ݵ ݶ ݷ ݸ ݹ ݺ ݻ ݼ ݽ ݾ ݿ ހ ށ ނ ރ ބ ޅ ކ އ ވ މ ފ ދ ތ ލ ގ ޏ ސ ޑ ޒ ޓ ޔ ޕ ޖ ޗ 
# ޘ ޙ ޚ ޛ ޜ ޝ ޞ ޟ ޠ ޡ ޢ ޣ ޤ ޥ ަ ާ ި ީ ު ޫ ެ ޭ ޮ ޯ ް ޱ ޲ ޳ ޴ ޵ ޶ ޷ ޸ ޹ ޺ ޻ ޼ ޽ ޾ ޿ ߀ ߁ ߂ ߃ ߄ ߅ ߆ ߇ ߈ ߉ ߊ ߋ ߌ ߍ ߎ ߏ ߐ ߑ ߒ ߓ ߔ ߕ ߖ ߗ ߘ ߙ ߚ ߛ ߜ ߝ ߞ ߟ ߠ ߡ ߢ ߣ ߤ ߥ ߦ ߧ ߨ ߩ ߪ ߫ ߬ ߭ ߮ ߯ ߰ ߱ ߲ ߳ ߴ ߵ ߶ ߷ ߸ ߹ ߺ ߻ ߼
#  ߽ ߾ ߿ ࠀ ࠁ ࠂ ࠃ ࠄ ࠅ ࠆ ࠇ ࠈ ࠉ ࠊ ࠋ ࠌ ࠍ ࠎ ࠏ ࠐ ࠑ ࠒ ࠓ ࠔ ࠕ ࠖ ࠗ ࠘ ࠙ ࠚ ࠛ ࠜ ࠝ ࠞ ࠟ ࠠ ࠡ ࠢ ࠣ ࠤ ࠥ ࠦ ࠧ ࠨ ࠩ ࠪ ࠫ ࠬ ࠭ ࠮ ࠯ ࠰ ࠱ ࠲ ࠳ ࠴ ࠵ ࠶ ࠷ ࠸ ࠹ ࠺ ࠻ ࠼ ࠽ ࠾ ࠿ ࡀ ࡁ ࡂ ࡃ ࡄ ࡅ ࡆ ࡇ ࡈ ࡉ ࡊ ࡋ ࡌ ࡍ ࡎ ࡏ ࡐ ࡑ ࡒ ࡓ ࡔ ࡕ ࡖ ࡗ ࡘ ࡙ ࡚ ࡛ ࡜ ࡝ ࡞ ࡟ ࡠ 
# ࡡ ࡢ ࡣ ࡤ ࡥ ࡦ ࡧ ࡨ ࡩ ࡪ ࡫ ࡬ ࡭ ࡮ ࡯ ࡰ ࡱ ࡲ ࡳ ࡴ ࡵ ࡶ ࡷ ࡸ ࡹ ࡺ ࡻ ࡼ ࡽ ࡾ ࡿ ࢀ ࢁ ࢂ ࢃ ࢄ ࢅ ࢆ ࢇ ࢈ ࢉ ࢊ ࢋ ࢌ ࢍ ࢎ ࢏ ࢐ ࢑ ࢒ ࢓ ࢔ ࢕ ࢖ ࢗ ࢘ ࢙ ࢚ ࢛ ࢜ ࢝ ࢞ ࢟ ࢠ ࢡ ࢢ ࢣ ࢤ ࢥ ࢦ ࢧ ࢨ ࢩ ࢪ ࢫ ࢬ ࢭ ࢮ ࢯ ࢰ ࢱ ࢲ ࢳ ࢴ ࢵ ࢶ ࢷ ࢸ ࢹ ࢺ ࢻ ࢼ ࢽ ࢾ ࢿ ࣀ ࣁ ࣂ ࣃ ࣄ ࣅ ࣆ ࣇ ࣈ ࣉ ࣊ ࣋ ࣌ ࣍ ࣎ ࣏ ࣐ ࣑ ࣒ ࣓ ࣔ ࣕ ࣖ ࣗ ࣘ ࣙ ࣚ ࣛ ࣜ ࣝ ࣞ ࣟ ࣠ ࣡ ࣢ ࣣ ࣤ ࣥ ࣦ ࣧ ࣨ ࣩ ࣪ ࣫ ࣬ ࣭ ࣮ ࣯ ࣰ ࣱ ࣲ ࣳ ࣴ ࣵ ࣶ ࣷ ࣸ ࣹ ࣺ ࣻ ࣼ ࣽ ࣾ ࣿ ऀ ँ ं ः ऄ अ आ इ ई उ ऊ ऋ ऌ ऍ ऎ ए ऐ ऑ ऒ ओ औ क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न ऩ 
# प फ ब भ म य र ऱ ल ळ ऴ व श ष स ह ऺ ऻ ़ ऽ ा ि ी ु ू ृ ॄ ॅ ॆ े ै ॉ ॊ ो ौ ् ॎ ॏ ॐ ॑ ॒ ॓ ॔ ॕ ॖ ॗ क़ ख़ ग़ ज़ ड़ ढ़ फ़ य़ ॠ ॡ ॢ ॣ । ॥ ० १ २ ३ ४ ५ ६ ७ ८ ९ ॰ ॱ ॲ ॳ ॴ ॵ ॶ ॷ ॸ ॹ ॺ ॻ ॼ ॽ ॾ ॿ ঀ ঁ ং ঃ ঄ অ আ ই ঈ উ ঊ ঋ ঌ ঍ ঎
#  এ ঐ ঑ ঒ ও ঔ ক খ গ ঘ ঙ চ ছ জ ঝ ঞ ট ঠ ড ঢ ণ ত থ দ ধ ন ঩ প ফ ব ভ ম য র ঱ ল ঳ ঴ ঵ শ ষ স হ ঺ ঻ ় ঽ া ি ী ু ূ ৃ ৄ ৅ ৆ ে ৈ ৉ ৊ ো ৌ ্ ৎ ৏ ৐ ৑ ৒ ৓ ৔ ৕ ৖ ৗ ৘ ৙ ৚ ৛ ড় ঢ় ৞ য় ৠ ৡ ৢ ৣ ৤ ৥ ০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯ ৰ ৱ ৲ 
# ৳ ৴ ৵ ৶ ৷ ৸ ৹ ৺ ৻ ৼ ৽ ৾ ৿ ਀ ਁ ਂ ਃ ਄ ਅ ਆ ਇ ਈ ਉ ਊ ਋ ਌ ਍ ਎ ਏ ਐ ਑ ਒ ਓ ਔ ਕ ਖ ਗ ਘ ਙ ਚ ਛ ਜ ਝ ਞ ਟ ਠ ਡ ਢ ਣ ਤ ਥ ਦ ਧ ਨ ਩ ਪ ਫ ਬ ਭ ਮ ਯ ਰ ਱ ਲ ਲ਼ ਴ ਵ ਸ਼ ਷ ਸ ਹ ਺ ਻ ਼ ਽ ਾ ਿ ੀ ੁ ੂ ੃ ੄ ੅ ੆ ੇ ੈ ੉ ੊ ੋ ੌ ੍ ੎ ੏ ੐ ੑ ੒ ੓ ੔ ੕ ੖ ੗
#  ੘ ਖ਼ ਗ਼ ਜ਼ ੜ ੝ ਫ਼ ੟ ੠ ੡ ੢ ੣ ੤ ੥ ੦ ੧ ੨ ੩ ੪ ੫ ੬ ੭ ੮ ੯ ੰ ੱ ੲ ੳ ੴ ੵ ੶ ੷ ੸ ੹ ੺ ੻ ੼ ੽ ੾ ੿ ઀ ઁ ં ઃ ઄ અ આ ઇ ઈ ઉ ઊ ઋ ઌ ઍ ઎ એ ઐ ઑ ઒ ઓ ઔ ક ખ ગ ઘ ઙ ચ છ જ ઝ ઞ ટ ઠ ડ ઢ ણ ત થ દ ધ ન ઩ પ ફ બ ભ મ ય ર ઱ લ ળ ઴ વ શ ષ સ હ ઺ ઻ 
# ઼ ઽ ા િ ી ુ ૂ ૃ ૄ ૅ ૆ ે ૈ ૉ ૊ ો ૌ ્ ૎ ૏ ૐ ૑ ૒ ૓ ૔ ૕ ૖ ૗ ૘ ૙ ૚ ૛ ૜ ૝ ૞ ૟ ૠ ૡ ૢ ૣ ૤ ૥ ૦ ૧ ૨ ૩ ૪ ૫ ૬ ૭ ૮ ૯ ૰ ૱ ૲ ૳ ૴ ૵ ૶ ૷ ૸ ૹ ૺ ૻ ૼ ૽ ૾ ૿ ଀ ଁ ଂ ଃ ଄ ଅ ଆ ଇ ଈ ଉ ଊ ଋ ଌ ଍ ଎ ଏ ଐ ଑ ଒ ଓ ଔ କ ଖ ଗ ଘ ଙ ଚ ଛ ଜ ଝ ଞ ଟ ଠ
#  ଡ ଢ ଣ ତ ଥ ଦ ଧ ନ ଩ ପ ଫ ବ ଭ ମ ଯ ର ଱ ଲ ଳ ଴ ଵ ଶ ଷ ସ ହ ଺ ଻ ଼ ଽ ା ି ୀ ୁ ୂ ୃ ୄ ୅ ୆ େ ୈ ୉ ୊ ୋ ୌ ୍ ୎ ୏ ୐ ୑ ୒ ୓ ୔ ୕ ୖ ୗ ୘ ୙ ୚ ୛ ଡ଼ ଢ଼ ୞ ୟ ୠ ୡ ୢ ୣ ୤ ୥ ୦ ୧ ୨ ୩ ୪ ୫ ୬ ୭ ୮ ୯ ୰ ୱ ୲ ୳ ୴ ୵ ୶ ୷ ୸ ୹ ୺ ୻ ୼ ୽ ୾ ୿ ஀ ஁ ஂ ஃ ஄ 
# அ ஆ இ ஈ உ ஊ ஋ ஌ ஍ எ ஏ ஐ ஑ ஒ ஓ ஔ க ஖ ஗ ஘ ங ச ஛ ஜ ஝ ஞ ட ஠ ஡ ஢ ண த ஥ ஦ ஧ ந ன ப ஫ ஬ ஭ ம ய ர ற ல ள ழ வ ஶ ஷ ஸ ஹ ஺ ஻ ஼ ஽ ா ி ீ ு ூ ௃ ௄ ௅ ெ ே ை ௉ ொ ோ ௌ ் ௎ ௏ ௐ ௑ ௒ ௓ ௔ ௕ ௖ ௗ ௘ ௙ ௚ ௛ ௜ ௝ ௞ ௟ ௠ ௡ ௢ ௣ ௤ ௥ ௦ ௧ ௨ ௩
#  ௪ ௫ ௬ ௭ ௮ ௯ ௰ ௱ ௲ ௳ ௴ ௵ ௶ ௷ ௸ ௹ ௺ ௻ ௼ ௽ ௾ ௿ ఀ ఁ ం ః ఄ అ ఆ ఇ ఈ ఉ ఊ ఋ ఌ ఍ ఎ ఏ ఐ ఑ ఒ ఓ ఔ క ఖ గ ఘ ఙ చ ఛ జ ఝ ఞ ట ఠ డ ఢ ణ త థ ద ధ న ఩ ప ఫ బ భ మ య ర ఱ ల ళ ఴ వ శ ష స హ ఺ ఻ ఼ ఽ ా ి ీ ు ూ ృ ౄ ౅ ె ే ై ౉ ొ ో ౌ ్ 
# ౎ ౏ ౐ ౑ ౒ ౓ ౔ ౕ ౖ ౗ ౘ ౙ ౚ ౛ ౜ ౝ ౞ ౟ ౠ ౡ ౢ ౣ ౤ ౥ ౦ ౧ ౨ ౩ ౪ ౫ ౬ ౭ ౮ ౯ ౰ ౱ ౲ ౳ ౴ ౵ ౶ ౷ ౸ ౹ ౺ ౻ ౼ ౽ ౾ ౿ ಀ ಁ ಂ ಃ ಄ ಅ ಆ ಇ ಈ ಉ ಊ ಋ ಌ ಍ ಎ ಏ ಐ ಑ ಒ ಓ ಔ ಕ ಖ ಗ ಘ ಙ ಚ ಛ ಜ ಝ ಞ ಟ ಠ ಡ ಢ ಣ ತ ಥ ದ ಧ ನ ಩ ಪ ಫ ಬ ಭ ಮ ಯ ರ ಱ ಲ
#  ಳ ಴ ವ ಶ ಷ ಸ ಹ ಺ ಻ ಼ ಽ ಾ ಿ ೀ ು ೂ ೃ ೄ ೅ ೆ ೇ ೈ ೉ ೊ ೋ ೌ ್ ೎ ೏ ೐ ೑ ೒ ೓ ೔ ೕ ೖ ೗ ೘ ೙ ೚ ೛ ೜ ೝ ೞ ೟ ೠ ೡ ೢ ೣ ೤ ೥ ೦ ೧ ೨ ೩ ೪ ೫ ೬ ೭ ೮ ೯ ೰ ೱ ೲ ೳ ೴ ೵ ೶ ೷ ೸ ೹ ೺ ೻ ೼ ೽ ೾ ೿ ഀ ഁ ം ഃ ഄ അ ആ ഇ ഈ ഉ ഊ ഋ ഌ ഍ എ ഏ ഐ ഑ ഒ ഓ ഔ ക ഖ 
# ഗ ഘ ങ ച ഛ ജ ഝ ഞ ട ഠ ഡ ഢ ണ ത ഥ ദ ധ ന ഩ പ ഫ ബ ഭ മ യ ര റ ല ള ഴ വ ശ ഷ സ ഹ ഺ ഻ ഼ ഽ ാ ി ീ ു ൂ ൃ ൄ ൅ െ േ ൈ ൉ ൊ ോ ൌ ് ൎ ൏ ൐ ൑ ൒ ൓ ൔ ൕ ൖ ൗ ൘ ൙ ൚ ൛ ൜ ൝ ൞ ൟ ൠ ൡ ൢ ൣ ൤ ൥ ൦ ൧ ൨ ൩ ൪ ൫ ൬ ൭ ൮ ൯ ൰ ൱ ൲ ൳ ൴ ൵ ൶ ൷ ൸ ൹ ൺ ൻ
#  ർ ൽ ൾ ൿ ඀ ඁ ං ඃ ඄ අ ආ ඇ ඈ ඉ ඊ උ ඌ ඍ ඎ ඏ ඐ එ ඒ ඓ ඔ ඕ ඖ ඗ ඘ ඙ ක ඛ ග ඝ ඞ ඟ ච ඡ ජ ඣ ඤ ඥ ඦ ට ඨ ඩ ඪ ණ ඬ ත ථ ද ධ න ඲ ඳ ප ඵ බ භ ම ඹ ය ර ඼ ල ඾ ඿ ව ශ ෂ ස හ ළ ෆ ෇ ෈ ෉ ් ෋ ෌ ෍ ෎ ා ැ ෑ ි ී ු ෕ ූ ෗ ෘ ෙ ේ ෛ ො ෝ ෞ ෟ 
# ෠ ෡ ෢ ෣ ෤ ෥ ෦ ෧ ෨ ෩ ෪ ෫ ෬ ෭ ෮ ෯ ෰ ෱ ෲ ෳ ෴ ෵ ෶ ෷ ෸ ෹ ෺ ෻ ෼ ෽ ෾ ෿ ฀ ก ข ฃ ค ฅ ฆ ง จ ฉ ช ซ ฌ ญ ฎ ฏ ฐ ฑ ฒ ณ ด ต ถ ท ธ น บ ป ผ ฝ พ ฟ ภ ม ย ร ฤ ล ฦ ว ศ ษ ส ห ฬ อ ฮ ฯ ะ ั า ำ ิ ี ึ ื ุ ู ฺ ฻ ฼ ฽ ฾ ฿ เ แ โ ใ ไ
#  ๅ ๆ ็ ่ ้ ๊ ๋ ์ ํ ๎ ๏ ๐ ๑ ๒ ๓ ๔ ๕ ๖ ๗ ๘ ๙ ๚ ๛ ๜ ๝ ๞ ๟ ๠ ๡ ๢ ๣ ๤ ๥ ๦ ๧ ๨ ๩ ๪ ๫ ๬ ๭ ๮ ๯ ๰ ๱ ๲ ๳ ๴ ๵ ๶ ๷ ๸ ๹ ๺ ๻ ๼ ๽ ๾ ๿ ຀ ກ ຂ ຃ ຄ ຅ ຆ ງ ຈ ຉ ຊ ຋ ຌ ຍ ຎ ຏ ຐ ຑ ຒ ຓ ດ ຕ ຖ ທ ຘ ນ ບ ປ ຜ ຝ ພ ຟ ຠ ມ ຢ ຣ ຤ ລ ຦ ວ ຨ 
# ຩ ສ ຫ ຬ ອ ຮ ຯ ະ ັ າ ຳ ິ ີ ຶ ື ຸ ູ ຺ ົ ຼ ຽ ຾ ຿ ເ ແ ໂ ໃ ໄ ໅ ໆ ໇ ່ ້ ໊ ໋ ໌ ໍ ໎ ໏ ໐ ໑ ໒ ໓ ໔ ໕ ໖ ໗ ໘ ໙ ໚ ໛ ໜ ໝ ໞ ໟ ໠ ໡ ໢ ໣ ໤ ໥ ໦ ໧ ໨ ໩ ໪ ໫ ໬ ໭ ໮ ໯ ໰ ໱ ໲ ໳ ໴ ໵ ໶ ໷ ໸ ໹ ໺ ໻ ໼ ໽ ໾ ໿ ༀ ༁ ༂ ༃ ༄ ༅ ༆ ༇ ༈ ༉ ༊ ་ ༌ །
#  ༎ ༏ ༐ ༑ ༒ ༓ ༔ ༕ ༖ ༗ ༘ ༙ ༚ ༛ ༜ ༝ ༞ ༟ ༠ ༡ ༢ ༣ ༤ ༥ ༦ ༧ ༨ ༩ ༪ ༫ ༬ ༭ ༮ ༯ ༰ ༱ ༲ ༳ ༴ ༵ ༶ ༷ ༸ ༹ ༺ ༻ ༼ ༽ ༾ ༿ ཀ ཁ ག གྷ ང ཅ ཆ ཇ ཈ ཉ ཊ ཋ ཌ ཌྷ ཎ ཏ ཐ ད དྷ ན པ ཕ བ བྷ མ ཙ ཚ ཛ ཛྷ ཝ ཞ ཟ འ ཡ ར ལ ཤ ཥ ས ཧ ཨ ཀྵ ཪ ཫ ཬ ཭ ཮ ཯ ཰ ཱ 
# ི ཱི ུ ཱུ ྲྀ ཷ ླྀ ཹ ེ ཻ ོ ཽ ཾ ཿ ྀ ཱྀ ྂ ྃ ྄ ྅ ྆ ྇ ྈ ྉ ྊ ྋ ྌ ྍ ྎ ྏ ྐ ྑ ྒ ྒྷ ྔ ྕ ྖ ྗ ྘ ྙ ྚ ྛ ྜ ྜྷ ྞ ྟ ྠ ྡ ྡྷ ྣ ྤ ྥ ྦ ྦྷ ྨ ྩ ྪ ྫ ྫྷ ྭ ྮ ྯ ྰ ྱ ྲ ླ ྴ ྵ ྶ ྷ ྸ ྐྵ ྺ ྻ ྼ ྽ ྾ ྿ ࿀ ࿁ ࿂ ࿃ ࿄ ࿅ ࿆ ࿇ ࿈ ࿉ ࿊ ࿋ ࿌ ࿍ ࿎ ࿏ ࿐ ࿑ ࿒ ࿓ ࿔ ࿕ ࿖
#  ࿗ ࿘ ࿙ ࿚ ࿛ ࿜ ࿝ ࿞ ࿟ ࿠ ࿡ ࿢ ࿣ ࿤ ࿥ ࿦ ࿧ ࿨ ࿩ ࿪ ࿫ ࿬ ࿭ ࿮ ࿯ ࿰ ࿱ ࿲ ࿳ ࿴ ࿵ ࿶ ࿷ ࿸ ࿹ ࿺ ࿻ ࿼ ࿽ ࿾ ࿿ က ခ ဂ ဃ င စ ဆ ဇ ဈ ဉ ည ဋ ဌ ဍ ဎ ဏ တ ထ ဒ ဓ န ပ ဖ ဗ ဘ မ ယ ရ လ ဝ သ ဟ ဠ အ ဢ ဣ ဤ ဥ ဦ ဧ ဨ ဩ ဪ ါ ာ ိ ီ ု ူ ေ ဲ ဳ ဴ ဵ ံ ့ း ္ ် 
# ျ ြ ွ ှ ဿ ၀ ၁ ၂ ၃ ၄ ၅ ၆ ၇ ၈ ၉ ၊ ။ ၌ ၍ ၎ ၏ ၐ ၑ ၒ ၓ ၔ ၕ ၖ ၗ ၘ ၙ ၚ ၛ ၜ ၝ ၞ ၟ ၠ ၡ ၢ ၣ ၤ ၥ ၦ ၧ ၨ ၩ ၪ ၫ ၬ ၭ ၮ ၯ ၰ ၱ ၲ ၳ ၴ ၵ ၶ ၷ ၸ ၹ ၺ ၻ ၼ ၽ ၾ ၿ ႀ ႁ ႂ ႃ ႄ ႅ ႆ ႇ ႈ ႉ ႊ ႋ ႌ ႍ ႎ ႏ ႐ ႑ ႒ ႓ ႔ ႕ ႖ ႗ ႘ ႙ ႚ ႛ ႜ ႝ ႞ ႟
#  Ⴀ Ⴁ Ⴂ Ⴃ Ⴄ Ⴅ Ⴆ Ⴇ Ⴈ Ⴉ Ⴊ Ⴋ Ⴌ Ⴍ Ⴎ Ⴏ Ⴐ Ⴑ Ⴒ Ⴓ Ⴔ Ⴕ Ⴖ Ⴗ Ⴘ Ⴙ Ⴚ Ⴛ Ⴜ Ⴝ Ⴞ Ⴟ Ⴠ Ⴡ Ⴢ Ⴣ Ⴤ Ⴥ ჆ Ⴧ ჈ ჉ ჊ ჋ ჌ Ⴭ ჎ ჏ ა ბ გ დ ე ვ ზ თ ი კ ლ მ ნ ო პ ჟ რ ს ტ უ ფ ქ ღ ყ შ ჩ ც ძ წ ჭ ხ ჯ ჰ ჱ ჲ ჳ ჴ ჵ ჶ ჷ ჸ ჹ ჺ ჻ ჼ ჽ ჾ ჿ ᄀ ᄁ ᄂ
#  ᄃ ᄄ ᄅ ᄆ ᄇ ᄈ ᄉ ᄊ ᄋ ᄌ ᄍ ᄎ ᄏ ᄐ ᄑ ᄒ ᄓ ᄔ ᄕ ᄖ ᄗ ᄘ ᄙ ᄚ ᄛ ᄜ ᄝ ᄞ ᄟ ᄠ ᄡ ᄢ ᄣ ᄤ ᄥ ᄦ ᄧ ᄨ ᄩ ᄪ ᄫ ᄬ ᄭ ᄮ ᄯ ᄰ ᄱ ᄲ ᄳ ᄴ ᄵ ᄶ ᄷ ᄸ ᄹ ᄺ ᄻ ᄼ ᄽ ᄾ ᄿ ᅀ ᅁ ᅂ ᅃ ᅄ ᅅ
#  ᅆ ᅇ ᅈ ᅉ ᅊ ᅋ ᅌ ᅍ ᅎ ᅏ ᅐ ᅑ ᅒ ᅓ ᅔ ᅕ ᅖ ᅗ ᅘ ᅙ ᅚ ᅛ ᅜ ᅝ ᅞ ᅟ ᅠ ᅡ ᅢ ᅣ ᅤ ᅥ ᅦ ᅧ ᅨ ᅩ ᅪ ᅫ ᅬ ᅭ ᅮ ᅯ ᅰ ᅱ ᅲ ᅳ ᅴ ᅵ ᅶ ᅷ ᅸ ᅹ ᅺ ᅻ ᅼ ᅽ ᅾ ᅿ ᆀ ᆁ ᆂ ᆃ ᆄ ᆅ ᆆ ᆇ ᆈ ᆉ ᆊ ᆋ ᆌ ᆍ ᆎ ᆏ ᆐ ᆑ ᆒ ᆓ ᆔ ᆕ ᆖ ᆗ ᆘ ᆙ ᆚ ᆛ ᆜ 
# ᆝ ᆞ ᆟ ᆠ ᆡ ᆢ ᆣ ᆤ ᆥ ᆦ ᆧ ᆨ ᆩ ᆪ ᆫ ᆬ ᆭ ᆮ ᆯ ᆰ ᆱ ᆲ ᆳ ᆴ ᆵ ᆶ ᆷ ᆸ ᆹ ᆺ ᆻ ᆼ ᆽ ᆾ ᆿ ᇀ ᇁ ᇂ ᇃ ᇄ ᇅ ᇆ ᇇ ᇈ ᇉ ᇊ ᇋ ᇌ ᇍ ᇎ ᇏ ᇐ ᇑ ᇒ ᇓ ᇔ ᇕ ᇖ ᇗ ᇘ ᇙ ᇚ ᇛ ᇜ ᇝ ᇞ ᇟ ᇠ ᇡ ᇢ ᇣ ᇤ ᇥ ᇦ ᇧ ᇨ ᇩ ᇪ ᇫ ᇬ ᇭ ᇮ ᇯ ᇰ ᇱ ᇲ ᇳ ᇴ ᇵ ᇶ ᇷ ᇸ ᇹ ᇺ ᇻ ᇼ ᇽ ᇾ ᇿ ሀ ሁ
#  ሂ ሃ ሄ ህ ሆ ሇ ለ ሉ ሊ ላ ሌ ል ሎ ሏ ሐ ሑ ሒ ሓ ሔ ሕ ሖ ሗ መ ሙ ሚ ማ ሜ ም ሞ ሟ ሠ ሡ ሢ ሣ ሤ ሥ ሦ ሧ ረ ሩ ሪ ራ ሬ ር ሮ ሯ ሰ ሱ ሲ ሳ ሴ ስ ሶ ሷ ሸ ሹ ሺ ሻ ሼ ሽ ሾ ሿ ቀ ቁ ቂ ቃ ቄ ቅ ቆ ቇ ቈ ቉ ቊ ቋ ቌ ቍ ቎ ቏ ቐ ቑ ቒ ቓ ቔ ቕ ቖ ቗ ቘ ቙ ቚ ቛ ቜ ቝ ቞ ቟ በ ቡ ቢ ባ ቤ ብ 
# ቦ ቧ ቨ ቩ ቪ ቫ ቬ ቭ ቮ ቯ ተ ቱ ቲ ታ ቴ ት ቶ ቷ ቸ ቹ ቺ ቻ ቼ ች ቾ ቿ ኀ ኁ ኂ ኃ ኄ ኅ ኆ ኇ ኈ ኉ ኊ ኋ ኌ ኍ ኎ ኏ ነ ኑ ኒ ና ኔ ን ኖ ኗ ኘ ኙ ኚ ኛ ኜ ኝ ኞ ኟ አ ኡ ኢ ኣ ኤ እ ኦ ኧ ከ ኩ ኪ ካ ኬ ክ ኮ ኯ ኰ ኱ ኲ ኳ ኴ ኵ ኶ ኷ ኸ ኹ ኺ ኻ ኼ ኽ ኾ ኿ ዀ ዁ ዂ ዃ ዄ ዅ ዆ ዇ ወ ዉ ዊ ዋ ዌ ው ዎ ዏ ዐ ዑ ዒ ዓ ዔ ዕ ዖ ዗ ዘ ዙ ዚ ዛ ዜ ዝ ዞ ዟ ዠ ዡ ዢ ዣ ዤ ዥ ዦ ዧ የ ዩ ዪ ያ ዬ ይ ዮ ዯ ደ ዱ ዲ ዳ ዴ ድ ዶ ዷ ዸ ዹ ዺ ዻ ዼ ዽ ዾ ዿ ጀ ጁ ጂ ጃ ጄ ጅ ጆ ጇ ገ ጉ ጊ ጋ ጌ ግ ጎ ጏ ጐ ጑ ጒ ጓ ጔ ጕ ጖ ጗ ጘ ጙ ጚ ጛ ጜ ጝ ጞ ጟ ጠ ጡ ጢ ጣ ጤ ጥ ጦ ጧ ጨ ጩ ጪ ጫ ጬ ጭ ጮ 
# ጯ ጰ ጱ ጲ ጳ ጴ ጵ ጶ ጷ ጸ ጹ ጺ ጻ ጼ ጽ ጾ ጿ ፀ ፁ ፂ ፃ ፄ ፅ ፆ ፇ ፈ ፉ ፊ ፋ ፌ ፍ ፎ ፏ ፐ ፑ ፒ ፓ ፔ ፕ ፖ ፗ ፘ ፙ ፚ ፛ ፜ ፝ ፞ ፟ ፠ ፡ ። ፣ ፤ ፥ ፦ ፧ ፨ ፩ ፪ ፫ ፬ ፭ ፮ ፯ ፰ ፱ ፲ ፳ ፴ ፵ ፶ ፷ ፸ ፹ ፺ ፻ ፼ ፽ ፾ ፿ ᎀ ᎁ ᎂ ᎃ ᎄ ᎅ ᎆ ᎇ ᎈ ᎉ ᎊ ᎋ ᎌ ᎍ ᎎ ᎏ ᎐ ᎑ ᎒ ᎓
#  ᎔ ᎕ ᎖ ᎗ ᎘ ᎙ ᎚ ᎛ ᎜ ᎝ ᎞ ᎟ Ꭰ Ꭱ Ꭲ Ꭳ Ꭴ Ꭵ Ꭶ Ꭷ Ꭸ Ꭹ Ꭺ Ꭻ Ꭼ Ꭽ Ꭾ Ꭿ Ꮀ Ꮁ Ꮂ Ꮃ Ꮄ Ꮅ Ꮆ Ꮇ Ꮈ Ꮉ Ꮊ Ꮋ Ꮌ Ꮍ Ꮎ Ꮏ Ꮐ Ꮑ Ꮒ Ꮓ Ꮔ Ꮕ Ꮖ Ꮗ Ꮘ Ꮙ Ꮚ Ꮛ Ꮜ Ꮝ Ꮞ Ꮟ Ꮠ Ꮡ Ꮢ Ꮣ Ꮤ Ꮥ Ꮦ Ꮧ Ꮨ Ꮩ Ꮪ Ꮫ Ꮬ Ꮭ Ꮮ Ꮯ Ꮰ Ꮱ Ꮲ Ꮳ Ꮴ Ꮵ Ꮶ Ꮷ Ꮸ Ꮹ Ꮺ Ꮻ Ꮼ Ꮽ Ꮾ Ꮿ Ᏸ Ᏹ Ᏺ Ᏻ Ᏼ Ᏽ ᏶ ᏷ 
# ᏸ ᏹ ᏺ ᏻ ᏼ ᏽ ᏾ ᏿ ᐀ ᐁ ᐂ ᐃ ᐄ ᐅ ᐆ ᐇ ᐈ ᐉ ᐊ ᐋ ᐌ ᐍ ᐎ ᐏ ᐐ ᐑ ᐒ ᐓ ᐔ ᐕ ᐖ ᐗ ᐘ ᐙ ᐚ ᐛ ᐜ ᐝ ᐞ ᐟ ᐠ ᐡ ᐢ ᐣ ᐤ ᐥ ᐦ ᐧ ᐨ ᐩ ᐪ ᐫ ᐬ ᐭ ᐮ ᐯ ᐰ ᐱ ᐲ ᐳ ᐴ ᐵ ᐶ ᐷ ᐸ ᐹ ᐺ ᐻ ᐼ ᐽ ᐾ ᐿ ᑀ ᑁ ᑂ ᑃ ᑄ ᑅ ᑆ ᑇ ᑈ ᑉ ᑊ ᑋ ᑌ ᑍ ᑎ ᑏ ᑐ ᑑ ᑒ ᑓ ᑔ ᑕ ᑖ ᑗ ᑘ ᑙ ᑚ ᑛ ᑜ ᑝ ᑞ ᑟ ᑠ ᑡ ᑢ ᑣ ᑤ ᑥ ᑦ ᑧ ᑨ ᑩ ᑪ ᑫ ᑬ ᑭ ᑮ ᑯ ᑰ ᑱ ᑲ ᑳ ᑴ ᑵ ᑶ ᑷ ᑸ ᑹ ᑺ ᑻ ᑼ ᑽ ᑾ ᑿ ᒀ ᒁ ᒂ ᒃ ᒄ ᒅ ᒆ ᒇ ᒈ ᒉ ᒊ ᒋ ᒌ ᒍ ᒎ ᒏ ᒐ ᒑ ᒒ ᒓ ᒔ ᒕ ᒖ ᒗ ᒘ ᒙ ᒚ ᒛ ᒜ ᒝ ᒞ ᒟ ᒠ ᒡ ᒢ ᒣ ᒤ ᒥ ᒦ ᒧ ᒨ ᒩ ᒪ ᒫ ᒬ ᒭ ᒮ ᒯ ᒰ ᒱ ᒲ ᒳ ᒴ ᒵ ᒶ ᒷ ᒸ ᒹ ᒺ ᒻ ᒼ ᒽ ᒾ ᒿ ᓀ 
# ᓁ ᓂ ᓃ ᓄ ᓅ ᓆ ᓇ ᓈ ᓉ ᓊ ᓋ ᓌ ᓍ ᓎ ᓏ ᓐ ᓑ ᓒ ᓓ ᓔ ᓕ ᓖ ᓗ ᓘ ᓙ ᓚ ᓛ ᓜ ᓝ ᓞ ᓟ ᓠ ᓡ ᓢ ᓣ ᓤ ᓥ ᓦ ᓧ ᓨ ᓩ ᓪ ᓫ ᓬ ᓭ ᓮ ᓯ ᓰ ᓱ ᓲ ᓳ ᓴ ᓵ ᓶ ᓷ ᓸ ᓹ ᓺ ᓻ ᓼ ᓽ ᓾ ᓿ ᔀ ᔁ ᔂ ᔃ ᔄ ᔅ ᔆ ᔇ ᔈ ᔉ ᔊ ᔋ ᔌ ᔍ ᔎ ᔏ ᔐ ᔑ ᔒ ᔓ ᔔ ᔕ ᔖ ᔗ ᔘ ᔙ ᔚ ᔛ ᔜ ᔝ ᔞ ᔟ ᔠ ᔡ ᔢ ᔣ ᔤ ᔥ ᔦ ᔧ ᔨ ᔩ ᔪ ᔫ ᔬ ᔭ ᔮ ᔯ ᔰ ᔱ ᔲ ᔳ ᔴ ᔵ ᔶ ᔷ ᔸ ᔹ ᔺ ᔻ ᔼ ᔽ ᔾ ᔿ ᕀ ᕁ ᕂ ᕃ ᕄ ᕅ ᕆ ᕇ ᕈ ᕉ ᕊ ᕋ ᕌ ᕍ ᕎ ᕏ ᕐ ᕑ ᕒ ᕓ ᕔ ᕕ ᕖ ᕗ ᕘ ᕙ ᕚ ᕛ ᕜ ᕝ ᕞ ᕟ ᕠ ᕡ ᕢ ᕣ ᕤ ᕥ ᕦ ᕧ ᕨ ᕩ ᕪ ᕫ ᕬ ᕭ ᕮ ᕯ ᕰ ᕱ ᕲ ᕳ ᕴ ᕵ ᕶ ᕷ ᕸ ᕹ ᕺ ᕻ ᕼ ᕽ ᕾ ᕿ ᖀ ᖁ ᖂ ᖃ ᖄ ᖅ ᖆ ᖇ ᖈ ᖉ 
# ᖊ ᖋ ᖌ ᖍ ᖎ ᖏ ᖐ ᖑ ᖒ ᖓ ᖔ ᖕ ᖖ ᖗ ᖘ ᖙ ᖚ ᖛ ᖜ ᖝ ᖞ ᖟ ᖠ ᖡ ᖢ ᖣ ᖤ ᖥ ᖦ ᖧ ᖨ ᖩ ᖪ ᖫ ᖬ ᖭ ᖮ ᖯ ᖰ ᖱ ᖲ ᖳ ᖴ ᖵ ᖶ ᖷ ᖸ ᖹ ᖺ ᖻ ᖼ ᖽ ᖾ ᖿ ᗀ ᗁ ᗂ ᗃ ᗄ ᗅ ᗆ ᗇ ᗈ ᗉ ᗊ ᗋ ᗌ ᗍ ᗎ ᗏ ᗐ ᗑ ᗒ ᗓ ᗔ ᗕ ᗖ ᗗ ᗘ ᗙ ᗚ ᗛ ᗜ ᗝ ᗞ ᗟ ᗠ ᗡ ᗢ ᗣ ᗤ ᗥ ᗦ ᗧ ᗨ ᗩ ᗪ ᗫ ᗬ ᗭ ᗮ ᗯ ᗰ ᗱ ᗲ ᗳ ᗴ ᗵ ᗶ ᗷ ᗸ ᗹ ᗺ ᗻ ᗼ ᗽ ᗾ ᗿ ᘀ ᘁ ᘂ ᘃ ᘄ ᘅ ᘆ ᘇ ᘈ ᘉ ᘊ ᘋ ᘌ ᘍ ᘎ ᘏ ᘐ ᘑ ᘒ ᘓ ᘔ ᘕ ᘖ ᘗ ᘘ ᘙ ᘚ ᘛ ᘜ ᘝ ᘞ ᘟ ᘠ ᘡ ᘢ ᘣ ᘤ ᘥ ᘦ ᘧ ᘨ ᘩ ᘪ ᘫ ᘬ ᘭ ᘮ ᘯ ᘰ ᘱ ᘲ ᘳ ᘴ ᘵ ᘶ ᘷ ᘸ ᘹ ᘺ ᘻ ᘼ ᘽ ᘾ ᘿ ᙀ ᙁ ᙂ ᙃ ᙄ ᙅ ᙆ ᙇ ᙈ ᙉ ᙊ ᙋ ᙌ ᙍ ᙎ ᙏ ᙐ ᙑ ᙒ 
# ᙓ ᙔ ᙕ ᙖ ᙗ ᙘ ᙙ ᙚ ᙛ ᙜ ᙝ ᙞ ᙟ ᙠ ᙡ ᙢ ᙣ ᙤ ᙥ ᙦ ᙧ ᙨ ᙩ ᙪ ᙫ ᙬ ᙭ ᙮ ᙯ ᙰ ᙱ ᙲ ᙳ ᙴ ᙵ ᙶ ᙷ ᙸ ᙹ ᙺ ᙻ ᙼ ᙽ ᙾ ᙿ   ᚁ ᚂ ᚃ ᚄ ᚅ ᚆ ᚇ ᚈ ᚉ ᚊ ᚋ ᚌ ᚍ ᚎ ᚏ ᚐ ᚑ ᚒ ᚓ ᚔ ᚕ ᚖ ᚗ ᚘ ᚙ ᚚ ᚛ ᚜ ᚝ ᚞ ᚟ ᚠ ᚡ ᚢ ᚣ ᚤ ᚥ ᚦ ᚧ ᚨ ᚩ ᚪ ᚫ ᚬ ᚭ ᚮ ᚯ ᚰ ᚱ ᚲ ᚳ ᚴ ᚵ ᚶ ᚷ ᚸ ᚹ ᚺ ᚻ ᚼ ᚽ ᚾ ᚿ ᛀ ᛁ ᛂ ᛃ ᛄ ᛅ ᛆ ᛇ ᛈ ᛉ ᛊ ᛋ ᛌ ᛍ ᛎ ᛏ ᛐ ᛑ ᛒ ᛓ ᛔ ᛕ ᛖ ᛗ ᛘ ᛙ ᛚ ᛛ ᛜ ᛝ ᛞ ᛟ ᛠ ᛡ ᛢ ᛣ ᛤ ᛥ ᛦ ᛧ ᛨ ᛩ ᛪ ᛫ ᛬ ᛭ ᛮ ᛯ ᛰ ᛱ ᛲ ᛳ ᛴ ᛵ ᛶ ᛷ ᛸ ᛹ ᛺ ᛻ ᛼ ᛽ ᛾ ᛿ ᜀ ᜁ ᜂ ᜃ ᜄ ᜅ ᜆ ᜇ ᜈ ᜉ ᜊ ᜋ ᜌ ᜍ ᜎ ᜏ ᜐ ᜑ ᜒ ᜓ ᜔ ᜕ ᜖ ᜗ ᜘ ᜙ ᜚ ᜛ 
# ᜜ ᜝ ᜞ ᜟ ᜠ ᜡ ᜢ ᜣ ᜤ ᜥ ᜦ ᜧ ᜨ ᜩ ᜪ ᜫ ᜬ ᜭ ᜮ ᜯ ᜰ ᜱ ᜲ ᜳ ᜴ ᜵ ᜶ ᜷ ᜸ ᜹ ᜺ ᜻ ᜼ ᜽ ᜾ ᜿ ᝀ ᝁ ᝂ ᝃ ᝄ ᝅ ᝆ ᝇ ᝈ ᝉ ᝊ ᝋ ᝌ ᝍ ᝎ ᝏ ᝐ ᝑ ᝒ ᝓ ᝔ ᝕ ᝖ ᝗ ᝘ ᝙ ᝚ ᝛ ᝜ ᝝ ᝞ ᝟ ᝠ ᝡ ᝢ ᝣ ᝤ ᝥ ᝦ ᝧ ᝨ ᝩ ᝪ ᝫ ᝬ ᝭ ᝮ ᝯ ᝰ ᝱ ᝲ ᝳ ᝴ ᝵ ᝶ ᝷ ᝸ ᝹ ᝺ ᝻ ᝼ ᝽ ᝾ ᝿ ក
#  ខ គ ឃ ង ច ឆ ជ ឈ ញ ដ ឋ ឌ ឍ ណ ត ថ ទ ធ ន ប ផ ព ភ ម យ រ ល វ ឝ ឞ ស ហ ឡ អ ឣ ឤ ឥ ឦ ឧ ឨ ឩ ឪ ឫ ឬ ឭ ឮ ឯ ឰ ឱ ឲ ឳ ឴ ឵ ា ិ ី ឹ ឺ ុ ូ ួ ើ ឿ ៀ េ ែ ៃ ោ ៅ ំ ះ ៈ ៉ ៊ ់ ៌ ៍ ៎ ៏ ័ ៑ ្ ៓ ។ ៕ ៖ ៗ ៘ ៙ ៚ ៛ ៜ ៝ ៞ ៟ ០ ១ ២ ៣ ៤ 
# ៥ ៦ ៧ ៨ ៩ ៪ ៫ ៬ ៭ ៮ ៯ ៰ ៱ ៲ ៳ ៴ ៵ ៶ ៷ ៸ ៹ ៺ ៻ ៼ ៽ ៾ ៿ ᠀ ᠁ ᠂ ᠃ ᠄ ᠅ ᠆ ᠇ ᠈ ᠉ ᠊ ᠋ ᠌ ᠍ ᠎ ᠏ ᠐ ᠑ ᠒ ᠓ ᠔ ᠕ ᠖ ᠗ ᠘ ᠙ ᠚ ᠛ ᠜ ᠝ ᠞ ᠟ ᠠ ᠡ ᠢ ᠣ ᠤ ᠥ ᠦ ᠧ ᠨ ᠩ ᠪ ᠫ ᠬ ᠭ ᠮ ᠯ ᠰ ᠱ ᠲ ᠳ ᠴ ᠵ ᠶ ᠷ ᠸ ᠹ ᠺ ᠻ ᠼ ᠽ ᠾ ᠿ ᡀ ᡁ ᡂ ᡃ ᡄ ᡅ ᡆ ᡇ ᡈ ᡉ
#  ᡊ ᡋ ᡌ ᡍ ᡎ ᡏ ᡐ ᡑ ᡒ ᡓ ᡔ ᡕ ᡖ ᡗ ᡘ ᡙ ᡚ ᡛ ᡜ ᡝ ᡞ ᡟ ᡠ ᡡ ᡢ ᡣ ᡤ ᡥ ᡦ ᡧ ᡨ ᡩ ᡪ ᡫ ᡬ ᡭ ᡮ ᡯ ᡰ ᡱ ᡲ ᡳ ᡴ ᡵ ᡶ ᡷ ᡸ ᡹ ᡺ ᡻ ᡼ ᡽ ᡾ ᡿ ᢀ ᢁ ᢂ ᢃ ᢄ ᢅ ᢆ ᢇ ᢈ ᢉ ᢊ ᢋ ᢌ ᢍ ᢎ ᢏ ᢐ ᢑ ᢒ ᢓ ᢔ ᢕ ᢖ ᢗ ᢘ ᢙ ᢚ ᢛ ᢜ ᢝ ᢞ ᢟ ᢠ ᢡ ᢢ ᢣ ᢤ ᢥ ᢦ ᢧ ᢨ ᢩ ᢪ ᢫ ᢬ ᢭ 
# ᢮ ᢯ ᢰ ᢱ ᢲ ᢳ ᢴ ᢵ ᢶ ᢷ ᢸ ᢹ ᢺ ᢻ ᢼ ᢽ ᢾ ᢿ ᣀ ᣁ ᣂ ᣃ ᣄ ᣅ ᣆ ᣇ ᣈ ᣉ ᣊ ᣋ ᣌ ᣍ ᣎ ᣏ ᣐ ᣑ ᣒ ᣓ ᣔ ᣕ ᣖ ᣗ ᣘ ᣙ ᣚ ᣛ ᣜ ᣝ ᣞ ᣟ ᣠ ᣡ ᣢ ᣣ ᣤ ᣥ ᣦ ᣧ ᣨ ᣩ ᣪ ᣫ ᣬ ᣭ ᣮ ᣯ ᣰ ᣱ ᣲ ᣳ ᣴ ᣵ ᣶ ᣷ ᣸ ᣹ ᣺ ᣻ ᣼ ᣽ ᣾ ᣿ ᤀ ᤁ ᤂ ᤃ ᤄ ᤅ ᤆ ᤇ ᤈ ᤉ ᤊ ᤋ ᤌ ᤍ ᤎ ᤏ ᤐ ᤑ ᤒ ᤓ ᤔ ᤕ ᤖ ᤗ ᤘ ᤙ ᤚ ᤛ ᤜ ᤝ ᤞ ᤟ ᤠ ᤡ ᤢ ᤣ ᤤ ᤥ ᤦ ᤧ ᤨ ᤩ ᤪ ᤫ ᤬ ᤭ ᤮ ᤯ ᤰ ᤱ ᤲ ᤳ ᤴ ᤵ ᤶ ᤷ ᤸ ᤹ ᤺ ᤻ ᤼ ᤽ ᤾ ᤿ ᥀ ᥁ ᥂ ᥃ ᥄ ᥅ ᥆ ᥇ ᥈ ᥉ ᥊ ᥋ ᥌ ᥍ ᥎ ᥏ ᥐ ᥑ ᥒ ᥓ ᥔ ᥕ ᥖ ᥗ ᥘ ᥙ ᥚ ᥛ ᥜ ᥝ ᥞ ᥟ ᥠ ᥡ ᥢ ᥣ ᥤ ᥥ ᥦ ᥧ ᥨ ᥩ ᥪ ᥫ ᥬ ᥭ ᥮ ᥯ ᥰ ᥱ ᥲ ᥳ ᥴ ᥵ ᥶ 
# ᥷ ᥸ ᥹ ᥺ ᥻ ᥼ ᥽ ᥾ ᥿ ᦀ ᦁ ᦂ ᦃ ᦄ ᦅ ᦆ ᦇ ᦈ ᦉ ᦊ ᦋ ᦌ ᦍ ᦎ ᦏ ᦐ ᦑ ᦒ ᦓ ᦔ ᦕ ᦖ ᦗ ᦘ ᦙ ᦚ ᦛ ᦜ ᦝ ᦞ ᦟ ᦠ ᦡ ᦢ ᦣ ᦤ ᦥ ᦦ ᦧ ᦨ ᦩ ᦪ ᦫ ᦬ ᦭ ᦮ ᦯ ᦰ ᦱ ᦲ ᦳ ᦴ ᦵ ᦶ ᦷ ᦸ ᦹ ᦺ ᦻ ᦼ ᦽ ᦾ ᦿ ᧀ ᧁ ᧂ ᧃ ᧄ ᧅ ᧆ ᧇ ᧈ ᧉ ᧊ ᧋ ᧌ ᧍ ᧎ ᧏ ᧐ ᧑ ᧒ ᧓ ᧔ ᧕ ᧖ ᧗ ᧘ ᧙ ᧚ ᧛ ᧜ ᧝ ᧞ ᧟ ᧠ ᧡ ᧢ ᧣ ᧤ ᧥ ᧦ ᧧ ᧨ ᧩ ᧪ ᧫ ᧬ ᧭ ᧮ ᧯ ᧰ ᧱ ᧲ ᧳ ᧴ ᧵ ᧶ ᧷ ᧸ ᧹ ᧺ ᧻ ᧼ ᧽ ᧾ ᧿ ᨀ ᨁ ᨂ ᨃ ᨄ ᨅ ᨆ ᨇ ᨈ ᨉ ᨊ ᨋ ᨌ ᨍ ᨎ ᨏ ᨐ ᨑ ᨒ ᨓ ᨔ ᨕ ᨖ ᨗ ᨘ ᨙ ᨚ ᨛ ᨜ ᨝ ᨞ ᨟ ᨠ ᨡ ᨢ ᨣ ᨤ ᨥ ᨦ ᨧ ᨨ ᨩ ᨪ ᨫ ᨬ ᨭ ᨮ ᨯ ᨰ ᨱ ᨲ ᨳ ᨴ ᨵ ᨶ ᨷ ᨸ ᨹ ᨺ ᨻ ᨼ ᨽ ᨾ ᨿ 
# ᩀ ᩁ ᩂ ᩃ ᩄ ᩅ ᩆ ᩇ ᩈ ᩉ ᩊ ᩋ ᩌ ᩍ ᩎ ᩏ ᩐ ᩑ ᩒ ᩓ ᩔ ᩕ ᩖ ᩗ ᩘ ᩙ ᩚ ᩛ ᩜ ᩝ ᩞ ᩟ ᩠ ᩡ ᩢ ᩣ ᩤ ᩥ ᩦ ᩧ ᩨ ᩩ ᩪ ᩫ ᩬ ᩭ ᩮ ᩯ ᩰ ᩱ ᩲ ᩳ ᩴ ᩵ ᩶ ᩷ ᩸ ᩹ ᩺ ᩻ ᩼ ᩽ ᩾ ᩿ ᪀ ᪁ ᪂ ᪃ ᪄ ᪅ ᪆ ᪇ ᪈ ᪉ ᪊ ᪋ ᪌ ᪍ ᪎ ᪏ ᪐ ᪑ ᪒ ᪓ ᪔ ᪕ ᪖ ᪗ ᪘ ᪙ ᪚ ᪛ ᪜ ᪝ ᪞ ᪟ ᪠ ᪡ ᪢ ᪣ ᪤
#  ᪥ ᪦ ᪧ ᪨ ᪩ ᪪ ᪫ ᪬ ᪭ ᪮ ᪯ ᪰ ᪱ ᪲ ᪳ ᪴ ᪵ ᪶ ᪷ ᪸ ᪹ ᪺ ᪻ ᪼ ᪽ ᪾ ᪿ ᫀ ᫁ ᫂ ᫃ ᫄ ᫅ ᫆ ᫇ ᫈ ᫉ ᫊ ᫋ ᫌ ᫍ ᫎ ᫏ ᫐ ᫑ ᫒ ᫓ ᫔ ᫕ ᫖ ᫗ ᫘ ᫙ ᫚ ᫛ ᫜ ᫝ ᫞ ᫟ ᫠ ᫡ ᫢ ᫣ ᫤ ᫥ ᫦ ᫧ ᫨ ᫩ ᫪ ᫫ ᫬ ᫭ ᫮ ᫯ ᫰ ᫱ ᫲ ᫳ ᫴ ᫵ ᫶ ᫷ ᫸ ᫹ ᫺ ᫻ ᫼ ᫽ ᫾ ᫿ ᬀ ᬁ ᬂ ᬃ ᬄ ᬅ ᬆ ᬇ ᬈ 
# ᬉ ᬊ ᬋ ᬌ ᬍ ᬎ ᬏ ᬐ ᬑ ᬒ ᬓ ᬔ ᬕ ᬖ ᬗ ᬘ ᬙ ᬚ ᬛ ᬜ ᬝ ᬞ ᬟ ᬠ ᬡ ᬢ ᬣ ᬤ ᬥ ᬦ ᬧ ᬨ ᬩ ᬪ ᬫ ᬬ ᬭ ᬮ ᬯ ᬰ ᬱ ᬲ ᬳ ᬴ ᬵ ᬶ ᬷ ᬸ ᬹ ᬺ ᬻ ᬼ ᬽ ᬾ ᬿ ᭀ ᭁ ᭂ ᭃ ᭄ ᭅ ᭆ ᭇ ᭈ ᭉ ᭊ ᭋ ᭌ ᭍ ᭎ ᭏ ᭐ ᭑ ᭒ ᭓ ᭔ ᭕ ᭖ ᭗ ᭘ ᭙ ᭚ ᭛ ᭜ ᭝ ᭞ ᭟ ᭠ ᭡ ᭢ ᭣ ᭤ ᭥ ᭦ ᭧ ᭨ ᭩ ᭪ ᭫ ᭬ ᭭
#  ᭮ ᭯ ᭰ ᭱ ᭲ ᭳ ᭴ ᭵ ᭶ ᭷ ᭸ ᭹ ᭺ ᭻ ᭼ ᭽ ᭾ ᭿ ᮀ ᮁ ᮂ ᮃ ᮄ ᮅ ᮆ ᮇ ᮈ ᮉ ᮊ ᮋ ᮌ ᮍ ᮎ ᮏ ᮐ ᮑ ᮒ ᮓ ᮔ ᮕ ᮖ ᮗ ᮘ ᮙ ᮚ ᮛ ᮜ ᮝ ᮞ ᮟ ᮠ ᮡ ᮢ ᮣ ᮤ ᮥ ᮦ ᮧ ᮨ ᮩ ᮪ ᮫ ᮬ ᮭ ᮮ ᮯ ᮰ ᮱ ᮲ ᮳ ᮴ ᮵ ᮶ ᮷ ᮸ ᮹ ᮺ ᮻ ᮼ ᮽ ᮾ ᮿ ᯀ ᯁ ᯂ ᯃ ᯄ ᯅ ᯆ ᯇ ᯈ ᯉ ᯊ ᯋ ᯌ ᯍ ᯎ ᯏ ᯐ ᯑ 
# ᯒ ᯓ ᯔ ᯕ ᯖ ᯗ ᯘ ᯙ ᯚ ᯛ ᯜ ᯝ ᯞ ᯟ ᯠ ᯡ ᯢ ᯣ ᯤ ᯥ ᯦ ᯧ ᯨ ᯩ ᯪ ᯫ ᯬ ᯭ ᯮ ᯯ ᯰ ᯱ ᯲ ᯳ ᯴ ᯵ ᯶ ᯷ ᯸ ᯹ ᯺ ᯻ ᯼ ᯽ ᯾ ᯿ ᰀ ᰁ ᰂ ᰃ ᰄ ᰅ ᰆ ᰇ ᰈ ᰉ ᰊ ᰋ ᰌ ᰍ ᰎ ᰏ ᰐ ᰑ ᰒ ᰓ ᰔ ᰕ ᰖ ᰗ ᰘ ᰙ ᰚ ᰛ ᰜ ᰝ ᰞ ᰟ ᰠ ᰡ ᰢ ᰣ ᰤ ᰥ ᰦ ᰧ ᰨ ᰩ ᰪ ᰫ ᰬ ᰭ ᰮ ᰯ ᰰ ᰱ ᰲ ᰳ ᰴ ᰵ ᰶ
#  ᰷ ᰸ ᰹ ᰺ ᰻ ᰼ ᰽ ᰾ ᰿ ᱀ ᱁ ᱂ ᱃ ᱄ ᱅ ᱆ ᱇ ᱈ ᱉ ᱊ ᱋ ᱌ ᱍ ᱎ ᱏ ᱐ ᱑ ᱒ ᱓ ᱔ ᱕ ᱖ ᱗ ᱘ ᱙ ᱚ ᱛ ᱜ ᱝ ᱞ ᱟ ᱠ ᱡ ᱢ ᱣ ᱤ ᱥ ᱦ ᱧ ᱨ ᱩ ᱪ ᱫ ᱬ ᱭ ᱮ ᱯ ᱰ ᱱ ᱲ ᱳ ᱴ ᱵ ᱶ ᱷ ᱸ ᱹ ᱺ ᱻ ᱼ ᱽ ᱾ ᱿ ᲀ ᲁ ᲂ ᲃ ᲄ ᲅ ᲆ ᲇ ᲈ Ᲊ ᲊ ᲋ ᲌ ᲍ ᲎ ᲏ Ა Ბ Გ Დ Ე Ვ Ზ Თ Ი Კ Ლ 
# Მ Ნ Ო Პ Ჟ Რ Ს Ტ Უ Ფ Ქ Ღ Ყ Შ Ჩ Ც Ძ Წ Ჭ Ხ Ჯ Ჰ Ჱ Ჲ Ჳ Ჴ Ჵ Ჶ Ჷ Ჸ Ჹ Ჺ ᲻ ᲼ Ჽ Ჾ Ჿ ᳀ ᳁ ᳂ ᳃ ᳄ ᳅ ᳆ ᳇ ᳈ ᳉ ᳊ ᳋ ᳌ ᳍ ᳎ ᳏ ᳐ ᳑ ᳒ ᳓ ᳔ ᳕ ᳖ ᳗ ᳘ ᳙ ᳚ ᳛ ᳜ ᳝ ᳞ ᳟ ᳠ ᳡ ᳢ ᳣ ᳤ ᳥ ᳦ ᳧ ᳨ ᳩ ᳪ ᳫ ᳬ ᳭ ᳮ ᳯ ᳰ ᳱ ᳲ ᳳ ᳴ ᳵ ᳶ ᳷ ᳸ ᳹ ᳺ ᳻ ᳼ ᳽ ᳾ ᳿
#  ᴀ ᴁ ᴂ ᴃ ᴄ ᴅ ᴆ ᴇ ᴈ ᴉ ᴊ ᴋ ᴌ ᴍ ᴎ ᴏ ᴐ ᴑ ᴒ ᴓ ᴔ ᴕ ᴖ ᴗ ᴘ ᴙ ᴚ ᴛ ᴜ ᴝ ᴞ ᴟ ᴠ ᴡ ᴢ ᴣ ᴤ ᴥ ᴦ ᴧ ᴨ ᴩ ᴪ ᴫ ᴬ ᴭ ᴮ ᴯ ᴰ ᴱ ᴲ ᴳ ᴴ ᴵ ᴶ ᴷ ᴸ ᴹ ᴺ ᴻ ᴼ ᴽ ᴾ ᴿ ᵀ ᵁ ᵂ ᵃ ᵄ ᵅ ᵆ ᵇ ᵈ ᵉ ᵊ ᵋ ᵌ ᵍ ᵎ ᵏ ᵐ ᵑ ᵒ ᵓ ᵔ ᵕ ᵖ ᵗ ᵘ ᵙ ᵚ ᵛ ᵜ ᵝ ᵞ ᵟ ᵠ ᵡ ᵢ ᵣ 
# ᵤ ᵥ ᵦ ᵧ ᵨ ᵩ ᵪ ᵫ ᵬ ᵭ ᵮ ᵯ ᵰ ᵱ ᵲ ᵳ ᵴ ᵵ ᵶ ᵷ ᵸ ᵹ ᵺ ᵻ ᵼ ᵽ ᵾ ᵿ ᶀ ᶁ ᶂ ᶃ ᶄ ᶅ ᶆ ᶇ ᶈ ᶉ ᶊ ᶋ ᶌ ᶍ ᶎ ᶏ ᶐ ᶑ ᶒ ᶓ ᶔ ᶕ ᶖ ᶗ ᶘ ᶙ ᶚ ᶛ ᶜ ᶝ ᶞ ᶟ ᶠ ᶡ ᶢ ᶣ ᶤ ᶥ ᶦ ᶧ ᶨ ᶩ ᶪ ᶫ ᶬ ᶭ ᶮ ᶯ ᶰ ᶱ ᶲ ᶳ ᶴ ᶵ ᶶ ᶷ ᶸ ᶹ ᶺ ᶻ ᶼ ᶽ ᶾ ᶿ ᷀ ᷁ ᷂ ᷃ ᷄ ᷅ ᷆ ᷇ ᷈
#  ᷉ ᷊ ᷋ ᷌ ᷍ ᷎ ᷏ ᷐ ᷑ ᷒ ᷓ ᷔ ᷕ ᷖ ᷗ ᷘ ᷙ ᷚ ᷛ ᷜ ᷝ ᷞ ᷟ ᷠ ᷡ ᷢ ᷣ ᷤ ᷥ ᷦ ᷧ ᷨ ᷩ ᷪ ᷫ ᷬ ᷭ ᷮ ᷯ ᷰ ᷱ ᷲ ᷳ ᷴ ᷵ ᷶ ᷷ ᷸ ᷹ ᷺ ᷻ ᷼ ᷽ ᷾ ᷿ Ḁ ḁ Ḃ ḃ Ḅ ḅ Ḇ ḇ Ḉ ḉ Ḋ ḋ Ḍ ḍ Ḏ ḏ Ḑ ḑ Ḓ ḓ Ḕ ḕ Ḗ ḗ Ḙ ḙ Ḛ ḛ Ḝ ḝ Ḟ ḟ Ḡ ḡ Ḣ ḣ Ḥ ḥ Ḧ ḧ Ḩ ḩ Ḫ ḫ Ḭ 
# ḭ Ḯ ḯ Ḱ ḱ Ḳ ḳ Ḵ ḵ Ḷ ḷ Ḹ ḹ Ḻ ḻ Ḽ ḽ Ḿ ḿ Ṁ ṁ Ṃ ṃ Ṅ ṅ Ṇ ṇ Ṉ ṉ Ṋ ṋ Ṍ ṍ Ṏ ṏ Ṑ ṑ Ṓ ṓ Ṕ ṕ Ṗ ṗ Ṙ ṙ Ṛ ṛ Ṝ ṝ Ṟ ṟ Ṡ ṡ Ṣ ṣ Ṥ ṥ Ṧ ṧ Ṩ ṩ Ṫ ṫ Ṭ ṭ Ṯ ṯ Ṱ ṱ Ṳ ṳ Ṵ ṵ Ṷ ṷ Ṹ ṹ Ṻ ṻ Ṽ ṽ Ṿ ṿ Ẁ ẁ Ẃ ẃ Ẅ ẅ Ẇ ẇ Ẉ ẉ Ẋ ẋ Ẍ ẍ Ẏ ẏ Ẑ ẑ Ẓ ẓ Ẕ ẕ ẖ ẗ ẘ ẙ ẚ ẛ ẜ ẝ ẞ ẟ Ạ ạ Ả ả Ấ ấ Ầ ầ Ẩ ẩ Ẫ ẫ Ậ ậ Ắ ắ Ằ ằ Ẳ ẳ Ẵ ẵ Ặ ặ Ẹ ẹ Ẻ ẻ Ẽ ẽ Ế ế Ề ề Ể ể Ễ ễ Ệ ệ Ỉ ỉ Ị ị Ọ ọ Ỏ ỏ Ố ố Ồ ồ Ổ ổ Ỗ ỗ Ộ ộ Ớ ớ Ờ ờ Ở ở Ỡ ỡ Ợ ợ Ụ ụ Ủ ủ Ứ ứ Ừ ừ Ử ử Ữ ữ Ự ự Ỳ ỳ Ỵ ỵ 
# Ỷ ỷ Ỹ ỹ Ỻ ỻ Ỽ ỽ Ỿ ỿ ἀ ἁ ἂ ἃ ἄ ἅ ἆ ἇ Ἀ Ἁ Ἂ Ἃ Ἄ Ἅ Ἆ Ἇ ἐ ἑ ἒ ἓ ἔ ἕ ἖ ἗ Ἐ Ἑ Ἒ Ἓ Ἔ Ἕ ἞ ἟ ἠ ἡ ἢ ἣ ἤ ἥ ἦ ἧ Ἠ Ἡ Ἢ Ἣ Ἤ Ἥ Ἦ Ἧ ἰ ἱ ἲ ἳ ἴ ἵ ἶ ἷ Ἰ Ἱ Ἲ Ἳ Ἴ Ἵ Ἶ Ἷ ὀ ὁ ὂ ὃ ὄ ὅ ὆ ὇ Ὀ Ὁ Ὂ Ὃ Ὄ Ὅ ὎ ὏ ὐ ὑ ὒ ὓ ὔ ὕ ὖ ὗ ὘ Ὑ ὚ Ὓ ὜ Ὕ ὞ Ὗ ὠ ὡ ὢ ὣ ὤ ὥ ὦ ὧ Ὠ Ὡ Ὢ Ὣ Ὤ Ὥ Ὦ Ὧ ὰ ά ὲ έ ὴ ή ὶ ί ὸ ό ὺ ύ ὼ ώ ὾ ὿ ᾀ ᾁ ᾂ ᾃ ᾄ ᾅ ᾆ ᾇ ᾈ ᾉ ᾊ ᾋ ᾌ ᾍ ᾎ ᾏ ᾐ ᾑ ᾒ ᾓ ᾔ ᾕ ᾖ ᾗ ᾘ ᾙ ᾚ ᾛ ᾜ ᾝ ᾞ ᾟ ᾠ ᾡ ᾢ ᾣ ᾤ ᾥ ᾦ ᾧ ᾨ ᾩ ᾪ ᾫ ᾬ ᾭ ᾮ ᾯ ᾰ ᾱ ᾲ ᾳ ᾴ ᾵ ᾶ ᾷ Ᾰ Ᾱ Ὰ Ά ᾼ ᾽ ι 
# ᾿ ῀ ῁ ῂ ῃ ῄ ῅ ῆ ῇ Ὲ Έ Ὴ Ή ῌ ῍ ῎ ῏ ῐ ῑ ῒ ΐ ῔ ῕ ῖ ῗ Ῐ Ῑ Ὶ Ί ῜ ῝ ῞ ῟ ῠ ῡ ῢ ΰ ῤ ῥ ῦ ῧ Ῠ Ῡ Ὺ Ύ Ῥ ῭ ΅ ` ῰ ῱ ῲ ῳ ῴ ῵ ῶ ῷ Ὸ Ό Ὼ Ώ ῼ ´ ῾ ῿                       ​ ‌ ‍ ‎ ‏ ‐ ‑ ‒ – — ― ‖ ‗ ‘ ’ ‚ ‛ “ ” „ ‟ † ‡ • ‣
#  ․ ‥ … ‧     ‪ ‫ ‬ ‭ ‮   ‰ ‱ ′ ″ ‴ ‵ ‶ ‷ ‸ ‹ › ※ ‼ ‽ ‾ ‿ ⁀ ⁁ ⁂ ⁃ ⁄ ⁅ ⁆ ⁇ ⁈ ⁉ ⁊ ⁋ ⁌ ⁍ ⁎ ⁏ ⁐ ⁑ ⁒ ⁓ ⁔ ⁕ ⁖ ⁗ ⁘ ⁙ ⁚ ⁛ ⁜ ⁝ ⁞   ⁠ ⁡ ⁢ ⁣ ⁤ ⁥ ⁦ ⁧ ⁨ ⁩ ⁪ ⁫ ⁬ ⁭ ⁮ ⁯ ⁰ ⁱ ⁲ ⁳ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁺ ⁻ ⁼ ⁽ ⁾ ⁿ ₀ ₁ ₂ ₃ ₄ ₅ ₆ ₇ 
# ₈ ₉ ₊ ₋ ₌ ₍ ₎ ₏ ₐ ₑ ₒ ₓ ₔ ₕ ₖ ₗ ₘ ₙ ₚ ₛ ₜ ₝ ₞ ₟ ₠ ₡ ₢ ₣ ₤ ₥ ₦ ₧ ₨ ₩ ₪ ₫ € ₭ ₮ ₯ ₰ ₱ ₲ ₳ ₴ ₵ ₶ ₷ ₸ ₹ ₺ ₻ ₼ ₽ ₾ ₿ ⃀ ⃁ ⃂ ⃃ ⃄ ⃅ ⃆ ⃇ ⃈ ⃉ ⃊ ⃋ ⃌ ⃍ ⃎ ⃏ ⃐ ⃑ ⃒ ⃓ ⃔ ⃕ ⃖ ⃗ ⃘ ⃙ ⃚ ⃛ ⃜ ⃝ ⃞ ⃟ ⃠ ⃡ ⃢ ⃣ ⃤ ⃥ ⃦ ⃧ ⃨ ⃩ ⃪ ⃫ ⃬
#  ⃭ ⃮ ⃯ ⃰ ⃱ ⃲ ⃳ ⃴ ⃵ ⃶ ⃷ ⃸ ⃹ ⃺ ⃻ ⃼ ⃽ ⃾ ⃿ ℀ ℁ ℂ ℃ ℄ ℅ ℆ ℇ ℈ ℉ ℊ ℋ ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ ℔ ℕ № ℗ ℘ ℙ ℚ ℛ ℜ ℝ ℞ ℟ ℠ ℡ ™ ℣ ℤ ℥ Ω ℧ ℨ ℩ K Å ℬ ℭ ℮ ℯ ℰ ℱ Ⅎ ℳ ℴ ℵ ℶ ℷ ℸ ℹ ℺ ℻ ℼ ℽ ℾ ℿ ⅀ ⅁ ⅂ ⅃ ⅄ ⅅ ⅆ ⅇ ⅈ ⅉ ⅊ ⅋ ⅌ ⅍ ⅎ ⅏ ⅐ 
# ⅑ ⅒ ⅓ ⅔ ⅕ ⅖ ⅗ ⅘ ⅙ ⅚ ⅛ ⅜ ⅝ ⅞ ⅟ Ⅰ Ⅱ Ⅲ Ⅳ Ⅴ Ⅵ Ⅶ Ⅷ Ⅸ Ⅹ Ⅺ Ⅻ Ⅼ Ⅽ Ⅾ Ⅿ ⅰ ⅱ ⅲ ⅳ ⅴ ⅵ ⅶ ⅷ ⅸ ⅹ ⅺ ⅻ ⅼ ⅽ ⅾ ⅿ ↀ ↁ ↂ Ↄ ↄ ↅ ↆ ↇ ↈ ↉ ↊ ↋ ↌ ↍ ↎ ↏ ← ↑ → ↓ ↔ ↕ ↖ ↗ ↘ ↙ ↚ ↛ ↜ ↝ ↞ ↟ ↠ ↡ ↢ ↣ ↤ ↥ ↦ ↧ ↨ ↩ ↪ ↫ ↬ ↭ ↮ ↯ ↰ ↱ ↲ ↳ ↴ ↵ ↶ ↷ ↸ ↹ ↺ ↻ ↼ ↽ ↾ ↿ ⇀ ⇁ ⇂ ⇃ ⇄ ⇅ ⇆ ⇇ ⇈ ⇉ ⇊ ⇋ ⇌ ⇍ ⇎ ⇏ ⇐ ⇑ ⇒ ⇓ ⇔ ⇕ ⇖ ⇗ ⇘ ⇙ ⇚ ⇛ ⇜ ⇝ ⇞ ⇟ ⇠ ⇡ ⇢ ⇣ ⇤ ⇥ ⇦ ⇧ ⇨ ⇩ ⇪ ⇫ ⇬ ⇭ ⇮ ⇯ ⇰ ⇱ ⇲ ⇳ ⇴ ⇵ ⇶ ⇷ ⇸ ⇹ ⇺ ⇻ ⇼ ⇽ ⇾ ⇿ ∀ ∁ ∂ ∃ ∄ ∅ ∆ ∇ ∈ ∉ ∊ ∋ ∌ ∍ ∎ ∏ ∐ ∑ − ∓ ∔ ∕ ∖ ∗ ∘ ∙ 
# √ ∛ ∜ ∝ ∞ ∟ ∠ ∡ ∢ ∣ ∤ ∥ ∦ ∧ ∨ ∩ ∪ ∫ ∬ ∭ ∮ ∯ ∰ ∱ ∲ ∳ ∴ ∵ ∶ ∷ ∸ ∹ ∺ ∻ ∼ ∽ ∾ ∿ ≀ ≁ ≂ ≃ ≄ ≅ ≆ ≇ ≈ ≉ ≊ ≋ ≌ ≍ ≎ ≏ ≐ ≑ ≒ ≓ ≔ ≕ ≖ ≗ ≘ ≙ ≚ ≛ ≜ ≝ ≞ ≟ ≠ ≡ ≢ ≣ ≤ ≥ ≦ ≧ ≨ ≩ ≪ ≫ ≬ ≭ ≮ ≯ ≰ ≱ ≲ ≳ ≴ ≵ ≶ ≷ ≸ ≹ ≺ ≻ ≼ ≽ ≾ ≿ ⊀ ⊁ ⊂ ⊃ ⊄ ⊅ ⊆ ⊇ ⊈ ⊉ ⊊ ⊋ ⊌ ⊍ ⊎ ⊏ ⊐ ⊑ ⊒ ⊓ ⊔ ⊕ ⊖ ⊗ ⊘ ⊙ ⊚ ⊛ ⊜ ⊝ ⊞ ⊟ ⊠ ⊡ ⊢ ⊣ ⊤ ⊥ ⊦ ⊧ ⊨ ⊩ ⊪ ⊫ ⊬ ⊭ ⊮ ⊯ ⊰ ⊱ ⊲ ⊳ ⊴ ⊵ ⊶ ⊷ ⊸ ⊹ ⊺ ⊻ ⊼ ⊽ ⊾ ⊿ ⋀ ⋁ ⋂ ⋃ ⋄ ⋅ ⋆ ⋇ ⋈ ⋉ ⋊ ⋋ ⋌ ⋍ ⋎ ⋏ ⋐ ⋑ ⋒ ⋓ ⋔ ⋕ ⋖ ⋗ ⋘ ⋙ ⋚ ⋛ ⋜ ⋝ ⋞ ⋟ ⋠ ⋡ ⋢ 
# ⋣ ⋤ ⋥ ⋦ ⋧ ⋨ ⋩ ⋪ ⋫ ⋬ ⋭ ⋮ ⋯ ⋰ ⋱ ⋲ ⋳ ⋴ ⋵ ⋶ ⋷ ⋸ ⋹ ⋺ ⋻ ⋼ ⋽ ⋾ ⋿ ⌀ ⌁ ⌂ ⌃ ⌄ ⌅ ⌆ ⌇ ⌈ ⌉ ⌊ ⌋ ⌌ ⌍ ⌎ ⌏ ⌐ ⌑ ⌒ ⌓ ⌔ ⌕ ⌖ ⌗ ⌘ ⌙ ⌚ ⌛ ⌜ ⌝ ⌞ ⌟ ⌠ ⌡ ⌢ ⌣ ⌤ ⌥ ⌦ ⌧ ⌨ 〈 〉 ⌫ ⌬ ⌭ ⌮ ⌯ ⌰ ⌱ ⌲ ⌳ ⌴ ⌵ ⌶ ⌷ ⌸ ⌹ ⌺ ⌻ ⌼ ⌽ ⌾ ⌿ ⍀ ⍁ ⍂ ⍃ ⍄ ⍅ ⍆
#  ⍇ ⍈ ⍉ ⍊ ⍋ ⍌ ⍍ ⍎ ⍏ ⍐ ⍑ ⍒ ⍓ ⍔ ⍕ ⍖ ⍗ ⍘ ⍙ ⍚ ⍛ ⍜ ⍝ ⍞ ⍟ ⍠ ⍡ ⍢ ⍣ ⍤ ⍥ ⍦ ⍧ ⍨ ⍩ ⍪ ⍫ ⍬ ⍭ ⍮ ⍯ ⍰ ⍱ ⍲ ⍳ ⍴ ⍵ ⍶ ⍷ ⍸ ⍹ ⍺ ⍻ ⍼ ⍽ ⍾ ⍿ ⎀ ⎁ ⎂ ⎃ ⎄ ⎅ ⎆ ⎇ ⎈ ⎉ ⎊ ⎋ ⎌ ⎍ ⎎ ⎏ ⎐ ⎑ ⎒ ⎓ ⎔ ⎕ ⎖ ⎗ ⎘ ⎙ ⎚ ⎛ ⎜ ⎝ ⎞ ⎟ ⎠ ⎡ ⎢ ⎣ ⎤ ⎥ ⎦ ⎧ ⎨ ⎩ ⎪ 
# ⎫ ⎬ ⎭ ⎮ ⎯ ⎰ ⎱ ⎲ ⎳ ⎴ ⎵ ⎶ ⎷ ⎸ ⎹ ⎺ ⎻ ⎼ ⎽ ⎾ ⎿ ⏀ ⏁ ⏂ ⏃ ⏄ ⏅ ⏆ ⏇ ⏈ ⏉ ⏊ ⏋ ⏌ ⏍ ⏎ ⏏ ⏐ ⏑ ⏒ ⏓ ⏔ ⏕ ⏖ ⏗ ⏘ ⏙ ⏚ ⏛ ⏜ ⏝ ⏞ ⏟ ⏠ ⏡ ⏢ ⏣ ⏤ ⏥ ⏦ ⏧ ⏨ ⏩ ⏪ ⏫ ⏬ ⏭ ⏮ ⏯ ⏰ ⏱ ⏲ ⏳ ⏴ ⏵ ⏶ ⏷ ⏸ ⏹ ⏺ ⏻ ⏼ ⏽ ⏾ ⏿ ␀ ␁ ␂ ␃ ␄ ␅ ␆ ␇ ␈ ␉ ␊ ␋ ␌ ␍ ␎ ␏
#  ␐ ␑ ␒ ␓ ␔ ␕ ␖ ␗ ␘ ␙ ␚ ␛ ␜ ␝ ␞ ␟ ␠ ␡ ␢ ␣ ␤ ␥ ␦ ␧ ␨ ␩ ␪ ␫ ␬ ␭ ␮ ␯ ␰ ␱ ␲ ␳ ␴ ␵ ␶ ␷ ␸ ␹ ␺ ␻ ␼ ␽ ␾ ␿ ⑀ ⑁ ⑂ ⑃ ⑄ ⑅ ⑆ ⑇ ⑈ ⑉ ⑊ ⑋ ⑌ ⑍ ⑎ ⑏ ⑐ ⑑ ⑒ ⑓ ⑔ ⑕ ⑖ ⑗ ⑘ ⑙ ⑚ ⑛ ⑜ ⑝ ⑞ ⑟ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳ 
# ⑴ ⑵ ⑶ ⑷ ⑸ ⑹ ⑺ ⑻ ⑼ ⑽ ⑾ ⑿ ⒀ ⒁ ⒂ ⒃ ⒄ ⒅ ⒆ ⒇ ⒈ ⒉ ⒊ ⒋ ⒌ ⒍ ⒎ ⒏ ⒐ ⒑ ⒒ ⒓ ⒔ ⒕ ⒖ ⒗ ⒘ ⒙ ⒚ ⒛ ⒜ ⒝ ⒞ ⒟ ⒠ ⒡ ⒢ ⒣ ⒤ ⒥ ⒦ ⒧ ⒨ ⒩ ⒪ ⒫ ⒬ ⒭ ⒮ ⒯ ⒰ ⒱ ⒲ ⒳ ⒴ ⒵ Ⓐ Ⓑ Ⓒ Ⓓ Ⓔ Ⓕ Ⓖ Ⓗ Ⓘ Ⓙ Ⓚ Ⓛ Ⓜ Ⓝ Ⓞ Ⓟ Ⓠ Ⓡ Ⓢ Ⓣ Ⓤ Ⓥ Ⓦ Ⓧ Ⓨ Ⓩ ⓐ ⓑ ⓒ ⓓ ⓔ ⓕ ⓖ ⓗ ⓘ ⓙ ⓚ ⓛ ⓜ ⓝ ⓞ ⓟ ⓠ ⓡ ⓢ ⓣ ⓤ ⓥ ⓦ ⓧ ⓨ ⓩ ⓪ ⓫ ⓬ ⓭ ⓮ ⓯ ⓰ ⓱ ⓲ ⓳ ⓴ ⓵ ⓶ ⓷ ⓸ ⓹ ⓺ ⓻ ⓼ ⓽ ⓾ ⓿ ─ ━ │ ┃ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋ ┌ ┍ ┎ ┏ ┐ ┑ ┒ ┓ └ ┕ ┖ ┗ ┘ ┙ ┚ ┛ ├ ┝ ┞ ┟ ┠ ┡ ┢ ┣ ┤ ┥ ┦ ┧ ┨ ┩ ┪ ┫ ┬ ┭ ┮ ┯ ┰ ┱ ┲ ┳ ┴ ┵ ┶ ┷ ┸ ┹ ┺ ┻ ┼ 
# ┽ ┾ ┿ ╀ ╁ ╂ ╃ ╄ ╅ ╆ ╇ ╈ ╉ ╊ ╋ ╌ ╍ ╎ ╏ ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟ ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╪ ╫ ╬ ╭ ╮ ╯ ╰ ╱ ╲ ╳ ╴ ╵ ╶ ╷ ╸ ╹ ╺ ╻ ╼ ╽ ╾ ╿ ▀ ▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▉ ▊ ▋ ▌ ▍ ▎ ▏ ▐ ░ ▒ ▓ ▔ ▕ ▖ ▗ ▘ ▙ ▚ ▛ ▜ ▝ ▞ ▟ ■ □ ▢ ▣ ▤ ▥ ▦ ▧ ▨ ▩ ▪ ▫ ▬ ▭ ▮ ▯ ▰ ▱ ▲ △ ▴ ▵ ▶ ▷ ▸ ▹ ► ▻ ▼ ▽ ▾ ▿ ◀ ◁ ◂ ◃ ◄ ◅ ◆ ◇ ◈ ◉ ◊ ○ ◌ ◍ ◎ ● ◐ ◑ ◒ ◓ ◔ ◕ ◖ ◗ ◘ ◙ ◚ ◛ ◜ ◝ ◞ ◟ ◠ ◡ ◢ ◣ ◤ ◥ ◦ ◧ ◨ ◩ ◪ ◫ ◬ ◭ ◮ ◯ ◰ ◱ ◲ ◳ ◴ ◵ ◶ ◷ ◸ ◹ ◺ ◻ ◼ ◽ ◾ ◿ ☀ ☁ ☂ ☃ ☄ ★ 
# ☆ ☇ ☈ ☉ ☊ ☋ ☌ ☍ ☎ ☏ ☐ ☑ ☒ ☓ ☔ ☕ ☖ ☗ ☘ ☙ ☚ ☛ ☜ ☝ ☞ ☟ ☠ ☡ ☢ ☣ ☤ ☥ ☦ ☧ ☨ ☩ ☪ ☫ ☬ ☭ ☮ ☯ ☰ ☱ ☲ ☳ ☴ ☵ ☶ ☷ ☸ ☹ ☺ ☻ ☼ ☽ ☾ ☿ ♀ ♁ ♂ ♃ ♄ ♅ ♆ ♇ ♈ ♉ ♊ ♋ ♌ ♍ ♎ ♏ ♐ ♑ ♒ ♓ ♔ ♕ ♖ ♗ ♘ ♙ ♚ ♛ ♜ ♝ ♞ ♟ ♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ♪
#  ♫ ♬ ♭ ♮ ♯ ♰ ♱ ♲ ♳ ♴ ♵ ♶ ♷ ♸ ♹ ♺ ♻ ♼ ♽ ♾ ♿ ⚀ ⚁ ⚂ ⚃ ⚄ ⚅ ⚆ ⚇ ⚈ ⚉ ⚊ ⚋ ⚌ ⚍ ⚎ ⚏ ⚐ ⚑ ⚒ ⚓ ⚔ ⚕ ⚖ ⚗ ⚘ ⚙ ⚚ ⚛ ⚜ ⚝ ⚞ ⚟ ⚠ ⚡ ⚢ ⚣ ⚤ ⚥ ⚦ ⚧ ⚨ ⚩ ⚪ ⚫ ⚬ ⚭ ⚮ ⚯ ⚰ ⚱ ⚲ ⚳ ⚴ ⚵ ⚶ ⚷ ⚸ ⚹ ⚺ ⚻ ⚼ ⚽ ⚾ ⚿ ⛀ ⛁ ⛂ ⛃ ⛄ ⛅ ⛆ ⛇ ⛈ ⛉ ⛊ ⛋ ⛌ ⛍ ⛎ 
# ⛏ ⛐ ⛑ ⛒ ⛓ ⛔ ⛕ ⛖ ⛗ ⛘ ⛙ ⛚ ⛛ ⛜ ⛝ ⛞ ⛟ ⛠ ⛡ ⛢ ⛣ ⛤ ⛥ ⛦ ⛧ ⛨ ⛩ ⛪ ⛫ ⛬ ⛭ ⛮ ⛯ ⛰ ⛱ ⛲ ⛳ ⛴ ⛵ ⛶ ⛷ ⛸ ⛹ ⛺ ⛻ ⛼ ⛽ ⛾ ⛿ ✀ ✁ ✂ ✃ ✄ ✅ ✆ ✇ ✈ ✉ ✊ ✋ ✌ ✍ ✎ ✏ ✐

# ascii=65
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(ascii),end="")
#         ascii+=1
#     print()    
# Output:
# ABCD
# EFGH
# IJKL
# MNOP

# iterable 1
# ascii=65:->ascii=65
# for i in range(1,5):->for i in 1
#     for j in range(1,5):->for j in 1
#         print(chr(ascii),end=""):->print(chr(65),end="")->print(A)
#         ascii+=1     ascii=65+1=66
#     print()    

# iterable 2 
#     for j in range(1,5):->for j in 2
#         print(chr(ascii),end=""):->print(chr(66),end="")->print(B)
#         ascii+=1     ascii=66+1=67
#     print()    

# ascii_value = 65

# for i in range(1, 5):
#     for j in range(1, 5):
#         print(chr(ascii_value), end="")
#     ascii_value += 1
#     print()
# Output:
# AAAA
# BBBB
# CCCC
# DDDD

# iterable 1
# ascii_value = 65:->ascii_value=65

# for i in range(1, 5):->for i in 1
#     for j in range(1, 5):for j in 1
#         print(chr(ascii_value), end=""):->print(chr(65), end="")->print(A)
#     ascii_value += 1
#     print()

# iterable 2
#     for j in range(1, 5):for j in 2
#         print(chr(ascii_value), end=""):->print(chr(65), end="")->print(A)
#     ascii_value += 1
#     print()

# iterable 3
#     for j in range(1, 5):for j in 3
#         print(chr(ascii_value), end=""):->print(chr(65), end="")->print(A)
#     ascii_value += 1
#     print()

# iterable 4
#     for j in range(1, 5):for j in 4
#         print(chr(ascii_value), end=""):->print(chr(65), end="")->print(A)
#     ascii_value += 1      ascii_value =65+1->66   
#     print()->execute hoga aur next line pai jayega

# ascii_value = 65

# for i in range(4):
#     for j in range(4):
#         print(chr(ascii_value), end="")
#     ascii_value += 1
#     print()
# Output:
# AAAA
# BBBB
# CCCC
# DDDD

# for i in range(4):
#     for j in range(4):
#         print(chr(65 + j), end="")
#     print()
# Output:
# ABCD
# ABCD
# ABCD
# ABCD

# ascii=65
# for i in range(1,5):
#     for j in range(1,5):
#         print(chr(ascii),end="")
#     ascii+=1
#     print()    
# Output:
# AAAA
# BBBB
# CCCC
# DDDD

# for i in range(65,69):
#     for j in range(1,5):
#         print(chr(i),end="")
#     print()    
# Output:
# AAAA
# BBBB
# CCCC
# DDDD

# for i in range(1,5):
#     for j in range(65,69):
#         print(chr(j),end="")
#     print()
# Output:
# ABCD
# ABCD
# ABCD
# ABCD

# iterable 1
# for i in range(1,5):for i in 1 
#     for j in range(65,69):->for j in 65
#         print(chr(j),end=""):->print(chr(65),end="")->print(A)
#     print()

# iterable 2
#     for j in range(65,69):->for j in 66
#         print(chr(j),end=""):->print(chr(66),end="")->print(B)
#     print()


# for i in range(1,5):
#     for j in range(65,69):
#         if(i%2==0):
#             print("*",end="")
#         else:
#             print(chr(j),end="")
#     print()
# Output:
# ABCD
# ****
# ABCD
# ****

# iterable 1
# for i in range(1,5):->for i in 1
#     for j in range(65,69):->for j in 65
#         if(i%2==0):->1%2==0->remainder1->False
#             print("*",end="")
#         else:
#             print(chr(j),end=""):->print(chr(65),end="")->print(A)
#     print()

    
# asci=65
# for i in range(1,5):
#     for j in range(1,5):
#         if j%2==0:
#             print("*",end="")

#         else:
#             print(chr(asci),end="")
#         asci+=1                          #isme harr baar asci run hoga if ho ya else ho because bahar hai asci
#     print()
# Output:
# A*C*
# E*G*
# I*K*
# M*O*

# iterable 1
# asci=65:->asci=65
# for i in range(1,5):-> for i in 1
#     for j in range(1,5):->for j in 1
#         if j%2==0:->1%2==0->remainder1->False
#             print("*",end="")

#         else:
#             print(chr(asci),end=""):->print(chr(65),end="")->print(A)
#         asci+=1       asci=65+1=66
#     print()

# iterable 2
#     for j in range(1,5):->for j in 2
#         if j%2==0:->2%2==0->remainder0->True
#             print("*",end=""):->print(*)

#         else:
#             print(chr(asci),end=""):->print(chr(65),end="")->print(A)
#         asci+=1       asci=66+1=67
#     print()


# asci = 65
# for i in range(1, 5):
#     for j in range(1, 5):
#         if j % 2 == 0:
#             print("*", end="")
#         else:
#             print(chr(asci), end="")
#             asci += 1                        #else aane pai asci run hoga bas because asci andarr hai else ke
#     print()
# Output:
# A*B*
# C*D*
# E*F*
# G*H*

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end="")
#     print() 
# Output:
# *
# **
# ***
# ****

# iterable 1
# i=1    1<5->True
# j=1    1<2->True(1,1+1)
# *
# j=2    2<2->False

# iterable 2
# i=2     2<5->True
# j=1    1<3->True
# *
# j=2    2<3->True
# *(baajo mai print hoga)
# j=3    3<3->False

# iterable 3
# 1=3     3<5->True
# j=1     1<4->True
# *
# j=2     2<4->True
# *(baajo mai print hoga)
# j=3     3<4->True
# *(baajo mai print hoga)
# j=4     4<4->False

# same program
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end="")
#     print() 
# Output:
# *
# **
# ***
# ****


# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=" ")
#     print()
# Output:
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 

# iterable 1
# for i in range(1, 5):->for i in 1
#     for j in range(i):->for j in range(1)->for j in range(0,1)->for j in 0
#         print(i, end=" "):->print(1)
#     print()
# Output:1

# iterable 2
# for i in range(1, 5):->for i in 2
#     for j in range(i):->for j in range(2)->for j in range(0,2)->for j in 0
#         print(i, end=" "):->print(2)
#     print()
# Output:1
#        2

# iterable 3
# for i in range(1, 5):->for i in 2
#     for j in range(i):->for j in range(2)->for j in range(0,2)->for j in 1
#         print(i, end=" "):->print(2)
#     print()
# Output:1
#        2 2

# iterable 4
# for i in range(1, 5):->for i in 3
#     for j in range(i):->for j in range(3)->for j in range(0,3)->for j in 0
#         print(i, end=" "):->print(3)
#     print()
# Output:1
#        2 2
#        3

# iterable 5
# for i in range(1, 5):->for i in 3
#     for j in range(i):->for j in range(3)->for j in range(0,3)->for j in 1
#         print(i, end=" "):->print(3)
#     print()
# Output:1
#        2 2
#        3 3

# iterable 6
# for i in range(1, 5):->for i in 3
#     for j in range(i):->for j in range(3)->for j in range(0,3)->for j in 2
#         print(i, end=" "):->print(3)
#     print()
# Output:1
#        2 2
#        3 3 3



# for i in range(1, 5):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()
# Output:
# A 
# A B 
# A B C 
# A B C D 

# iterable 1
# for i in range(1, 5):->for i in 1
#     for j in range(i):->for j in range(1)->for j in range(0,1)->for j in 0
#         print(chr(65 + j), end=" "):->print(chr(65 + 0), end=" ")->print(65)->print(A)
#     print()->yeh execute hoga because j ka loop khatam hogaya
# Output:
# A 

# iterable 2
# for i in range(1, 5):->for i in 2
#     for j in range(i):->for j in range(2)->for j in range(0,2)->for j in 0
#         print(chr(65 + j), end=" "):->print(chr(65 + 0), end=" ")->print(65)->print(A)
#     print()
# Output:
# A 
# A

# iterable 3
# for i in range(1, 5):->for i in 2
#     for j in range(i):->for j in range(2)->for j in range(0,2)->for j in 1
#         print(chr(65 + j), end=" "):->print(chr(65 + 1), end=" ")->print(66)->print(B)
#     print()->yeh execute hoga because j ka loop khatam hogaya
# Output:
# A 
# A B

# for i in range(1,5):
#     for j in range(4,i-1,-1):
#         print("*",end="")
#     print()
# Output:
# ****
# ***
# **
# *

# iterable 1
# for i in range(1,5):->for i in 1
#     for j in range(4,i-1,-1):->for j in range(4,1-1,-1)->for j in range(4,0,-1)->for j in 4
#         print("*",end=""):->priint(*)
#     print()
# Output:
# *

# iterable 2
#     for j in range(4,i-1,-1):->for j in range(4,1-1,-1)->for j in range(4,0,-1)->for j in 3
#         print("*",end=""):->priint(*)
#     print()
# Output:
# **



# for i in range(1,5):
#     for j in range(4,i-1,-1):
#         if(j==i):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# Output:
#    *
#   *
#  *
# *

# for i in range(1,5):
#     for j in range(1,i+1):
#         if(j==i):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# Output:
# *   
#  *  
#   * 
#    *

# for i in range(1, 5):
#     for j in range(1, 5):
#         if j == i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# Output:
# *
#  *
#   *
#    *

# for i in range(1,5):
#     for j in range(4,i-1,-1):
#         if(j==i):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# for i in range(2,5):
#     for j in range(1,i+1):
#         if(j==i):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
# Output:

#    *
#   *
#  *
# *
#  *
#   *
#    *


# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for i in range(3, 0, -1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# Output:
# * 
# * *
# * * *
# * * * *
# * * *
# * *
# *


# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

# for i in range(1,4):
#     for j in range(3,i-1,-1):
#         print("*", end=" ")
#     print()
# Output:
# * 
# * *
# * * *
# * * * *
# * * *
# * *
# *

# for i in range(1,5):
#     for j in range(2,i+1):
#         print(" ",end="")

#     for k in range(4,i-1,-1):
#         print("*",end="")

#     print()
# Output:
# ****
#  ***
#   **
#    *

# iterable 1
# for i in range(1,5):->for i in 1
#     for j in range(2,i+1):->for j in range(2,1+1)->for j in range(2,2)
#         print(" ",end="")

#    for k in range(4,i-1,-1):->for k in range(4,1-1,-1)->for k in range(4,0,-1)->for k in 4
#        print("*",end=""):->print(*)

#    print()

# iterable 2

#    for k in range(4,i-1,-1):->for k in range(4,1-1,-1)->for k in range(4,0,-1)->for k in 3
#        print("*",end=""):->print(*)

#    print()

# iterable 3

#    for k in range(4,i-1,-1):->for k in range(4,1-1,-1)->for k in range(4,0,-1)->for k in 2
#        print("*",end=""):->print(*)

#    print()

# iterable 4

#    for k in range(4,i-1,-1):->for k in range(4,1-1,-1)->for k in range(4,0,-1)->for k in 1
#        print("*",end=""):->print(*)->****

#    print()

# for i in range(1,5):
#     for j in range(3,i-1,-1):
#         print(" ",end="")

#     for k in range(1,i+1):
#         print("*",end="")
#     print()
# Output:
#    *
#   **
#  ***
# ****

# for i in range(1,5):
#     for j in range(3,i-1,-1):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("* ",end="")
#     print()
# Output:
#    * 
#   * * 
#  * * * 
# * * * * 

# x=[2,8,5,6,10,3]

# for i in range(0,len(x)):
#     for j in range(i+1,len(x)):
#         if(x[j]<x[i]):
#             x[i],x[j]=x[j],x[i]

# print(x)
# Output:
# [2, 3, 5, 6, 8, 10]

##a = [1001, 1002, 1003, 1004, 1005]
## reversed_a = a[::-1]
## print(reversed_a)

# #a = [1001, 1002, 1003, 1004, 1005]
# #reversed_a = []

## while a:
##     element = a.pop()
##     reversed_a.append(element)

## print(reversed_a)

## deep copy means same location refer karna 
## shallow copy means different location refer karna

# a=[1001,1002,1003,1004,1005]

# for i in range(0,len(a)//2):
#     start=i
#     end=len(a)-(i+1)
#     a[start],a[end]=a[end],a[start]
# print(a)
# Output:
# [1005, 1004, 1003, 1002, 1001]
# interview question:-
# find max key value pair
# find min key value pair

# d={'a':10,'b':20,'c':30}

# for k,v in d.items():
#     print(k,v)

# interview question
# a=["Hello","Hi","Hello","Hey","Bye"]
# d={ }

# for i in a:
#     d[i]=d.get(i,0)+1
# print(d)    
# Output:
# {'Hello': 2, 'Hi': 1, 'Hey': 1, 'Bye': 1}

# ----------------------------------------------------------Basic questions------------------------------------------------------
# HW 
# 1.take input from user and print its inputvalue using input function

# user_input = input("Enter a value: ")
# print("You entered:", user_input)

# Output:
# Enter a value: zaid
# You entered: zaid

# 2.create a string and print the last element

# my_string = "Hello, World!"
# last_element = my_string[-1]
# print("Last element:", last_element)

# Output: 
# Last element: !

# 3.create a string and print second last element

# my_string = "Hello, World!"
# second_last_element = my_string[-2]
# print("Second-to-last element:", second_last_element)

# Output:
# Second-to-last element: d

# 4.create a string as eg:"hellohellohellohello" and print it

# my_string = "hello" * 4
# print(my_string)

# Output:
# hellohellohellohello

# 5.create  two string like "hello" and "world" and print "helloworld"

# string1 = "hello"
# string2 = "world"
# result_string = string1 + string2
# print(result_string)

# Output:
# helloworld

# 6.create two variable and swap its value eg a=10,b=20 afer swapping there output is a=20,b=10

# a=10 
# b=20
# a,b=b,a
# print(a)
# print(b)

# Output:
# 20
# 10

# 7.create a tuple like(1,2,3,4,3,2) and count number of  occurrences  of 3

# my_tuple = (1, 2, 3, 4, 3, 2)
# count_of_3 = my_tuple.count(3)

# print("Number of occurrences of 3:", count_of_3)

# Output:
# Number of occurrences of 3: 2

# 8.create a tuple like(1,2,3,4,3,2) and print the index number of 3

# my_tuple = (1, 2, 3, 4, 3, 2)
# index_of_3 = my_tuple.index(3)

# print("Index of the first occurrence of 3:", index_of_3)

# Output:
# Index of the first occurrence of 3: 2

# 9.create a tuple like(1,2,3,4,3,2) and print (2,3,4) only

# my_tuple = (1, 2, 3, 4, 3, 2)
# selected_elements = my_tuple[1:4]

# print(selected_elements)

# Output:
# (2, 3, 4)

# 10.create tuple like(1,2,3,4,3,2) and remove 3 in this tuple
# original_tuple = (1, 2, 3, 4, 3, 2)
# element_to_remove = 3

# # Convert tuple to list
# tuple_list = list(original_tuple)

# # Remove all occurrences of the specified element from the list
# while element_to_remove in tuple_list:
#     tuple_list.remove(element_to_remove)

# # Convert the list back to a tuple
# original_tuple = tuple(tuple_list)

# print(original_tuple)
# Output:
# (1, 2, 4, 2)

# 11.create a list like[1,2,3,4] and change the elements like[1,2,4,3] without using list methods
# original_list = [1, 2, 3, 4]

# # Change the order of elements
# original_list[2], original_list[3] = original_list[3], original_list[2]

# print(original_list)
# Output:
# [1, 2, 4, 3]

# 12.create a list like[1,2,3,4] and delete all the elements in list and print empty list without using any method 
# original_list = [1, 2, 3, 4]

# # Delete all elements in the list without using list methods
# original_list = []

# print(original_list)
# # Output:
# # []

# 13.create single value tuple
# single_value_tuple = (42,)
# print(type(single_value_tuple))
# Output:
# <class 'tuple'>

# Without the comma, it's not a tuple
# not_a_tuple = (42)
# print(type(not_a_tuple))  # <class 'int'>
# Output:
# <class 'int'>

# 14.create empty set
# empty_set = set()
# Output:"

# 15.create a dictionery like {"a":10,"b":20} and print the value of "a" without using methods
# my_dict = {"a": 10, "b": 20}

# # Access the value associated with the key "a" without using methods
# value_of_a = my_dict["a"]

# print(value_of_a)
# Output:10

# 16.create a dictionery like {"a":10,"b":20} and change the value of "b" is 30 and print it without using methods
# my_dict = {"a": 10, "b": 20}

# # Change the value associated with the key "b" without using methods
# my_dict["b"] = 30

# # Print the updated dictionary
# print(my_dict)
# Output:{'a': 10, 'b': 30}


# 17.create a dictionary like {"a":10,"b":20} and insert the key value pair which the key is "c" and the value is 30 and print it
# my_dict = {"a": 10, "b": 20}

# # Insert a new key-value pair "c": 30 without using methods
# my_dict["c"] = 30

# # Print the updated dictionary
# print(my_dict)
# Output:{'a': 10, 'b': 20, 'c': 30}

# 18.create two sets like {1,2,3,4} and {3,4,5,6} and find the union without using union method
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# # Find the union of the two sets without using union method
# union_result = set1 | set2

# # Print the union
# print(union_result)
# Output:{1, 2, 3, 4, 5, 6}

# 19.create two sets like {1,2,3,4} and {3,4,5,6} and find the intersection without using intersection method
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# Find the intersection of the two sets without using intersection method
# intersection_result = set1 & set2

# # Print the intersection
# print(intersection_result)
# Output:{3, 4}

# 20.create two sets like {1,2,3,4} and {3,4,5,6} and find there difference without using difference method
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# # Find the difference of the two sets without using difference method
# difference_result = set1 - set2

# # Print the difference
# print(difference_result)
# Output:{1, 2}

# 21.create a set like {1,2,3,4} and remove 3
# my_set = {1, 2, 3, 4}

# # Remove the element 3 without using the remove method
# my_set = my_set - {3}

# # Print the updated set
# print(my_set)
# Output:{1, 2, 4}

# 21.create a set like {1,2,3,4} and remove 3 using discard method and undrstand what's the difference between remove and pop
# To remove an element from a set using the discard method and explain the difference between remove and discard, you can use the following example:

# my_set = {1, 2, 3, 4}

# # Remove the element 3 using the discard method
# my_set.discard(3)

# # Print the updated set
# print(my_set)
# Output:{1, 2, 4}

# The discard method removes the specified element from the set if it exists. If the element is not present in the set, discard does nothing and does not raise an error.

# Now, let's discuss the difference between remove and discard:

# remove: Removes the specified element from the set. If the element is not present, it raises a KeyError.
# discard: Removes the specified element from the set if it exists. If the element is not present, it does nothing and does not raise an error.
# In summary, the main difference is in how they handle the case when the element to be removed is not present in the set. remove raises an error,
# while discard does not.

# 22.create a set like {1,2,3,4} and remove 3 using discard method and undrstand what's the difference between remove and pop
# To remove an element from a set using the discard method, you can do the following:

# my_set = {1, 2, 3, 4}

# # Remove the element 3 using the discard method
# my_set.discard(3)

# # Print the updated set
# print(my_set)
# Output:{1, 2, 4}

# The discard method removes the specified element from the set if it is present. If the element is not present, it does nothing (no error is raised).
# Now, let's discuss the difference between the remove and discard methods:

# remove: Removes the specified element from the set. If the element is not present, it raises a KeyError. Use remove when you want to ensure that the element
# is in the set before removing it.

# discard: Removes the specified element from the set if it is present. If the element is not present, it does nothing and does not raise an error. 
# Use discard when you want to remove an element if it exists, but don't want to raise an error if it doesn't.

# In summary, remove raises an error if the element is not found, while discard does not raise an error in such cases.

# 23.create a string like "hello world" and count "o"

# my_string = "hello world"

# # Count the occurrences of "o" in the string
# count_of_o = my_string.count("o")

# # Print the count
# print(count_of_o)
# Output:2

# 24.create a string like "hello world" and find "z" or index "z" and understand difference between index and count

# To find the index of a character, such as "z," in the string "hello world," you can use the find method. If the character is not present, 
# the find method will return -1. 
# Here's an example:

# my_string = "hello world"

# # Find the index of "z" in the string
# index_of_z = my_string.find("z")

# # Print the index
# print(index_of_z)
# Output:-1

# In this example, since "z" is not present in the string, the find method returns -1.

# Now, let's discuss the difference between count and find:

# count: Counts the occurrences of a substring or character in the string. Returns the number of occurrences.
# find: Finds the first occurrence of a substring or character in the string. Returns the index of the first occurrence or -1 if not found.
# In summary, count provides the number of occurrences, while find provides the index of the first occurrence or -1 if not found.

# 25.create a list like ["p","y","t","h","o","n"] and print "python"

# my_list = ["p", "y", "t", "h", "o", "n"]

# # Print "python" using list indexing
# word_python = "".join(my_list)
# print(word_python)
# Output:python

# 26.create a string "python" and print ["p","y","t","h","o","n"]

# my_string = "python"

# # Initialize an empty list
# char_list = []

# # Use a while loop to iterate over each character in the string
# index = 0
# while index < len(my_string):
#     # Append each character to the list
#     char_list.append(my_string[index])
#     index += 1

# # Print the list
# print(char_list)

# Output:
# ['p', 'y', 't', 'h', 'o', 'n']

# 27.create a string like"     python" and print "python"

# my_string = "     python"

# # Remove leading spaces using strip method
# result_string = my_string.strip()

# # Print the result
# print(result_string)
# Output:python

# 28.create a list [1,2,3,4] and print it like [1,2,3,4,5]

# my_list = [1, 2, 3, 4]

# # Add 5 to the list using the append method
# my_list.append(5)

# # Print the updated list
# print(my_list)
# Output:[1, 2, 3, 4, 5]

# 29.create a list [1,2,3,4] and print [1,2,3,4,1,2,3,4] using extend function

# my_list = [1, 2, 3, 4]

# # Extend the list with its own elements
# my_list.extend(my_list)

# # Print the updated list
# print(my_list)
# Output:[1, 2, 3, 4, 1, 2, 3, 4]

# 30.create a list [1,2,3,4] and print [1,2,3,4,"p","y","t","h","o","n"] using extend function

# my_list = [1, 2, 3, 4]

# # Extend the list with the elements of the string "python"
# my_list.extend("python")

# # Print the updated list
# print(my_list)
# Output:[1, 2, 3, 4, 'p', 'y', 't', 'h', 'o', 'n']

# 31.create a list [1,2,3,4] and remove 2 using pop function

# my_list = [1, 2, 3, 4]

# # Remove the element "2" using the pop method with the value
# my_list.pop(my_list.index(2))

# # Print the updated list
# print(my_list)
# Output:[1, 3, 4]

# 32.create a list [1,2,3,4] and print [1,5,3,4] using insert function

# my_list = [1, 2, 3, 4]

# # Replace the element "2" with "5" using the insert method
# index_to_replace = my_list.index(2)
# my_list.insert(index_to_replace, 5)
# my_list.pop(index_to_replace + 1)

# # Print the updated list
# print(my_list)
# Output:[1, 5, 3, 4]

# 33.create a list [1,2,3,4] and print [1,5,3,4] using negative indexing in insert function

# my_list = [1, 2, 3, 4]

# # Replace the element at index -2 (second-to-last) with "5"
# my_list[-2] = 5

# # Print the updated list
# print(my_list)
# Output:[1, 2, 5, 4]

# 34.create a list [1,2,3,4] and print [4,3,2,1]

# my_list = [1, 2, 3, 4]

# # Reverse the list using the reverse method
# my_list.reverse()

# # Print the reversed list
# print(my_list)
# Output:[4, 3, 2, 1]

# 35.create a list [1,4,3,2] and print [1,2,3,4] using function
# my_list = [1, 4, 3, 2]

# # Sort the list using the sorted function
# sorted_list = sorted(my_list)

# # Print the sorted list
# print(sorted_list)
# Output:[1, 2, 3, 4]

# 36.create a dict {"a":10,"b":12,"c":14} and clear it{}
# my_dict = {"a": 10, "b": 12, "c": 14}

# # Clear the dictionary using the clear method
# my_dict.clear()

# # Print the empty dictionary
# print(my_dict)
# Output:{}

# 37.create a empty set{}

# my_set = set()

# # Print the empty set
# print(my_set)
# Output:set()

# 38.create empty dict{}

# my_dict = {}

# # Print the empty dictionary
# print(my_dict)

# Output:{}

# 39.create a dict{"a":10,"b":20,"c":30} and print {"b":20,"c":30}

# my_dict = {"a": 10, "b": 20, "c": 30}

# # Print a subset of the dictionary
# subset_dict = {"b": my_dict["b"], "c": my_dict["c"]}
# print(subset_dict)
# Output:{'b': 20, 'c': 30}

# 40.create a set {1,2,3,4} and remove 2
# my_set = {1, 2, 3, 4}

# # Remove element 2 from the set
# my_set.remove(2)

# # Print the modified set
# print(my_set)
# Output:{1, 3, 4}

# ------------------------------------------------------moderate question--------------------------------------------------------
# 1)create a string "hello" and print >> ll:2 times without using count method

# # Define the string
# my_string = "hello"

# # Specify the character to count
# char_to_count = 'l'

# # Initialize a counter
# count = 0

# # Iterate through the string and count occurrences of the specified character
# for char in my_string:
#     if char == char_to_count:
#         count += 1

# # Print the result
# print(f"The character '{char_to_count}' appears {count} times in the string.")
# Output:The character 'l' appears 2 times in the string.

# 2)create a string "hello" and sort it 

# # Define the string
# my_string = "hello"

# # Convert the string to a list of characters
# char_list = list(my_string)

# # Sort the list of characters
# char_list.sort()

# # Convert the sorted list back to a string
# sorted_string = ''.join(char_list)

# # Print the sorted string
# print(sorted_string)
# Output:ehllo

# 3)Take input string from user and find vowels

# # Get input string from the user
# user_input = input("Enter a string: ")

# # Define a function to find vowels
# def find_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     vowel_list = [char for char in input_string if char in vowels]
#     return vowel_list

# # Find and print vowels in the input string
# result = find_vowels(user_input)
# print("Vowels in the string:", result)
# Output:
# Enter a string: zaid
# Vowels in the string: ['a', 'i']

# 4) create a list [(1,2),{"A":10},"abc",[1,2,3,4]] and find the data type of each element 

# # Create the list
# my_list = [(1, 2), {"A": 10}, "abc", [1, 2, 3, 4]]

# # Iterate through the list and print the data type of each element
# for element in my_list:
#     print(f"Element: {element}, Type: {type(element)}")
# Output:
# Element: (1, 2), Type: <class 'tuple'>
# Element: {'A': 10}, Type: <class 'dict'>
# Element: abc, Type: <class 'str'>
# Element: [1, 2, 3, 4], Type: <class 'list'>

# 5) print A to Z in sequence like A B C D E........XYZ.

# # Iterate through the alphabet from 'A' to 'Z'
# for char in range(ord('A'), ord('Z') + 1):
#     print(chr(char), end=" ")
# Output:A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
    
# 6)print ten time "hii" 

# count = 0
# while count < 10:
#     print("hii")
#     count += 1
# Output:
# hii
# hii
# hii
# hii
# hii
# hii
# hii
# hii
# hii
# hii

# for i in range(1,11):
#     print("hii")
# Output:
# hii
# hii
# hii
# hii
# hii
# hii
# hii
# hii
# hii
# hii

# 7)print right angle triangle using while loop 

# rows = 5
# i = 1

# while i <= rows:
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i += 1
# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

# 8)print right angle triangle using for loop 

# rows = 5

# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# 9)take input from user and check its even or odd

# # Get input from the user
# number = int(input("Enter a number: "))

# # Check if the number is even or odd
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")
# Output:
# Enter a number: 26
# 26 is an even number.
# Output:
# Enter a number: 21
# 21 is an odd number.
    
# 10)take input from user and check the number is divisible by 5 or not

# Get input from the user
# number = int(input("Enter a number: "))

# # Check if the number is divisible by 5
# if number % 5 == 0:
#     print(f"{number} is divisible by 5.")
# else:
#     print(f"{number} is not divisible by 5.")
# Output:
# Enter a number: 25
# 25 is divisible by 5.
# Output:
# Enter a number: 24
# 24 is not divisible by 5.
    
# 11)write a program to check whether a person is eligible for voting or not(accept age from user)

# # Get age input from the user
# age = int(input("Enter your age: "))

# # Check eligibility for voting
# if age >= 18:
#     print("You are eligible to vote!")
# else:
#     print("Sorry, you are not eligible to vote.")
# Output:
# Enter your age: 18
# You are eligible to vote!
# Output:
# Enter your age: 17
# Sorry, you are not eligible to vote.
    
# 12)print 1 to 10 using for loop

# Using for loop to print numbers from 1 to 10
# for i in range(1, 11):
#     print(i)
#  Output:
# 1
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8 
# 9 
# 10
    
# 13)write a programme to check whether a number is divisible by 7 or not

# Get input from the user
# number = int(input("Enter a number: "))

# # Check if the number is divisible by 7
# if number % 7 == 0:
#     print(f"{number} is divisible by 7.")
# else:
#     print(f"{number} is not divisible by 7.")
# Output:
# Enter a number: 49
# 49 is divisible by 7.
# Output:
# Enter a number: 48
# 48 is not divisible by 7.
    
# 14)write a program to display "hello" if number entered by user is even , otherwise print "bye"

# # Get input from the user
# number = int(input("Enter a number: "))

# # Check if the number is even
# if number % 2 == 0:
#     print("hello")
# else:
#     print("bye")
# Output:
# Enter a number: 24
# hello
# Output:
# Enter a number: 23
# bye
    
# 15)take input from user and check its data type 

# # Get input from the user
# user_input = input("Enter something: ")

# # Check the data type
# data_type = type(user_input)

# # Display the data type
# print(f"The data type of '{user_input}' is {data_type}")
# Output:
# Enter something: zaid
# The data type of 'zaid' is <class 'str'>

# 16)create set like {1,2,3,4,5} and update it {1,2,3,4,5,6,7,8,9}

# # Create a set
# my_set = {1, 2, 3, 4, 5}

# # Display the original set
# print("Original Set:", my_set)

# # Update the set
# my_set.update({6, 7, 8, 9})

# # Display the updated set
# print("Updated Set:", my_set)
# Output:
# Original Set: {1, 2, 3, 4, 5}
# Updated Set: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 17)create a set like {1,2,3,4,5} and add the element like {1,2,3,4,5,6,7,8,9}

# # Create a set
# my_set = {1, 2, 3, 4, 5}

# # Display the original set
# print("Original Set:", my_set)

# # Add elements to the set
# my_set |= {6, 7, 8, 9}

# # Display the set after adding elements
# print("Updated Set:", my_set)
# Output:
# Original Set: {1, 2, 3, 4, 5}
# Updated Set: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 18)take string from user like "python" and print ["p","y","t","h","o","n"]

# # Take input from the user
# user_input = input("Enter a string: ")

# # Create a list of individual characters
# char_list = list(user_input)

# # Display the list
# print("List of characters:", char_list)
# Output:
# Enter a string: python
# List of characters: ['p', 'y', 't', 'h', 'o', 'n']   

# 19)take input from user in int data type without using int() function

# # Take input from the user
# user_input = input("Enter an integer: ")

# # Convert the input to an integer
# user_integer = int(user_input)

# # Display the integer
# print("Entered integer:", user_integer)
# Output:
# Enter an integer: 24
# Entered integer: 24

# 20)create a string like " 7 apple 8 mango 9 banana" and print the int values only which dynamic state

# # Given string
# input_string = "7 apple 8 mango 9 banana"

# # Split the string into words
# words = input_string.split()

# # Iterate through the words and print integers
# for word in words:
#     if word.isdigit():  # Check if the word is a digit
#         print(int(word))
# Output:
# 7
# 8
# 9
        
# 21)take input from user like 1234 and print the every second element 0 for eg:1020

# # Get input from the user
# user_input = input("Enter a number: ")

# # Initialize an empty string to store the result
# result = ""

# # Iterate through every second character and append it to the result with 0
# for i in range(len(user_input)):
#     if i % 2 == 1:
#         result += "0"
#     else:
#         result += user_input[i]

# # Print the result
# print(result)
# Output:
# Enter a number: 1234
# 1030

# 22)take gmail from user like "abc@gmail.com" and print its name only "abc"

# # Get input from the user
# gmail_address = input("Enter your Gmail address: ")

# # Extract the name part before '@'
# name = gmail_address.split('@')[0]

# # Print the name
# print(f"The name part of the Gmail address is: {name}")
#  Output:
# Enter your Gmail address: abc@gmail.com
# The name part of the Gmail address is: abc

# 23) Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
#     Unit                          Price  
#   First 100 units                 no charge
#   Next 100 units                 Rs 5 per unit
#   After 200 units                Rs 10 per unit
#   (For example if input unit is 350 than total bill amount is Rs2000)

# # Get input for the number of units
# units = int(input("Enter the number of units consumed: "))

# # Initialize variables
# total_price = 0

# # Determine the bill amount based on the criteria
# if units <= 100:
#     total_price = 0  # No charge for the first 100 units
# elif units <= 200:
#     total_price = (units - 100) * 5  # Rs 5 per unit for the next 100 units
# else:
#     total_price = 100 * 5 + (units - 200) * 10  # Rs 10 per unit after 200 units

# # Display the total bill amount
# print(f"The total electricity bill amount is: Rs {total_price}")
# Output:
# Enter the number of units consumed: 350
# The total electricity bill amount is: Rs 2000

# 24) Write a program to check whether the last digit of a number(entered by user ) is divisible by 3 or not.

# # Get input for the number
# number = int(input("Enter a number: "))

# # Extract the last digit
# last_digit = abs(number) % 10

# # Check if the last digit is divisible by 3
# if last_digit % 3 == 0:
#     print(f"The last digit ({last_digit}) is divisible by 3.")
# else:
#     print(f"The last digit ({last_digit}) is not divisible by 3.")
# Output:
# Enter a number: 23
# The last digit (3) is divisible by 3.
# Output:
# Enter a number: 24
# The last digit (4) is not divisible by 3.
    
# 25) Write a program to determine whether a number (accepted from the user) is divisible by 2 and 3 both.

# # Get input for the number
# number = int(input("Enter a number: "))

# # Check if the number is divisible by 2 and 3
# if number % 2 == 0 and number % 3 == 0:
#     print(f"{number} is divisible by both 2 and 3.")
# else:
#     print(f"{number} is not divisible by both 2 and 3.")
# Output:
# Enter a number: 6
# 6 is divisible by both 2 and 3.
# Output:
# Enter a number: 16
# 16 is not divisible by both 2 and 3.

# 26)Accept the age of 4 people and display the youngest one?

# # Get input for each person's age
# age1 = int(input("Enter the age of person 1: "))
# age2 = int(input("Enter the age of person 2: "))
# age3 = int(input("Enter the age of person 3: "))
# age4 = int(input("Enter the age of person 4: "))

# # Determine the youngest age using if, elif, and else statements
# if age1 <= age2 and age1 <= age3 and age1 <= age4:
#     youngest_age = age1
# elif age2 <= age1 and age2 <= age3 and age2 <= age4:
#     youngest_age = age2
# elif age3 <= age1 and age3 <= age2 and age3 <= age4:[]
#     youngest_age = age3
# else:
#     youngest_age = age4

# # Display the youngest age
# print(f"The youngest person is {youngest_age} years old.")
# Output:
# Enter the age of person 1: 20
# Enter the age of person 2: 21
# Enter the age of person 3: 22
# Enter the age of person 4: 23
# The youngest person is 20 years old.

# 27) Accept the age of 4 people and display the oldest one?

# # Get input for each person's age
# age1 = int(input("Enter the age of person 1: "))
# age2 = int(input("Enter the age of person 2: "))
# age3 = int(input("Enter the age of person 3: "))
# age4 = int(input("Enter the age of person 4: "))

# # Determine the oldest age using if, elif, and else statements
# if age1 >= age2 and age1 >= age3 and age1 >= age4:
#     oldest_age = age1
# elif age2 >= age1 and age2 >= age3 and age2 >= age4:
#     oldest_age = age2
# elif age3 >= age1 and age3 >= age2 and age3 >= age4:
#     oldest_age = age3
# else:
#     oldest_age = age4

# # Display the oldest age
# print(f"The oldest person is {oldest_age} years old.")
# Output:
# Enter the age of person 1: 20
# Enter the age of person 2: 21
# Enter the age of person 3: 22
# Enter the age of person 4: 23
# The oldest person is 23 years old.

# 28) Write a program to check whether an years is leap year or not

# # Get input for the year
# year = int(input("Enter a year: "))

# # Check if the year is a leap year
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
# Output:
# Enter a year: 2024
# 2024 is a leap year.
# Output:
# Enter a year: 2014
# 2014 is not a leap year.

# 29) Write a program to check whether an years is leap year or not without using (or) keyword

# # Get input for the year
# year = int(input("Enter a year: "))

# # Check if the year is a leap year
# if (year % 4 == 0 and year % 100 != 0):
#     print(f"{year} is a leap year.")
# elif(year % 400 == 0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")
# Output:
# Enter a year: 2024
# 2024 is a leap year
# Output:
# Enter a year: 2014
# 2014 is not a leap year.
    
# 30) Write a program to check whether an years is leap year or not , without using (and),(or) keywords

# # Get input for the year
# year = int(input("Enter a year: "))

# # Check if the year is a leap year
# if year % 4 == 0:
#     if year % 100 != 0:
#         print(f"{year} is a leap year.")
#     else:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.")
#         else:
#             print(f"{year} is not a leap year.")
# else:
#     print(f"{year} is not a leap year.")
# Output:
# Enter a year: 2024
# 2024 is a leap year.
# Output:
# Enter a year: 2014
# 2014 is not a leap year.

# 31)Write a program to check whether a number entered is three digit number or not. 

# # Get input from the user
# number = int(input("Enter a number: "))

# # Check if the number is three digits
# if 100 <= number <= 999:
#     print(f"{number} is a three-digit number.")
# else:
#     print(f"{number} is not a three-digit number.")
# Output:
# Enter a number: 111
# 111 is a three-digit number.
# Output:
# Enter a number: 99
# 99 is not a three-digit number.
    
# 32) Write a program to check whether a person is senior citizen or not.

# # Get age input from the user
# age = int(input("Enter your age: "))

# # Check if the person is a senior citizen
# if age >= 60:
#     print("You are a senior citizen.")
# else:
#     print("You are not a senior citizen yet.")
#  Output:
# Enter your age: 60
# You are a senior citizen.
#  Output:
# Enter your age: 59
# You are not a senior citizen yet.
    
# 33)write a program which will add(sum) all the elements of list

# # Define a list of numbers
# numbers = [5, 10, 15, 20, 25]

# # Initialize a variable to store the sum
# total_sum = 0

# # Iterate through each element in the list and add it to the sum
# for number in numbers:
#     total_sum += number

# # Print the total sum
# print("The sum of the elements is:", total_sum)
# Output: The sum of the elements is:75

# 34)write a program to print maximum number without using max function

# # Define a list of numbers
# numbers = [12, 45, 23, 67, 89, 34, 56]

# # Initialize a variable to store the maximum number
# max_number = numbers[0]  # Assuming the first element is the maximum initially

# # Iterate through each element in the list to find the maximum
# for number in numbers:
#     if number > max_number:
#         max_number = number

# # Print the maximum number
# print("The maximum number is:", max_number)
# Output: The maximum number is: 89

# 35)write a program to print minimum number without using min function 

# # Define a list of numbers
# numbers = [12, 45, 23, 67, 89, 34, 56]

# # Initialize a variable to store the minimum number
# min_number = numbers[0]  # Assuming the first element is the minimum initially

# # Iterate through each element in the list to find the minimum
# for number in numbers:
#     if number < min_number:
#         min_number = number

# # Print the minimum number
# print("The minimum number is:", min_number)
# Ouput: The minimum number is: 12

# 36)write a program to square all the all elements of list note[1,5,3,9],>>[1,25,9,81]

# # Define a list of numbers
# numbers = [1, 5, 3, 9]

# # Use list comprehension to square each element
# squared_numbers = [num ** 2 for num in numbers]

# # Print the squared list
# print("Original list:", numbers)
# print("Squared list:", squared_numbers)
# Output:
# Original list: [1, 5, 3, 9]
# Squared list: [1, 25, 9, 81]

# 37)write a program to print all the elements in list which are divisible by 3 

# # Define a list of numbers
# numbers = [12, 24, 9, 18, 7, 15, 30, 21]

# # Initialize an empty list to store numbers divisible by 3
# divisible_by_3 = []

# # Use a for loop to iterate through the list
# for num in numbers:
#     # Check if the number is divisible by 3
#     if num % 3 == 0:
#         divisible_by_3.append(num)

# # Print the list of numbers divisible by 3
# print(divisible_by_3)
# Output:[12, 24, 9, 18, 15, 30, 21]

# 38)write a program to print all the elements which are greater than 100

# # Define a list of numbers
# numbers = [12, 150, 9, 200, 7, 15, 30, 21]

# # Use a for loop to iterate through the list
# for num in numbers:
#     # Check if the number is greater than 100
#     if num > 100:
#         print(num)
# Output: 
# 150
# 200

# 39)write a program to find the total length of all string element in a list eg ["py","thon"],>>[2,4]

# # Define a list of strings
# strings_list = ["py", "thon", "hello", "world"]

# # Initialize an empty list to store lengths
# lengths = []

# # Iterate through each string and append its length to the list
# for s in strings_list:
#     lengths.append(len(s))

# # Print the resulting list of lengths
# print(lengths)
# Output:[2, 4, 5, 5]

# 40)write a program to print all elements in dictionary

# # Define a dictionary
# my_dict = {"a": 10, "b": 20, "c": 30, "d": 40}

# # Iterate through key-value pairs and print them
# for key, value in my_dict.items():
#     print(f"{key}: {value}")
# Output:
# a: 10
# b: 20
# c: 30
# d: 40

# Write a program to make a table of any number but take a number from user input

# # Take a number from the user input
# number = int(input("Enter a number: "))

# # Display the multiplication table for the entered number
# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")
# Output:
# Enter a number: 2
# 2 x 1 = 2 
# 2 x 2 = 4 
# 2 x 3 = 6 
# 2 x 4 = 8 
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

# ---------------------------------------------------high level question----------------------------------------------------------



# 1)take a list and sort it without using sort function

# # Bubble Sort function
# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         # Last i elements are already sorted, so we don't need to check them
#         for j in range(0, n-i-1):
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

# # Example usage
# my_list = [64, 34, 25, 12, 22, 11, 90]

# # Call the bubble_sort function
# bubble_sort(my_list)

# # Print the sorted list
# print("Sorted list:", my_list)
# Output:Sorted list: [11, 12, 22, 25, 34, 64, 90]

# 2)take a list and sort it in descending order without using sort function

# def bubble_sort_desc(arr):
#     n = len(arr)

#     while n > 0:
#         for i in range(n - 1):
#             if arr[i] < arr[i + 1]:
#                 # Swap if the element found is smaller than the next element
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
        
#         n -= 1

# # Example usage
# my_list = [64, 34, 25, 12, 22, 11, 90]

# # Call the bubble_sort_desc function
# bubble_sort_desc(my_list)

# # Print the sorted list in descending order
# print("Sorted list (Descending):", my_list)
# Output:Sorted list (Descending): [90, 64, 34, 25, 22, 12, 11]

# 3)take a list and find the highest element without using max function

# def find_highest_element(arr):
#     # Check if the list is not empty
#     if not arr:
#         return None  # Return None for an empty list

#     highest = arr[0]  # Assume the first element is the highest

#     # Iterate through the list using a for loop
#     for element in arr[1:]:
#         # Update the highest element if a greater one is found
#         if element > highest:
#             highest = element

#     return highest

# # Example usage
# my_list = [64, 34, 25, 12, 22, 11, 90]

# # Call the find_highest_element function
# highest_element = find_highest_element(my_list)

# # Print the highest element
# print("Highest element:", highest_element)
# Output:Highest element: 90

# 4)take a list and find the second highest element

# def find_second_highest(arr):
#     # Check if the list has at least two elements
#     if len(arr) < 2:
#         return None  # Return None if the list is too short

#     highest = max(arr[0], arr[1])  # Initialize highest and second highest
#     second_highest = min(arr[0], arr[1])

#     # Iterate through the list starting from the third element
#     for element in arr[2:]:
#         if element > highest:
#             second_highest = highest
#             highest = element
#         elif element > second_highest:
#             second_highest = element

#     return second_highest

# # Example usage
# my_list = [64, 34, 25, 12, 22, 11, 90]

# # Call the find_second_highest function
# second_highest_element = find_second_highest(my_list)

# # Print the second highest element
# print("Second highest element:", second_highest_element)
# Output:Second highest element: 64

# 5)take a list and find the lowest element with using min function

# def find_lowest(arr):
#     # Check if the list is not empty
#     if not arr:
#         return None  # Return None if the list is empty

#     lowest = min(arr)  # Use the min function to find the lowest element

#     return lowest

# # Example usage
# my_list = [64, 34, 25, 12, 22, 11, 90]

# # Call the find_lowest function
# lowest_element = find_lowest(my_list)

# # Print the lowest element
# print("Lowest element:", lowest_element)
# Output:Lowest element: 11

# 6)take a dictionary and print the highest key value pair 

# def find_highest_key_value_pair(dictionary):
#     # Check if the dictionary is not empty
#     if not dictionary:
#         return None  # Return None if the dictionary is empty

#     # Find the key with the highest value using max function
#     highest_key = max(dictionary, key=dictionary.get)
    
#     # Get the corresponding value
#     highest_value = dictionary[highest_key]

#     return highest_key, highest_value

# # Example usage
# my_dict = {'a': 10, 'b': 30, 'c': 15, 'd': 25}

# # Call the find_highest_key_value_pair function
# highest_pair = find_highest_key_value_pair(my_dict)

# # Print the highest key-value pair
# print("Highest key-value pair:", highest_pair)
# Output:Highest key-value pair: ('b', 30)

# 7)take a dictionary and print the lowest key value pair

# # Example dictionary
# my_dict = {'a': 10, 'b': 30, 'c': 15, 'd': 25}

# # Initialize variables to store the lowest key-value pair
# lowest_key = None
# lowest_value = float('inf')  # Set to positive infinity initially

# # Iterate through the dictionary to find the lowest value
# for key, value in my_dict.items():
#     if value < lowest_value:
#         lowest_key = key
#         lowest_value = value

# # Print the lowest key-value pair
# print("Lowest key-value pair:", {lowest_key: lowest_value})
# Output:Lowest key-value pair: {'a': 10}

# 8)create a list like [1,2,3,4] and print the elements without using loop

# my_list = [1, 2, 3, 4]

# # Concatenate elements into a string and print
# print(' '.join(map(str, my_list)))
# Output:1 2 3 4

# 9)create a string "ABCD" and convert into "abcd" without using lower and upper method

# uppercase_string = "ABCD"

# # Convert to lowercase without using lower()
# lowercase_string = ''.join(chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in uppercase_string)

# # Print the result
# print(lowercase_string)
# Output:abcd

# interview qs

# car->arc program

# original_string = "car"

# # Reverse the string to get "arc"
# reversed_string = original_string[1] + original_string[2] + original_string[0]

# # Print the result
# print(reversed_string)
# Output:arc


# silent->listen program
# original_string = "silent"

# # Reverse the string to get "listen"
# reversed_string = original_string[2] + original_string[1] + original_string[0]+ original_string[5]+original_string[3]+original_string[4]

# # Print the result
# print(reversed_string)
# Output:listen

# Function:->A function is a block of code or set of instruction which performs a specific task when we call it and it is also provide reusabilty of code.
# main feature hai function ka reusability

# Three types of function are:
# in-built function:->print(),id():->baney banaye function hote hai through python.
# user defined function:->joh user create karta hai:->with the help of def.
# anonymous function:->function jiska koi naam nahi ho,ek he expression de sakte hai bas,argument multiple de sakte hai,lamba used karke banate hai anonymous function.

# static function
# def add():
#     return 10+20  #return yeh value return karne ka kaam karega means 10+20=30 toh 30 return karega.
# print(add())
# Output:30
# val=add()
# print(val)
# Output:30

#  dynamic function
# def add(n1,n2):
#     return n1+n2

# val=add(10,20)
# print(val)
# # Output:30
# val2=add(23,46)
# print(val2)
# # Output:69
# val3=add(33,67)
# print(val3)
# # Output:100

# def add(n1,n2):
#     return n1-n2

# val=add(30,20)
# print(val)
# # Output:10
# val2=add(63,46)
# print(val2)
# # Output:17
# val3=add(83,67)
# print(val3)
# # Output:16

# def add(n1,n2):
#     return n1*n2

# val=add(30,20)
# print(val)
# # Output:600
# val2=add(63,46)
# print(val2)
# # Output:2898
# val3=add(83,67)
# print(val3)
# # Output:5561

# def checkPrime(n):
#     c=0
#     for i in range(2,n):
#         if(n%i==0):
#             c+=1
#             break
#     if(c==0):
#         return True
#     return False

# print(checkPrime(2))
# Output:True

# if checkPrime(24):
#     print("hello")
# else:
#     print("hi")
# Output:hi

# data=[23,45,66,54]

# def reverseList(l):
#     for i in range(0,len(l)//2):
#         start=i
#         end=len(l)-(i+1)
#         l[start],l[end]=l[end],l[start]

# def reverseList(l):
#     for i in range(0,len(l)//2):
#         start=i
#         end=len(l)-i-1
#         l[start],l[end]=l[end],l[start]

# reverseList(data)
# print(data)
# Output:[54, 66, 45, 23]


# value get karni hai toh return use karegai.
# value get nahi karni hai toh return use nahi karegai.
# return ke baad kuch bhi likho fark nahi padta hai.

# def show():
#     print("hello")

# show()
# Output:hello

# def show():
#     print("hello")

# print(show())
# Output:hello
#        None

# def show():
#     print("hello")
#     return "hello"
# show()

# def show():
#     print("hello")
#     return"hii"
#     print("bye")
# show()

# def show():
#     a=10
#     if(a>0):
#         return True
#     return False
# print(show())

# based on Function homework

# def show():
#     print("Hi")
#     return "Hi"
# show()
# Output:Hi

# def show():
#     print("Hi")
#     return "Hi"
# show()
# print(show())
# Output:
# Hi
# Hi
# Hi

# def show(self):
#     print(self)
# show(10)
# print(show(20))
# Output:
# 10
# 20
# None  

# def none():
#     print("Hi")
# none()
# Output:Hi

# def print():
#     return("Hi")
# print()
# Output:"

# def show(s):
#     print("Hi")
# a=show()
# a()
# Output:
# a=show()
#   ^^^^^^
# TypeError: show() missing 1 required positional argument: 's'

# def show(x,y=10):
#     print(x+y)
# show(10)
# print(show(20))
# Output:
# 20
# 30
# None

# def show(x=10,y):
#     print(x+y)
# show()
# Output:
# def show(x=10,y):
#               ^
# SyntaxError: non-default argument follows default argument

# def show(*a):
#     print(*a)
# show(10,20,30)
# Output:10 20 30

# def show(*kwargs):
#     print(kwargs)
# show(10,20,30,40)
# Output:(10, 20, 30, 40)

# def show(**args):
#     print(args)
# show(a=10,b=20,c=30)
# Output:{'a': 10, 'b': 20, 'c': 30}

# def show(**args):
#     print(args)
# show({"a":10,"b":20})
# Output:
# show({"a":10,"b":20})
# TypeError: show() takes 0 positional arguments but 1 was given


# argument topic
# paramter:means joh user pass karra hai
# argument:joh function banate waqt user set karta hai
# types of parameter or argument are:
# default argument
# required argument
# variable length argument
# keyword variable length argument

# default argument

# def sum(n1,n2=0):
#     return n1+n2

# print(sum(10))
# Output:10
# print(sum(10,20))
# Output:30

# def sum(n1=10,n2=0):
#     return n1+n2

# print(sum())
# Output:10
# print(sum(10,30))
# Output:40
# print(sum(10))
# Output:10

# def selfprint(val="",myend="\n"):
#     print(val,end=myend)

# selfprint("hello")
# # Output:hello
# selfprint("hi")
# # Output:hi
# selfprint("hey")
# # Output:hey

# selfprint("hello",myend="")
# selfprint("hi")
# # Output:hellohi
# selfprint("hey")
# # Output:hey

# def show(a,b,c=10):
#     return a+b+c
# print(show(10,2))
# Output:22

# def show(a,b,c=10,d): # default argument ke baad required argument nahi daal sakte hai
#     return a+b+c
# print(show(10,20,30))
# Output:
# def show(a,b,c=10,d):
#                   ^
# SyntaxError: non-default argument follows default argument

# required argument
# def sum(n1,n2):
#     return n1+n2

# print(sum(10,20))
# Output:30

# variable length argument(multiple argument le sakte hai ismey)(yeh * se hamesha start hota hai)(tuple mai output dega)(args)
# def show(*n):
#     print(n)

# show(10)
# show(10,20)
# show(10,20,30)

# Output:
# (10,)
# (10, 20)
# (10, 20, 30)

# n number of sum program
# def show(*n):
#     print(sum(n))

# show(10)
# show(10,20)
# show(10,20,30)

# Output:
# 10
# 30
# 60

# n number of sum program
# def show(*n):
#     # print(sum(n))
#     s=0
#     for i in n:
#         s+=i
#     print(s)

# show(10)
# show(10,20)
# show(10,20,30)

# Output:
# 10
# 30
# 60

# keyword variable length argument(multiple argument le sakte hai key aur value ke based pai)(yeh ** se hamesha start hota hai)(dictionary mai output dega)(kwargs)
# def show(**n):
#     print(n)
# show(a=10,b=20,c=30)
# Output:{'a': 10, 'b': 20, 'c': 30}

# generator:apne ko ek se zyaada value return karna hai toh generator used karte hai
# yield:yeh generator object banata hai,par iska koi structure nahi hota hai,display karna parta hai output using typecasting

# def calculate(n1,n2):
#     yield n1+n2
#     yield n1-n2
#     yield n1*n2
#     yield n1/n2
#     yield n1//n2
#     yield n1%n2
#     yield n1**n2

# print(list(calculate(3,2)))  #type casting kiye edhar
# Output:[5, 1, 6, 1.5, 1, 1, 9]

# anonymous function:function jiska koi naam nahi ho,ek he expression de sakte hai bas,argument multiple de sakte hai,lamba used karke banate hai anonymous function
# lambda:-> It is used to create anonymous function
# lambda arguments: expression
# Here:

# lambda is the keyword indicating the creation of a lambda function.
# arguments are the input parameters for the function.
# expression is a single expression that the lambda function evaluates and returns.

# Lambda functions are useful when you need a quick function for a short period and don't want to formally define a full
#  function using the def keyword. They are commonly used in places where a function is required as an argument to a higher-order function,
# like in functions such as map(), filter(), and sorted().

# sum=lambda a,b:a+b   #ek he expression de sakte hai bas
# print(sum(10,20))
# Output:30

# filter():iska return type iterable object hota hai,yeh used hota hai filter out karne ke liye
# (function,iterable object):->True rahega tabb naye collection mai add karega nahi toh false aane pai add nahi karega
# Certainly! In simple terms, filter() is a built-in function in Python that is used to filter elements from an iterable (like a list) based on a specified function 
# or condition. The function takes two arguments: the filtering function and the iterable. The filtering function is applied to each element of the iterable, 
# and only the elements for which the function returns True are included in the result.


# def checkeven(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# # ==============================================================================================================================   
#     return n%2==0

# data=[23,45,6,78,9]
# # even=list((filter(checkeven,data)))
# even=list(filter(lambda n:n%2==0,data))
# print(even)
# # Output:[6, 78]

# filter:yeh tumse function mai expect karta hai boolean values
# map:yeh ek ek value get karega aur pucchega ki mujhe karna kya hai(alternatives of for loops)

# map():
# Certainly! In simple terms, map() is a built-in function in Python that is used to apply a specific function to each element of an iterable (like a list) and 
# return an iterable of the results. The function takes two arguments: the mapping function and the iterable. The mapping function is applied to 
# each element of the iterable, and the results are collected in a new iterable.

# salaries=[23000,34000,50000,2100]
# def addBonus(amt):
#     return amt+100

# salaries_bonus=list(map(lambda amt:amt+100,salaries))
# print(salaries_bonus)
# Output:[23100, 34100, 50100, 2200]

# def addBonus(amt):
#     return amt + 100
# salaries = [23000, 34000, 50000,2100]
# salaries_bonus = list(map(addBonus, salaries))
# print(salaries_bonus)
# Output:[23100, 34100, 50100, 2200]

            
# reduce():single value deta hai
# Certainly! In simple terms, reduce() is a function provided by the functools module in Python. It is used to successively apply a binary function to the
# items of an iterable, reducing the iterable to a single accumulated result.


# from functools import reduce #yeh import karna parega reduce use karne ke liye

# salaries  =[23000,34000,50000,34000]
# s=reduce(lambda x,y:x+y,salaries)
# print(s)
# # Output:141000
# f=reduce(lambda x,y:x*y,salaries)
# print(f)
# Output:1329400000000000000

# list comprehension

# import time

# start_time=time.time()
# a=[]
# for i in range(1,1000000):
#     if i%2==0:
#         a.append(i)

# end_time=time.time()
# elapsed_time=end_time-start_time
# print(f"Execution:  {elapsed_time*1000} seconds")
# Output:Execution:  110.94117164611816 seconds
# print("===============================================================================")

# list comprehension:->It is a shortest way to create a new list
# yeh time kam leta hai compare to traditional loops
# Certainly! In simple terms, list comprehension is a concise and readable way to create lists in Python. It allows you to define a list by specifying its elements 
# using a single line of code. The syntax involves specifying an expression followed by one or more 'for' or 'if' clauses to filter or modify the elements.

# s=[i for i in range(1,101)]
# print(s)
# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
#   86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# start_time=time.time()
# s=[i for i in range(1,1000000)if i%2==0]
# end_time=time.time()
# elapsed_time=end_time-start_time
# print(f"Execution:  {elapsed_time*1000} seconds")
# Output:Execution:  94.0237045288086 seconds

# dictionary comprehension:->
# In simple terms, dictionary comprehension is a concise and readable way to create dictionaries in Python. Similar to list comprehension, 
# it allows you to define a dictionary by specifying key-value pairs using a single line of code. The syntax involves expressing both the keys and
# values using an expression, along with one or more 'for' or 'if' clauses to filter or modify the items.

# s=[23,45,34,67,8]
# d={}
# for i in s:
#     d[i]=i*i
# print(d)
# Output:{23: 529, 45: 2025, 34: 1156, 67: 4489, 8: 64}

# s=[23,45,34,67,8]
# d={i:i*i  for i in s}
# print(d)
# Output:{23: 529, 45: 2025, 34: 1156, 67: 4489, 8: 64}


# set comprehension:->
# Set comprehension is a concise way to create sets in Python based on a specific rule or condition. It follows a syntax similar to list comprehension but produces a 
# set as the final result. The basic structure is:

# {expression for item in iterable if condition}

# expression: The operation or value to include in the set.
# item: The variable representing each element in the iterable.
# iterable: The sequence of elements (e.g., a list, tuple, or string) to iterate over.
# condition: (Optional) An optional filtering condition to include only certain elements in the set.
# Here's a simple example:

# squared_numbers = {x**2 for x in range(1, 6)}
# print(squared_numbers)

# Output:{1, 4, 9, 16, 25}

# This creates a set squared_numbers containing the squares of numbers from 1 to 5. The set comprehension is a concise way to achieve the same result as using a 
# loop to build a set.

# interview question
# string = "Rohit Khandekar Zaid Ansari"
# Expected Output:R K Z A

# string="Rohit Khandekar Zaid Ansari"
# new_list= string[0]+" "+ string[6]+" "+ string[16]+" "+ string[21]
# print(new_list)
# Output:R K Z A

# =============================================================================================================
# string = "Rohit Khandekar Zaid Ansari"

# # Initialize an empty string to store the result
# result = ""

# # Iterate over each word in the string and append the first letter to the result
# for word in string.split():
#     result += word[0] + " "

# # Remove the trailing space
# result = result.rstrip()

# print(result)
# Output:R K Z A

# =================================================================================================
# string="Rohit Khandekar Zaid Ansari"
# for i in range (0,len(string)):
#     if i==" " or i==0:
#         print(string[i+0],string[i+6],string[i+16],string[i+21])
# Output:R K Z A

# write a program to check number is armstrong or not 

# # Input a number
# number = int(input("Enter a number to check if it's an Armstrong number: "))

# # Convert the number to a string to find its length
# num_str = str(number)
# num_digits = len(num_str)

# # Calculate the sum of each digit raised to the power of the number of digits
# total = sum(int(digit) ** num_digits for digit in num_str)

# # Check if the total is equal to the original number
# if total == number:
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")
# Output:
# Enter a number to check if it's an Armstrong number: 153
# 153 is an Armstrong number.
# Output:
# Enter a number to check if it's an Armstrong number: 224
# 224 is not an Armstrong number.

# write a program to check number is armstrong or not 
# n =int(input("Enter a number :"))

# # Initialize variables
# armstrong_sum = 0
# temp = n
# num_digits = len(str(n))

# # Calculate the sum of cubes of digits
# while temp > 0:
#     digit = temp % 10
#     armstrong_sum += digit ** num_digits
#     temp //= 10

# # Check if the number is an Armstrong number
# if n == armstrong_sum:
#     print(f"{n} is an Armstrong number.")
# else:
#     print(f"{n} is not an Armstrong number.")
# Output:
# Enter a number :153
# 153 is an Armstrong number.
# Output:
# Enter a number :224
# 224 is not an Armstrong number.

# a=[12,52,90,20,25,45] 
# reverse a number after that reverse number without using inbuilt function

# # Given list of numbers
# a = [12, 52, 90, 20, 25, 45]

# # Function to reverse a number
# def reverse_number(num):
#     reversed_num = 0
#     while num > 0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num = num // 10
#     return reversed_num

# # Reverse each number in the list
# reversed_numbers = [reverse_number(num) for num in a]

# # Reverse the order of numbers in the list
# reversed_numbers.reverse()

# # Print the result
# print("Original List:", a)
# print("Reversed List:", reversed_numbers)
# Output:
# Original List: [12, 52, 90, 20, 25, 45]
# Reversed List: [54, 52, 2, 9, 25, 21]

# write a program to print this pattern 
# * * * *
#  * * *
#   * *
#    *

# # Number of rows
# n = 4

# # Outer loop for each row
# for i in range(n):
#     # Inner loop for spaces
#    for j in range(i):
#        print(" ", end="")
#     # Inner loop for asterisks
#    for k in range(n - i):
#        print("* ", end="")
#     # Move to the next line after each row
#    print()
# Output:
# * * * * 
#  * * * 
#   * * 
#    * 

# a=[50,20,11,90,15,16,20]
# addition of even numbers of list 

# # Given list
# a = [50, 20, 11, 90, 15, 16, 20]

# # Initialize sum to 0
# even_sum = 0

# # Loop through each element in the list
# for num in a:
#     # Check if the number is even
#     if num % 2 == 0:
#         # Add the even number to the sum
#         even_sum += num

# # Print the sum of even numbers
# print("Sum of even numbers in the list:", even_sum)
# # Output:Sum of even numbers in the list: 196

# a=[5,7,9,8,15,20,61]
# find second highest number in list 

# #Given list
# a = [5, 7, 9, 8, 15, 20, 61]

# # Initialize variables to store the highest and second highest numbers
# highest = second_highest = float('-inf')

# # Loop through each element in the list
# for num in a:
#     # Check if the number is greater than the highest
#     if num > highest:
#         # Update both highest and second highest
#         second_highest = highest
#         highest = num
#     # Check if the number is greater than the second highest but not equal to the highest
#     elif num > second_highest and num != highest:
#         # Update only second highest
#         second_highest = num

# # Print the second highest number
# print("Second highest number in the list:", second_highest)
# Output:
# Second highest number in the list: 20

# recursive function:A function that call itself it is known as recursive function.

# def show():
#     print("hello")
#     show()
# show()
# Output:
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# Traceback (most recent call last):
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 7437, in <module>
#     show()
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 7436, in show
#     show()
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 7436, in show
#     show()
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 7436, in show
#     show()
#   [Previous line repeated 993 more times]
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 7435, in show
#     print("hello")
# RecursionError: maximum recursion depth exceeded while calling a Python object

# def show(i=0):
#     print(f"hello {i}")
#     show(i+1)
# show()
# Output:
# hello 0
# hello 1
# hello 2
# hello 3
# hello 4
# hello 5
# hello 6
# hello 7
# hello 8
# hello 9
# hello 10
# hello 11
# hello 12
# hello 13
# hello 14
# hello 15
# hello 16
# hello 17
# hello 18
# hello 19
# hello 20
# hello 21
# hello 22
# hello 23
# hello 24
# hello 25
# hello 26
# hello 27
# hello 28
# hello 29
# hello 30
# hello 31
# hello 32
# hello 33
# hello 34
# hello 35
# hello 36
# hello 37
# hello 38
# hello 39
# hello 40
# hello 41
# hello 42
# hello 43
# hello 44
# hello 45
# hello 46
# hello 47
# hello 48
# hello 49
# hello 50
# hello 51
# hello 52
# hello 53
# hello 54
# hello 55
# hello 56
# hello 57
# hello 58
# hello 59
# hello 60
# hello 61
# hello 62
# hello 63
# hello 64
# hello 65
# hello 66
# hello 67
# hello 68
# hello 69
# hello 70
# hello 71
# hello 72
# hello 73
# hello 74
# hello 75
# hello 76
# hello 77
# hello 78
# hello 79
# hello 80
# hello 81
# hello 82
# hello 83
# hello 84
# hello 85
# hello 86
# hello 87
# hello 88
# hello 89
# hello 90
# hello 91
# hello 92
# hello 93
# hello 94
# hello 95
# hello 96
# hello 97
# hello 98
# hello 99
# hello 100
# hello 101
# hello 102
# hello 103
# hello 104
# hello 105
# hello 106
# hello 107
# hello 108
# hello 109
# hello 110
# hello 111
# hello 112
# hello 113
# hello 114
# hello 115
# hello 116
# hello 117
# hello 118
# hello 119
# hello 120
# hello 121
# hello 122
# hello 123
# hello 124
# hello 125
# hello 126
# hello 127
# hello 128
# hello 129
# hello 130
# hello 131
# hello 132
# hello 133
# hello 134
# hello 135
# hello 136
# hello 137
# hello 138
# hello 139
# hello 140
# hello 141
# hello 142
# hello 143
# hello 144
# hello 145
# hello 146
# hello 147
# hello 148
# hello 149
# hello 150
# hello 151
# hello 152
# hello 153
# hello 154
# hello 155
# hello 156
# hello 157
# hello 158
# hello 159
# hello 160
# hello 161
# hello 162
# hello 163
# hello 164
# hello 165
# hello 166
# hello 167
# hello 168
# hello 169
# hello 170
# hello 171
# hello 172
# hello 173
# hello 174
# hello 175
# hello 176
# hello 177
# hello 178
# hello 179
# hello 180
# hello 181
# hello 182
# hello 183
# hello 184
# hello 185
# hello 186
# hello 187
# hello 188
# hello 189
# hello 190
# hello 191
# hello 192
# hello 193
# hello 194
# hello 195
# hello 196
# hello 197
# hello 198
# hello 199
# hello 200
# hello 201
# hello 202
# hello 203
# hello 204
# hello 205
# hello 206
# hello 207
# hello 208
# hello 209
# hello 210
# hello 211
# hello 212
# hello 213
# hello 214
# hello 215
# hello 216
# hello 217
# hello 218
# hello 219
# hello 220
# hello 221
# hello 222
# hello 223
# hello 224
# hello 225
# hello 226
# hello 227
# hello 228
# hello 229
# hello 230
# hello 231
# hello 232
# hello 233
# hello 234
# hello 235
# hello 236
# hello 237
# hello 238
# hello 239
# hello 240
# hello 241
# hello 242
# hello 243
# hello 244
# hello 245
# hello 246
# hello 247
# hello 248
# hello 249
# hello 250
# hello 251
# hello 252
# hello 253
# hello 254
# hello 255
# hello 256
# hello 257
# hello 258
# hello 259
# hello 260
# hello 261
# hello 262
# hello 263
# hello 264
# hello 265
# hello 266
# hello 267
# hello 268
# hello 269
# hello 270
# hello 271
# hello 272
# hello 273
# hello 274
# hello 275
# hello 276
# hello 277
# hello 278
# hello 279
# hello 280
# hello 281
# hello 282
# hello 283
# hello 284
# hello 285
# hello 286
# hello 287
# hello 288
# hello 289
# hello 290
# hello 291
# hello 292
# hello 293
# hello 294
# hello 295
# hello 296
# hello 297
# hello 298
# hello 299
# hello 300
# hello 301
# hello 302
# hello 303
# hello 304
# hello 305
# hello 306
# hello 307
# hello 308
# hello 309
# hello 310
# hello 311
# hello 312
# hello 313
# hello 314
# hello 315
# hello 316
# hello 317
# hello 318
# hello 319
# hello 320
# hello 321
# hello 322
# hello 323
# hello 324
# hello 325
# hello 326
# hello 327
# hello 328
# hello 329
# hello 330
# hello 331
# hello 332
# hello 333
# hello 334
# hello 335
# hello 336
# hello 337
# hello 338
# hello 339
# hello 340
# hello 341
# hello 342
# hello 343
# hello 344
# hello 345
# hello 346
# hello 347
# hello 348
# hello 349
# hello 350
# hello 351
# hello 352
# hello 353
# hello 354
# hello 355
# hello 356
# hello 357
# hello 358
# hello 359
# hello 360
# hello 361
# hello 362
# hello 363
# hello 364
# hello 365
# hello 366
# hello 367
# hello 368
# hello 369
# hello 370
# hello 371
# hello 372
# hello 373
# hello 374
# hello 375
# hello 376
# hello 377
# hello 378
# hello 379
# hello 380
# hello 381
# hello 382
# hello 383
# hello 384
# hello 385
# hello 386
# hello 387
# hello 388
# hello 389
# hello 390
# hello 391
# hello 392
# hello 393
# hello 394
# hello 395
# hello 396
# hello 397
# hello 398
# hello 399
# hello 400
# hello 401
# hello 402
# hello 403
# hello 404
# hello 405
# hello 406
# hello 407
# hello 408
# hello 409
# hello 410
# hello 411
# hello 412
# hello 413
# hello 414
# hello 415
# hello 416
# hello 417
# hello 418
# hello 419
# hello 420
# hello 421
# hello 422
# hello 423
# hello 424
# hello 425
# hello 426
# hello 427
# hello 428
# hello 429
# hello 430
# hello 431
# hello 432
# hello 433
# hello 434
# hello 435
# hello 436
# hello 437
# hello 438
# hello 439
# hello 440
# hello 441
# hello 442
# hello 443
# hello 444
# hello 445
# hello 446
# hello 447
# hello 448
# hello 449
# hello 450
# hello 451
# hello 452
# hello 453
# hello 454
# hello 455
# hello 456
# hello 457
# hello 458
# hello 459
# hello 460
# hello 461
# hello 462
# hello 463
# hello 464
# hello 465
# hello 466
# hello 467
# hello 468
# hello 469
# hello 470
# hello 471
# hello 472
# hello 473
# hello 474
# hello 475
# hello 476
# hello 477
# hello 478
# hello 479
# hello 480
# hello 481
# hello 482
# hello 483
# hello 484
# hello 485
# hello 486
# hello 487
# hello 488
# hello 489
# hello 490
# hello 491
# hello 492
# hello 493
# hello 494
# hello 495
# hello 496
# hello 497
# hello 498
# hello 499
# hello 500
# hello 501
# hello 502
# hello 503
# hello 504
# hello 505
# hello 506
# hello 507
# hello 508
# hello 509
# hello 510
# hello 511
# hello 512
# hello 513
# hello 514
# hello 515
# hello 516
# hello 517
# hello 518
# hello 519
# hello 520
# hello 521
# hello 522
# hello 523
# hello 524
# hello 525
# hello 526
# hello 527
# hello 528
# hello 529
# hello 530
# hello 531
# hello 532
# hello 533
# hello 534
# hello 535
# hello 536
# hello 537
# hello 538
# hello 539
# hello 540
# hello 541
# hello 542
# hello 543
# hello 544
# hello 545
# hello 546
# hello 547
# hello 548
# hello 549
# hello 550
# hello 551
# hello 552
# hello 553
# hello 554
# hello 555
# hello 556
# hello 557
# hello 558
# hello 559
# hello 560
# hello 561
# hello 562
# hello 563
# hello 564
# hello 565
# hello 566
# hello 567
# hello 568
# hello 569
# hello 570
# hello 571
# hello 572
# hello 573
# hello 574
# hello 575
# hello 576
# hello 577
# hello 578
# hello 579
# hello 580
# hello 581
# hello 582
# hello 583
# hello 584
# hello 585
# hello 586
# hello 587
# hello 588
# hello 589
# hello 590
# hello 591
# hello 592
# hello 593
# hello 594
# hello 595
# hello 596
# hello 597
# hello 598
# hello 599
# hello 600
# hello 601
# hello 602
# hello 603
# hello 604
# hello 605
# hello 606
# hello 607
# hello 608
# hello 609
# hello 610
# hello 611
# hello 612
# hello 613
# hello 614
# hello 615
# hello 616
# hello 617
# hello 618
# hello 619
# hello 620
# hello 621
# hello 622
# hello 623
# hello 624
# hello 625
# hello 626
# hello 627
# hello 628
# hello 629
# hello 630
# hello 631
# hello 632
# hello 633
# hello 634
# hello 635
# hello 636
# hello 637
# hello 638
# hello 639
# hello 640
# hello 641
# hello 642
# hello 643
# hello 644
# hello 645
# hello 646
# hello 647
# hello 648
# hello 649
# hello 650
# hello 651
# hello 652
# hello 653
# hello 654
# hello 655
# hello 656
# hello 657
# hello 658
# hello 659
# hello 660
# hello 661
# hello 662
# hello 663
# hello 664
# hello 665
# hello 666
# hello 667
# hello 668
# hello 669
# hello 670
# hello 671
# hello 672
# hello 673
# hello 674
# hello 675
# hello 676
# hello 677
# hello 678
# hello 679
# hello 680
# hello 681
# hello 682
# hello 683
# hello 684
# hello 685
# hello 686
# hello 687
# hello 688
# hello 689
# hello 690
# hello 691
# hello 692
# hello 693
# hello 694
# hello 695
# hello 696
# hello 697
# hello 698
# hello 699
# hello 700
# hello 701
# hello 702
# hello 703
# hello 704
# hello 705
# hello 706
# hello 707
# hello 708
# hello 709
# hello 710
# hello 711
# hello 712
# hello 713
# hello 714
# hello 715
# hello 716
# hello 717
# hello 718
# hello 719
# hello 720
# hello 721
# hello 722
# hello 723
# hello 724
# hello 725
# hello 726
# hello 727
# hello 728
# hello 729
# hello 730
# hello 731
# hello 732
# hello 733
# hello 734
# hello 735
# hello 736
# hello 737
# hello 738
# hello 739
# hello 740
# hello 741
# hello 742
# hello 743
# hello 744
# hello 745
# hello 746
# hello 747
# hello 748
# hello 749
# hello 750
# hello 751
# hello 752
# hello 753
# hello 754
# hello 755
# hello 756
# hello 757
# hello 758
# hello 759
# hello 760
# hello 761
# hello 762
# hello 763
# hello 764
# hello 765
# hello 766
# hello 767
# hello 768
# hello 769
# hello 770
# hello 771
# hello 772
# hello 773
# hello 774
# hello 775
# hello 776
# hello 777
# hello 778
# hello 779
# hello 780
# hello 781
# hello 782
# hello 783
# hello 784
# hello 785
# hello 786
# hello 787
# hello 788
# hello 789
# hello 790
# hello 791
# hello 792
# hello 793
# hello 794
# hello 795
# hello 796
# hello 797
# hello 798
# hello 799
# hello 800
# hello 801
# hello 802
# hello 803
# hello 804
# hello 805
# hello 806
# hello 807
# hello 808
# hello 809
# hello 810
# hello 811
# hello 812
# hello 813
# hello 814
# hello 815
# hello 816
# hello 817
# hello 818
# hello 819
# hello 820
# hello 821
# hello 822
# hello 823
# hello 824
# hello 825
# hello 826
# hello 827
# hello 828
# hello 829
# hello 830
# hello 831
# hello 832
# hello 833
# hello 834
# hello 835
# hello 836
# hello 837
# hello 838
# hello 839
# hello 840
# hello 841
# hello 842
# hello 843
# hello 844
# hello 845
# hello 846
# hello 847
# hello 848
# hello 849
# hello 850
# hello 851
# hello 852
# hello 853
# hello 854
# hello 855
# hello 856
# hello 857
# hello 858
# hello 859
# hello 860
# hello 861
# hello 862
# hello 863
# hello 864
# hello 865
# hello 866
# hello 867
# hello 868
# hello 869
# hello 870
# hello 871
# hello 872
# hello 873
# hello 874
# hello 875
# hello 876
# hello 877
# hello 878
# hello 879
# hello 880
# hello 881
# hello 882
# hello 883
# hello 884
# hello 885
# hello 886
# hello 887
# hello 888
# hello 889
# hello 890
# hello 891
# hello 892
# hello 893
# hello 894
# hello 895
# hello 896
# hello 897
# hello 898
# hello 899
# hello 900
# hello 901
# hello 902
# hello 903
# hello 904
# hello 905
# hello 906
# hello 907
# hello 908
# hello 909
# hello 910
# hello 911
# hello 912
# hello 913
# hello 914
# hello 915
# hello 916
# hello 917
# hello 918
# hello 919
# hello 920
# hello 921
# hello 922
# hello 923
# hello 924
# hello 925
# hello 926
# hello 927
# hello 928
# hello 929
# hello 930
# hello 931
# hello 932
# hello 933
# hello 934
# hello 935
# hello 936
# hello 937
# hello 938
# hello 939
# hello 940
# hello 941
# hello 942
# hello 943
# hello 944
# hello 945
# hello 946
# hello 947
# hello 948
# hello 949
# hello 950
# hello 951
# hello 952
# hello 953
# hello 954
# hello 955
# hello 956
# hello 957
# hello 958
# hello 959
# hello 960
# hello 961
# hello 962
# hello 963
# hello 964
# hello 965
# hello 966
# hello 967
# hello 968
# hello 969
# hello 970
# hello 971
# hello 972
# hello 973
# hello 974
# hello 975
# hello 976
# hello 977
# hello 978
# hello 979
# hello 980
# hello 981
# hello 982
# hello 983
# hello 984
# hello 985
# hello 986
# hello 987
# hello 988
# hello 989
# hello 990
# hello 991
# hello 992
# hello 993
# hello 994
# hello 995
# hello 996
# Traceback (most recent call last):
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 7521, in <module>
#     show()
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 7520, in show
#     show(i+1)
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 7520, in show
#     show(i+1)
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 7520, in show
#     show(i+1)
#   [Previous line repeated 993 more times]
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 7519, in show
#     print(f"hello {i}")
# RecursionError: maximum recursion depth exceeded while calling a Python object

# def show(i=0):
#     if(i<=10):
#         print(f"hello {i}")
#         show(i+1)
# show()
# Output:
# hello 0
# hello 1
# hello 2
# hello 3
# hello 4
# hello 5
# hello 6
# hello 7
# hello 8
# hello 9
# hello 10

# def show(i=1):
#     if(i<=10):
#         print(i)
#         show(i+1)
# show()
# Output:
# 1
# 2 
# 3 
# 4 
# 5 
# 6 
# 7 
# 8 
# 9 
# 10

# def show(i=1):
#     if(i<=10):
#         if(i%2==0):
#             print(i)
#         show(i+1)
# show()
# Output:
# 2
# 4
# 6
# 8
# 10

# def show(i=10):
#     if(i>=1):
#         print(i)
#         show(i-1)
# show()
# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# def show(i=1):
#     if(i<=10):
#         i%2==0  and print(i)
#         show(i+1)
# show()
# Output:
# 2
# 4
# 6
# 8
# 10

# Make function that take input integer number from user and make table of that integer value without using for loop and while loop

# def table(n,c=1):
#     if(c<=10):
#         print(n*c)
#         table(n,c+1)
# table(2)
# Output:
# 2
# 4 
# 6 
# 8 
# 10
# 12
# 14
# 16
# 18
# 20

# what is the difference between local variable and global variable?

# a variable which is created inside a function it is called as local variable.
# andarr ke area ko local scope kehte hai(local scope is the body of function).
# local scope mai variable joh banaye jaate hai usey kehte hai local variable.
# local scope means local area.

# a variable which is created outside a function it is called as global variable.
# global scope mai variable joh banaye jaate hai usey kehte hai global variable.
# global scope means global area. 

# a=10
# print(a)
# if(True):
#     a=20
#     print(a)
# print(a)
# Output:
# 10
# 20
# 20

# if(True):
#     a=20
#     print(a)
# print(a)
# Output:
# 20
# 20

# a=10
# print(a)
# def demo():
#     a=20
#     print(a)
# Output:10

# a=10
# print(a)
# def demo():
#     a=20
#     print(a)
# print(a)
# demo()
# print(a)
# Output:
# 10
# 10
# 20
# 10

# def demo():
#     a=20
#     print(a)
# demo()
# print(a)
# Output:
# 20
# Traceback (most recent call last):
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 8685, in <module>
#     print(a)
#           ^
# NameError: name 'a' is not defined

# Topic: Object Oriented Programming

# There are two types of programming patterns are :
# 1)OOP(Object Oriented Programming)
# 2)POP(Procedural Oriented Programming)

# python support both oop and pop
# c support pop but not oop
# java support oop but not pop
# javascript support  both oop and pop
# typescript support oop but not pop(typrescript is a superior version of javascript)

# Object Oriented Programming:It is working based on class and object.
# Procedural Oriented Programming:yeh function banana provide karta hai.

# class aur object ko samajhne ke liye building banane ka example liye hai jaise building banane se pehle apne ko pehle structure banana parta hai fir structure 
# follow karke building banate hai.
# Toh structure class hota hai means woh blueprint hota hai aur object blueprint ko follow karke banta hai means class ke structure ko follow karke banta hai.

# Class:It is a blueprint of an object and also it does not take any spaces.

# Object:It is an instance of a class and also it take spaces based on functionality and property(yeh class ko follow karke banta hai).
# Each object has state and behaviour occurs.
# state means variable and behaviour means method.

# A Function which is created inside a class it is known as method.
# Class ke andarr joh bhi method hai usme ek parameter pass karna parta hai means compulsory hota hai joh ki "self" parameter hai.
# Class ka name hamesha capital words se start hota hai.

# Human state
# class Human:
#     name="xyz"
#     color="white"
#     height=4.2
#     weight=23.6

# def walk(self):
#     return "walking"

# def speak(self):
#     return "speaking"

# def jump(self):
#     return "jumping"

# def intro(self):
#     return f"hello my name is {self.name}"

# Human Behaviour

# obj=Human()
# print(id(obj))
# print(obj.name)
# print(obj.intro())
# print(obj.jump())

# obj2=Human()
# print(id(obj2))
# print(obj2.name)
# print(obj2.intro())
# print(obj2.jump())

# Output:
# 2277092851856
# xyz
# Traceback (most recent call last):
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 8725, in <module>
#     print(obj.intro())
#           ^^^^^^^^^
# AttributeError: 'Human' object has no attribute 'intro'

# OOP:isme instance variable and local variable hote hai bas
# POP:isme local variable and global variable hote hai
# self:It is a paramter which refer current object
# instance variable:yeh state hai inside a class or outside a method joh ki object ke states hote hai inhe self se call kiya jaata hai
# (object ke states ko instance variable kehte hai).
# local varaible:A varaible which is created inside a method it is known as local variable.
# method:method created inside a class,method required one positional argument which is self,method ko call karne ke liye object banana parta hai.
# function:function created a outside a class,function does not required any parameter,function ko direct call kar sakte hai

# # Human state
# class Human:
#     name = "xyz"
#     color = "white"
#     height = 4.2
#     weight = 23.6

#     def walk(self):
#         return "walking"

#     def speak(self):
#         return "speaking"

#     def jump(self):
#         return "jumping"

#     def intro(self):
#         return f"hello my name is {self.name}"

# # Human Behaviour
# obj = Human()
# print(id(obj))
# print(obj.name)
# print(obj.intro())
# print(obj.jump())

# obj2 = Human()
# print(id(obj2))
# print(obj2.name)
# print(obj2.intro())
# print(obj2.jump())

# Output:
# 2407409552912
# xyz
# hello my name is xyz
# jumping
# 2407409552976
# xyz
# hello my name is xyz
# jumping

# Static value based class

# class User:
#     name="zaid"
#     city="Thane"
#     email="azaid@gmail.com"
#     password="1122"

#     def intro(self):
#         return f'hello my name is {self.name} i am from  {self.city}'
    
# obj=User()
# print(obj.name)
# print(obj.city)
# print(obj.email)
# print(obj.password)
# print(obj.intro())

# obj2=User()
# print(obj2.name)
# print(obj2.city)
# print(obj2.email)
# print(obj2.password)
# print(obj2.intro())

# Output:
# zaid
# Thane
# azaid@gmail.com
# 1122
# hello my name is zaid i am from  Thane
# zaid
# Thane
# azaid@gmail.com
# 1122
# hello my name is zaid i am from  Thane

# Dynamic value based class

# class User:
#     name=""
#     city=""
#     email=""
#     password=""

#     def intro(self):
#         return f' hello my name is {self.name} i am from {self.city}'
    
#     def setDetails(self,name,city,email,password):
#         self.name=name
#         self.city=city
#         self.email=email
#         self.password=password

# obj=User()
# obj.setDetails("Karan","Thane","karan@gmail.com","11ab")
# print(obj.name)
# print(obj.city)
# print(obj.email)
# print(obj.password)
# print(obj.intro())

# obj2=User()
# obj2.setDetails("zaid","mumbra","azaid@gmail.com","11abcb")
# print(obj2.name)
# print(obj2.city)
# print(obj2.email)
# print(obj2.password)
# print(obj2.intro())
# Output:
# Karan
# Thane
# karan@gmail.com
# 11ab
#  hello my name is Karan i am from Thane
# zaid
# mumbra
# azaid@gmail.com
# 11abcb
#  hello my name is zaid i am from mumbra

# Topic: constructor
# implicit means internally and explicit means externally.
# A constructor is used initiliaze the instance variable of a class.
# we does not need to call constructor explicitly.
# It is start with ___init___.
# It is implicitly call whenever we create an object.
# constructor ke through instance variable ko initialize karwa sakte hai class ke.
# method ko call karna parta hai but constructor ko call karne ki zaroorat nhi parti haiwoh automatically call hota hai.
# jab bhi humlog object create karte hai uss waqt constructor khud ba khud call hojata hai.
# object ko create karte waqt constructor call hota hai automatically.
# isme values daalna compulsory hai tabb he object banega nahi toh nahi banega. 
 
# method:iska naam kuch bhi ho sakta hai,multiple times call kar sakte hai method ko,isme kuch bhi operation perform kar sakte hai,isko empty rakh sakte hai means
#  bina values daaley.

# constructor:yeh init se start hoga,yeh ek time he create hoga harr ek object ke liye jab apon uss object ko create karte hai tabb,yeh specially instance variable ko 
# initialize karne ke kaam aata hai,isko empty nahi rakh sakte hai means values daalna he parta hai.

# class User:
#     name=""
#     city=""
#     email=""
#     password=""

#     def intro(self):
#         return f' hello my name is {self.name} i am from {self.city}'
    
#     def __init__(self,name,city,email,password):
#         self.name=name
#         self.city=city
#         self.email=email
#         self.password=password

# obj=User("Karan","Thane","karan@gmail.com","11ab")
# print(obj.name)
# print(obj.city)
# print(obj.email)
# print(obj.password)
# print(obj.intro())

# obj2=User("zaid","mumbra","azaid@gmail.com","11abcb")
# print(obj2.name)
# print(obj2.city)
# print(obj2.email)
# print(obj2.password)
# print(obj2.intro())
# Output:
# Karan
# Thane
# karan@gmail.com
# 11ab
#  hello my name is Karan i am from Thane
# zaid
# mumbra
# azaid@gmail.com
# 11abcb
#  hello my name is zaid i am from mumbra

# To count how much times object occurs inside a class

# class User:
#     name=""
#     city=""
#     email=""
#     password=""
#     objectcount=0

#     def intro(self):
#         return f' hello my name is {self.name} i am from {self.city}'
    
#    def __init__(self,name,city,email,password):
#        self.name=name
#        self.city=city
#        self.email=email
#        self.password=password
#        User.objectcount+=1   #edhar yeh isko as static variable treat karra hai because humlog ne object ko call kiya using class name that's why yeh isko as 
                              #a static variable treat karra hai aur agar humlog yeh object ko self ke saath call kiye hote toh instance variable jaisa treat karta 
                              #fir apne ko objectcount '2' ki jagah '1' milta because woh sirf initialize instance variable ko count karta jis wajah se '1' aata fir.
          
# obj=User("Karan","Thane","karan@gmail.com","11ab")
# print(obj.name)
# print(obj.city)
# print(obj.email)
# print(obj.password)
# print(obj.intro())

# obj2=User("zaid","mumbra","azaid@gmail.com","11abcb")
# print(obj2.name)
# print(obj2.city)
# print(obj2.email)
# print(obj2.password)
# print(obj2.intro())
# print(User.objectcount)

# Output:
# Karan
# Thane
# karan@gmail.com
# 11ab
#  hello my name is Karan i am from Thane
# zaid
# mumbra
# azaid@gmail.com
# 11abcb
#  hello my name is zaid i am from mumbra
# 2

# instance variable class ke andarr banana hai toh direct declare kardo variable name daalke aur agar constructor ke andarr banana hai instance variable toh self 
# ka use karna parega instance variable banane ke liye nahi toh nhi banega fir

# There are two types access specifiers are in python are :-
# 1)Public:by default apna variable public access specifier he rehta hai
# 2)Private:yeh start hota hai ____(underscore se ) aur yeh used hota hai variable ko secured rakhne ke liye
# private variable ko set karne ke liye setter ka use karte hai means kuch condition detai hai aur get karne ke liye getter ka use karte hai direct get ya set nahi kar
# sakte hai private variable ko

# class Human:
#     def __init__(self,name,email):
#         self.name=name
#         if("@" in email):
#             self._email = email
#         else:
#             self._email="not valid"    

#     def intro(self):
#         return f" hello my name is {self.name}  and my email id is {self._email}"
    
#     def setEmail(self,email):
#         if("@" in email):
#             self._email=email
#         else:
#             self._email="not valid"
    
#     def  getEmail(self):
#         return self._email
    
    
# obj=Human("karan","ka@gmail.com")
# obj.setEmail("kaa@gmail.com")
# print(obj.getEmail())
# print(obj.intro())

# obj2=Human("kunal","ku@gmail.com")
# print(obj2.intro())
# Output:
# kaa@gmail.com
#  hello my name is karan  and my email id is kaa@gmail.com 
#  hello my name is kunal  and my email id is ku@gmail.com  

# Create a class name it as Character, and use following methods and attribute.

# -> create a constructor which can initialise the name of character

# -> create a two private attributes name it as life and score -> set life = 3 and score = 0

# -> create a methods name it as kicked, punched, stabbed which does the following action

# when kicked is called, it should increment the score atrribute by 10

# - when punched is called, it should increment the score attribute by 5

# when stabbed is called, it should decrement the life attribute by 1

# -> create two more method name it as, displaylife and displayscore which does the follwoing action

# - when displaylife is called, it return current life attribute value

# - when displayscore is called, it return current score attribute value

# Perform the following operations with Character class

# -> create 1 object for Character class and initialise the name as Mario

# -> call the kicked method

# -> call the stabbed method

# -> call punched method

# -> call stabbed method

# class Character:
#     def  __init__(self,name):
#         self.name=name
#         self.__life=3
#         self.__score=0

#     def kick(self):
#         self.__score+=10

#     def punch(self):
#         self.__score+=5

#     def stabbed(self):
#         self.__life-=1
    
#     def  displaylife(self):
#         if(self.__life<1):
#             return "game over"
#         return self.__life
    
#     def displayscore(self):
#         return self.__score

#    def __str__(self):                                                       #__str__ return type hamesha string he hoga aur print(obj) karne pai yeh 
#        return f'name: {self.name} score: {self.__score} life: {self.__life}'#automatically call hoga isko alag se call nahi karna parta hai like a constructor
                                                                              #woh bhi object create hone pai apne aap call hojata hai automatically call hojata hai
                                                                              #alag se call nahi karna parta hai aur __str__ ka used esliye kiya jaata hai
                                                                              #taaki humko generator object ki value string mai mil sakai aur hum read kar sakai.
# obj=Character("mario")
# obj.kick()
# obj.stabbed()
# obj.punch()
# obj.stabbed()
# obj.stabbed()
# print(obj.displaylife())
# print(obj.displayscore())
# print(obj)
# Output:
# game over
# 15
# name: mario score: 15 life: 0

# obj=Character("mario")
# obj.kick()
# obj.stabbed()
# obj.punch()
# obj.stabbed()
# print(obj.displaylife())
# print(obj.displayscore())
# Output:
# 1
# 15

# four pillars of OOP are:-
# 1)encapsulation(security):-Data ko bind aur wrap karke rakhna single unit mai for security purpose,private access specifier ko support karta hai .
# 2)inheritance(data reusability):
# 3)polymorphism(data reusability):
# 4)abstraction(security):

# OOP Questions:
# 1)what is OOPS?

#Ans:In Python, Object-Oriented Programming (OOPS) is a way of writing code that revolves around the concept of "objects." Let's break it down:

# 1. **Object:** An object is like a self-contained package that combines data (attributes) and the functions (methods) that work with that data. 
# Think of an object as something that represents a specific thing or concept. For example, you can have an object representing a car with its properties (color, model) 
# and actions (drive, brake).

# 2. **Class:** A class is like a blueprint for creating objects. It defines what attributes and methods an object created from that class will have.
# Going back to the car example, a class would describe what a generic car is like, listing its possible features and behaviors.

# 3. **Attributes:** These are characteristics or properties of an object. For a car, attributes could include things like color, model, and speed.

# 4. **Methods:** These are functions that are associated with an object. They define what actions an object can perform. For a car, methods could be things like drive, 
# brake, and honk.

# Here's a simple example in Python:

# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def drive(self):
#         print(f"The {self.color} car is driving.")

# # Creating an object (instance) of the Car class
# my_car = Car(color="blue", model="sedan")

# # Accessing attributes
# print(f"My car is a {my_car.color} {my_car.model}.")

# # Calling a method
# my_car.drive()
# Output:
# My car is a blue sedan.
# The blue car is driving.

# In this example, `Car` is a class, and `my_car` is an object (instance) of that class. The object has attributes (color and model) and a method (drive). 
# OOPS in Python allows you to structure your code in a way that mimics real-world objects and their interactions.

# 2)what is an object oriented programming?

#Ans:In Python, Object-Oriented Programming (OOPS) is a way of writing code that revolves around the concept of "objects." Let's break it down:

# 1. **Object:** An object is like a self-contained package that combines data (attributes) and the functions (methods) that work with that data. 
# Think of an object as something that represents a specific thing or concept. For example, you can have an object representing a car with its properties (color, model) 
# and actions (drive, brake).

# 2. **Class:** A class is like a blueprint for creating objects. It defines what attributes and methods an object created from that class will have.
# Going back to the car example, a class would describe what a generic car is like, listing its possible features and behaviors.

# 3. **Attributes:** These are characteristics or properties of an object. For a car, attributes could include things like color, model, and speed.

# 4. **Methods:** These are functions that are associated with an object. They define what actions an object can perform. For a car, methods could be things like drive, 
# brake, and honk.

# Here's a simple example in Python:

# class Car:
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     def drive(self):
#         print(f"The {self.color} car is driving.")

# # Creating an object (instance) of the Car class
# my_car = Car(color="blue", model="sedan")

# # Accessing attributes
# print(f"My car is a {my_car.color} {my_car.model}.")

# # Calling a method
# my_car.drive()
# Output:
# My car is a blue sedan.
# The blue car is driving.

# In this example, `Car` is a class, and `my_car` is an object (instance) of that class. The object has attributes (color and model) and a method (drive). 
# OOPS in Python allows you to structure your code in a way that mimics real-world objects and their interactions.

# 3)what is class?

#Ans:In Python, a class is like a blueprint or template that defines the structure and behavior of objects. Think of a class as a way to create objects with specific 
# attributes and methods. 

# Here's a breakdown in simple English:

# 1. **Blueprint or Template:** A class is a way to define what an object will look like and what it can do. It's like a plan for creating objects.

# 2. **Attributes:** These are characteristics or properties that describe an object. For example, if you have a class representing a car, attributes could include color,
# model, and speed.

# 3. **Methods:** These are functions that are associated with a class. They define what actions or behaviors an object created from the class can perform. 
# In the car example, methods could be things like drive, brake, and honk.

# 4. **Object:** An object is an instance of a class. It's a specific realization or implementation of the class blueprint. If the class is like a recipe, 
# an object is the actual dish you cook using that recipe.

# Here's a simple example in Python:

# # Define a class named 'Car'
# class Car:
#     # The __init__ method is a special method called a constructor.
#     # It initializes the object with specified attributes.
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model

#     # Method to drive the car
#     def drive(self):
#         print(f"The {self.color} car is driving.")

# # Create an object (instance) of the 'Car' class
# my_car = Car(color="blue", model="sedan")

# # Access attributes
# print(f"My car is a {my_car.color} {my_car.model}.")

# # Call a method
# my_car.drive()
# Output:
# My car is a blue sedan.
# The blue car is driving.

# In this example, `Car` is a class that defines what a car is. `my_car` is an object (instance) of that class with specific attributes (color and model) and 
# a method (drive). Classes help organize code and structure it in a way that represents real-world entities.

# 4)give real world example of a class?

#Ans: Sure, let's take a real-world example, say, a `Dog` class in Python.

# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#         self.energy = 100  # A default energy level when a dog is created

#     def bark(self):
#         print(f"{self.name} says Woof! Woof!")

#     def play(self):
#         if self.energy >= 20:
#             print(f"{self.name} is playing fetch.")
#             self.energy -= 20
#         else:
#             print(f"{self.name} is too tired to play.")

#     def sleep(self):
#         print(f"{self.name} is taking a nap.")
#         self.energy += 30

# # Creating instances (objects) of the Dog class
# dog1 = Dog(name="Buddy", breed="Golden Retriever", age=3)
# dog2 = Dog(name="Max", breed="Poodle", age=2)

# # Accessing attributes and calling methods
# print(f"{dog1.name} is a {dog1.age}-year-old {dog1.breed}.")
# dog1.bark()
# dog1.play()
# dog1.sleep()

# print(f"{dog2.name} is a {dog2.age}-year-old {dog2.breed}.")
# dog2.bark()
# dog2.play()
# Output:
# Buddy is a 3-year-old Golden Retriever.
# Buddy says Woof! Woof!
# Buddy is playing fetch.
# Buddy is taking a nap.
# Max is a 2-year-old Poodle.
# Max says Woof! Woof!
# Max is playing fetch.

# In this example:

# - `Dog` is a class representing the concept of a dog.
# - Instances of this class, like `dog1` and `dog2`, represent specific dogs with individual attributes (name, breed, age) and behaviors (bark, play, sleep).
# - The methods (`bark`, `play`, `sleep`) define actions that a dog can perform.
# - Attributes (`name`, `breed`, `age`, `energy`) store information about each dog.

# This `Dog` class helps model and organize the code in a way that mirrors real-world entities and their interactions. Each dog created from this class has its own 
# set of attributes and can perform actions based on the defined methods.

# Ans: Sure, let's delve into a real-world example with some theoretical explanations.

# **Real-world Example: Car Class**

# In the world of programming, a class is like a blueprint or a template that defines the properties and behaviors common to a group of objects. 
# Objects are instances created from a class and represent tangible entities with specific characteristics and actions.

# **Class Theory:**

# In Python, a class is a code structure that encapsulates data and functions related to a specific concept. Let's consider a simple example of a `Car` class:

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.speed = 0  # Default speed when a car is created

#     def accelerate(self):
#         self.speed += 10
#         print(f"The {self.year} {self.make} {self.model} is accelerating. Current speed: {self.speed} mph")

#     def brake(self):
#         if self.speed >= 10:
#             self.speed -= 10
#             print(f"The {self.year} {self.make} {self.model} is braking. Current speed: {self.speed} mph")
#         else:
#             print(f"The {self.year} {self.make} {self.model} has already stopped.")

# # Creating instances (objects) of the Car class
# car1 = Car(make="Toyota", model="Camry", year=2022)
# car2 = Car(make="Ford", model="Mustang", year=2021)

# # Accessing attributes and calling methods
# print(f"Details of {car1.year} {car1.make} {car1.model}")
# car1.accelerate()
# car1.brake()

# print(f"\nDetails of {car2.year} {car2.make} {car2.model}")
# car2.accelerate()
# car2.brake()
# Output:
# Details of 2022 Toyota Camry
# The 2022 Toyota Camry is accelerating. Current speed: 10 mph
# The 2022 Toyota Camry is braking. Current speed: 0 mph      

# Details of 2021 Ford Mustang
# The 2021 Ford Mustang is accelerating. Current speed: 10 mph
# The 2021 Ford Mustang is braking. Current speed: 0 mph   

# **Explanation:**

# - **Class (`Car`):** The class defines the blueprint for a car, including attributes (`make`, `model`, `year`, `speed`) and methods (`accelerate`, `brake`).
  
# - **Object Instances (`car1`, `car2`):** Objects created from the `Car` class represent specific cars with individual characteristics.

# - **Attributes (`make`, `model`, `year`, `speed`):** These store information about each car instance.

# - **Methods (`accelerate`, `brake`):** These define actions that a car can perform.

# This `Car` class helps organize code, making it more modular and understandable. Each car instance has its own set of attributes and can perform actions based on the 
# defined methods. The class provides a clean and efficient way to model and manipulate car-related data in a Python program.

# 5)what is an object?

# Ans:In Python, an object is a concrete instance of a class. A class, as mentioned earlier, is like a blueprint or a template that defines the properties and behaviors 
# common to a group of objects. Objects are created based on these classes and represent specific instances with distinct characteristics and actions.

# **Simple Explanation:**

# - **Class:** Think of a class as a blueprint for creating things. For example, the class "Car" could describe how to make cars, with features like make, model, 
# and actions like accelerating and braking.

# - **Object:** An object is like an actual, tangible car created using that blueprint. If you have a class "Car," an object could be a specific Toyota Camry with a 
# particular make, model, and its own speed.

# **Example:**

# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

# # Creating objects (instances) of the Car class
# my_car = Car(make="Toyota", model="Camry")
# your_car = Car(make="Ford", model="Mustang")

# In this example, `my_car` and `your_car` are objects of the `Car` class. They have distinct properties (make and model) but follow the blueprint defined by the class. 
# Objects allow us to work with specific instances and perform actions or access information related to those instances.

# 6)give real world example of an object?

# Ans:Certainly! Let's consider a real-world example to understand objects and classes in Python: a `Dog` class.

# **Class:**
# A class is like a blueprint that defines the properties and behaviors shared by a group of objects. In our example, the `Dog` class is the blueprint for creating 
# different dogs.

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         return "Woof!"

#     def fetch(self):
#         return f"{self.name} is fetching the ball."

# **Object:**
# An object is an instance of a class, representing a specific entity. Using the `Dog` class, we can create individual dogs with unique names, breeds, and behaviors.

# # Creating objects (instances) of the Dog class
# my_dog = Dog(name="Buddy", breed="Golden Retriever")
# your_dog = Dog(name="Max", breed="Labrador")

# Now, `my_dog` and `your_dog` are objects of the `Dog` class. They each have their own distinct properties (name, breed) and can perform actions defined by the class 
# methods.

# **Using Objects:**
# # Accessing properties
# print(f"My dog's name is {my_dog.name}.")
# print(f"Your dog is a {your_dog.breed}.")

# # Performing actions
# print(my_dog.bark())   # Output: Woof!
# print(your_dog.fetch())  # Output: Max is fetching the ball.

# Output:
# My dog's name is Buddy.
# Your dog is a Labrador.
# Woof!
# Max is fetching the ball.

# In this example, `my_dog` and `your_dog` are individual objects created from the common blueprint provided by the `Dog` class. Each object has its own unique state 
# (properties) and behavior (methods). This concept of classes and objects is fundamental to Object-Oriented Programming (OOP) and is widely used in Python and other
# programming languages.

# 7)what is the difference between class and object?

# Ans:In simple terms:

# **Class:**
# - A class is like a blueprint or a template that defines the properties and behaviors shared by a group of objects.
# - It encapsulates the common attributes and methods that the objects of that class will have.
# - It acts as a design or structure for creating objects.

# **Object:**
# - An object is an instance of a class, representing a specific entity or thing.
# - It is created based on the blueprint provided by the class.
# - Objects have their own unique characteristics (attributes) and can perform actions (methods) defined by the class.

# **Difference:**
# - **Class is a Blueprint:** Think of a class as a blueprint that describes how something should be created. It defines the common properties and behaviors that objects
# of that class will have.
# - **Object is an Instance:** An object is a specific instance created from that blueprint. It represents an actual occurrence or realization of the class, with its
# unique characteristics and actions.

# **Example:**
# - **Class (Blueprint):** If a class is like a blueprint for a car, specifying common features like color, model, and functions like driving and honking.
# - **Object (Instance):** An object of that class would be a specific car, such as a red Toyota Prius, with its unique color, model, and the ability to drive and honk.

# In Python, you use a class to define a blueprint, and then you create objects based on that class to work with specific instances of the described entity.

# 8)what are the four pillars of object oriented programming?

# Ans:The four pillars of Object-Oriented Programming (OOP) are:

# 1. **Encapsulation:**
#    - **Simple Explanation:** Wrapping data (attributes) and the methods (functions) that operate on the data into a single unit, known as a class.
#    - **Example:** Imagine a class representing a car. Encapsulation allows you to keep the car's details (like model, color) and actions (like starting, stopping) 
# together in one unit.

# 2. **Abstraction:**
#    - **Simple Explanation:** Hiding the complex implementation details and showing only the essential features of an object.
#    - **Example:** When you drive a car, you don't need to know how the engine works internally. Abstraction allows you to interact with the car using a simplified
# interface (steering wheel, pedals).

# 3. **Inheritance:**
#    - **Simple Explanation:** Creating a new class that inherits properties and behaviors from an existing class, forming a parent-child relationship.
#    - **Example:** If you have a general class representing animals, you can create a more specific class for dogs that inherits attributes and methods from the general 
# animal class.

# 4. **Polymorphism:**
#    - **Simple Explanation:** The ability of different classes to be used interchangeably based on a common interface. It allows a single interface to represent 
# different types.
#    - **Example:** If both a car and a bicycle have a `start` method, polymorphism allows you to call the `start` method on any vehicle object (car or bicycle) without
# worrying about its specific type.

# These pillars provide a foundation for designing and organizing code in a way that promotes modularity, reusability, and flexibility in programming.
   
# 9)what is encapsulation?

# Ans:**Encapsulation in Python - Simple Explanation:**

# **Encapsulation** is like putting your code in a protective bubble. It involves wrapping the data (attributes) and the methods (functions) that operate on the data 
# into a single unit, known as a **class**.

# Imagine a class as a blueprint for creating objects. This blueprint not only defines what kind of data an object can hold (attributes) but also what actions the object
# can perform (methods).

# Here's a breakdown:

# 1. **Attributes (Data):** These are the characteristics or properties of an object. For example, if you have a class representing a car, the attributes could include 
# the car's model, color, and year.

# 2. **Methods (Functions):** These are the actions that an object can perform. Sticking with the car example, methods could include starting the engine, stopping, or
# honking the horn.

# Now, encapsulation ensures that these attributes and methods are bundled together within a class. The outside world interacts with the class through a well-defined
# interface, and the internal details are hidden from the outside.

# **Why is this important?**
# - **Security:** Encapsulation protects the internal details of an object, preventing unintended interference from the outside.
# - **Modularity:** It organizes code in a way that makes it easier to manage, understand, and update.
# - **Reusability:** Classes with encapsulated features can be reused in different parts of a program or in different programs altogether.

# In simpler terms, encapsulation is like packaging your code neatly, making it easy to use and understand while keeping the internal complexities hidden.

# 10)what is inheritance?

# Ans:**Inheritance in Python - Simple Explanation:**

# **Inheritance** is like inheriting traits from your parents. In the world of programming, it allows a new class (called the **child class**) to inherit attributes and
# methods from an existing class (called the **parent class**).

# Here's a simple breakdown:

# 1. **Parent Class (Base Class):** This is the class that already exists, containing attributes and methods. Think of it as the "parent" passing on its traits.

# 2. **Child Class (Derived Class):** This is the new class that is created based on the existing class. It inherits attributes and methods from the parent class.

# **Why is this useful?**
# - **Code Reusability:** Instead of writing the same code again, you can reuse the code from the parent class in the child class. This saves time and promotes a cleaner
# code structure.

# - **Modularity:** Inheritance allows you to create a hierarchy of classes. The parent class can be a general, abstract representation, and child classes can provide 
# more specific details.

# **Example:**

# Let's say you have a class called `Animal` with attributes and methods common to all animals. You can then create a `Dog` class that inherits from `Animal`. The `Dog` 
# class automatically has all the attributes and methods of the `Animal` class, and you can add or modify specific details for dogs.

# In summary, inheritance is like passing down characteristics from a parent to a child, creating a relationship between classes that promotes code reuse and 
# organization.

# 11)what is polymorphism?

# Ans:**Polymorphism in Python - Simple Explanation:**

# **Polymorphism** is like a shape-shifter. In programming, it allows objects to take on different forms or behaviors based on the context.

# Here's a simple breakdown:

# 1. **Many Forms:** "Poly" means many, and "morph" means forms. In programming, polymorphism allows objects to be used in various ways or to have different behaviors.

# 2. **Same Method, Different Implementation:** Polymorphism is often achieved through methods with the same name in different classes. These methods may have different 
# implementations but are called the same way.

# **Types of Polymorphism:**

# - **Compile-Time (Static) Polymorphism:** This is also known as method overloading. It occurs at compile-time, and the correct method is chosen based on the number or 
# type of arguments.

# - **Run-Time (Dynamic) Polymorphism:** This is also known as method overriding. It occurs at run-time, and the correct method is chosen based on the object's type.

# **Why is this useful?**

# - **Flexibility:** Polymorphism allows you to write more flexible and adaptable code. Objects can take on different roles or behaviors in different situations.

# **Example:**

# Consider a method called `area()` in both a `Circle` class and a `Square` class. Despite having the same method name, each class calculates the area differently. 
# Through polymorphism, you can use the `area()` method on both a `Circle` object and a `Square` object, and each will perform its unique calculation.

# In summary, polymorphism allows objects to exhibit different behaviors or take on different forms based on the context, providing flexibility and adaptability in 
# programming.

# 12)what is abstraction?

# Ans:**Abstraction in Python - Simple Explanation:**

# **Abstraction** in programming is like using a TV remote without knowing the internal circuitry. It allows you to focus on the essential features while hiding the 
# complex details.

# Here's a straightforward breakdown:

# 1. **Hiding Complexity:** Abstraction involves hiding the complex implementation details and showing only the necessary features.

# 2. **Focus on What, Not How:** It allows you to focus on what an object does rather than how it achieves its functionality.

# **Example:**

# Imagine a car. As a driver, you don't need to understand the intricate details of how the engine works. You interact with the car through a simplified interface - 
# the steering wheel, pedals, and dashboard. This abstraction allows you to drive the car without dealing with the complexities under the hood.

# **In Programming:**

# - **Class Interface:** In Python, abstraction is often achieved through classes. You define a class with methods (functions) that represent the essential behaviors of 
# an object. Users of the class interact with these methods without needing to know the internal workings.

# - **Hide Implementation Details:** For instance, if you have a `Car` class, you might have methods like `start_engine()` and `drive()`. Users of the `Car` class don't 
# need to know how these methods achieve their functionality; they only need to know what these methods do.

# **Why is this useful?**

# - **Simplicity:** Abstraction simplifies the interaction with complex systems by providing a clear and simplified interface.

# - **Modularity:** It allows you to break down a system into manageable parts, each with its abstraction, promoting modularity in your code.

# In summary, abstraction allows you to focus on what an object does without getting bogged down by the intricate details of how it achieves its functionality, 
# promoting simplicity and modularity in programming.

# 13)what is method?

# Ans:**Method in Python - Simple Explanation:**

# In Python, a **method** is a function that is associated with an object. It defines the behavior or actions that the object can perform. Think of a method as a set of 
# instructions that tell an object how to do something.

# Here's a straightforward breakdown:

# 1. **Function Associated with an Object:** A method is essentially a function, but it's associated with an object. It operates on the data within the object and can 
# modify the object's state.

# 2. **Defines Object Behavior:** Methods define what actions or behaviors an object can exhibit. For example, a `Car` object might have methods like `start_engine()` 
# and `drive()`, defining how the car can start its engine and move.

# **Example:**

# class Car:
#     def start_engine(self):
#         print("Engine started!")

#     def drive(self):
#         print("Car is moving.")

# # Creating an instance of the Car class
# my_car = Car()

# # Calling methods on the Car object
# my_car.start_engine()  # Output: Engine started!
# my_car.drive()         # Output: Car is moving.

# Output:
# Engine started!
# Car is moving.

# In this example, `start_engine()` and `drive()` are methods of the `Car` class. They define the actions a `Car` object can take.

# **Why are Methods Useful?**

# - **Encapsulation:** Methods encapsulate functionality within an object, promoting the concept of bundling data and methods that operate on that data.

# - **Object Interaction:** Methods allow objects to interact with and modify their own data. They define the interface through which the outside world can interact with 
# an object.

# - **Code Reusability:** Methods can be reused across multiple instances of an object. For example, all `Car` objects can use the same `start_engine()` method.

# In summary, a method in Python is a function associated with an object, defining the actions or behaviors that the object can perform. It encapsulates functionality, 
# promotes object interaction, and enhances code reusability.

# 14)what is the difference between class and method?

# Ans:**Class vs. Method in Python - Simple Explanation:**

# **Class:**
# - A **class** in Python is like a blueprint or a template for creating objects.
# - It defines a set of attributes (characteristics) and methods (behaviors) that objects created from the class will have.
# - Think of a class as a general category or type of thing.

# **Method:**
# - A **method** is a function that is associated with an object created from a class.
# - It defines the behavior or actions that an object can perform. Methods operate on the data within the object.
# - Methods are specific to instances (objects) of a class.

# **Key Differences:**
# 1. **Definition:**
#    - A **class** is a blueprint or a design that defines how objects will be created.
#    - A **method** is a function defined within a class, specifying what actions objects of that class can perform.

# 2. **Purpose:**
#    - A **class** defines the structure, attributes, and methods that objects will have.
#    - A **method** defines the specific actions or behaviors of objects created from a class.

# 3. **Association:**
#    - A **class** is associated with the concept of a type or category of objects.
#    - A **method** is associated with a specific instance (object) of a class.

# **Example:**

# # Class definition
# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(f"{self.name} is barking!")

# # Creating objects (instances) from the class
# dog1 = Dog("Buddy")
# dog2 = Dog("Max")

# # Calling methods on the objects
# dog1.bark()  # Output: Buddy is barking!
# dog2.bark()  # Output: Max is barking!
# Output:
# Buddy is barking!
# Max is barking!

# In this example, `Dog` is a class that defines both attributes (`name`) and a method (`bark`). Objects like `dog1` and `dog2` are instances of the `Dog` class, and 
# they can bark using the `bark` method.

# **Summary:**
# - A **class** is a blueprint or template for creating objects.
# - A **method** is a function associated with an object created from a class, defining its specific actions or behaviors.
# - Classes define what objects are, and methods define what objects can do.

# 15)what is the difference between function and method?

# Ans:**Function vs. Method in Python - Simple Explanation:**

# **Function:**
# - A **function** in Python is a block of code that performs a specific task or operation.
# - Functions are not associated with a specific object or instance; they are standalone blocks of code.
# - Functions are defined using the `def` keyword.

# **Method:**
# - A **method** in Python is a function that is associated with an object and is called on that object.
# - Methods are specific to classes and objects. They are functions that operate on the data within an object.
# - Methods are defined within a class using the `def` keyword.

# **Key Differences:**
# 1. **Association:**
#    - A **function** is not associated with any class or object. It is a standalone piece of code.
#    - A **method** is associated with a specific class and operates on the data within objects of that class.

# 2. **Call Syntax:**
#    - To call a **function**, you use its name followed by parentheses. Example: `function_name()`
#    - To call a **method**, you use the object on which the method is called, followed by a dot and the method name. Example: `object.method()`

# **Example:**

# # Function definition
# def greet(name):
#     return f"Hello, {name}!"

# # Method definition within a class
# class Greeter:
#     def greet(self, name):
#         return f"Hello, {name} from the Greeter class!"

# # Using the function
# message1 = greet("Alice")
# print(message1)  # Output: Hello, Alice!

# # Creating an object from the class
# greeter_object = Greeter()

# # Using the method
# message2 = greeter_object.greet("Bob")
# print(message2)  # Output: Hello, Bob from the Greeter class!

# Output:
# Hello, Alice!
# Hello, Bob from the Greeter class!

# In this example, `greet` is a function that can be used independently. The `greet` method is part of the `Greeter` class and is called on an object created from that 
# class.

# **Summary:**
# - A **function** is a standalone block of code not associated with any specific object.
# - A **method** is a function associated with a class or object, operating on the data within that object.
# - Functions are called by their names, while methods are called on objects using the object's name followed by a dot and the method name.

# 16)what is constructor?

# Ans:**Constructor in Python - Simple Explanation:**

# A **constructor** in Python is a special method within a class that is automatically called when an object of that class is created. Its primary purpose is to 
# initialize the attributes (properties) of the object. In Python, the constructor method is named `__init__`.

# **Key Points:**

# 1. **Initialization:**
#    - The constructor is responsible for initializing the attributes of an object when it is created.
#    - It is called automatically when an object is instantiated from the class.

# 2. **`__init__` Method:**
#    - The constructor is defined using the `__init__` method within the class.
#    - The first parameter of the `__init__` method is typically `self`, which represents the instance of the class.

# 3. **Attributes Initialization:**
#    - Inside the constructor, you can initialize the attributes by assigning values to them using the `self` keyword.
#    - Attributes are the characteristics or properties of an object.

# **Example:**

# class Person:
#     def __init__(self, name, age):
#         # Initializing attributes
#         self.name = name
#         self.age = age

# # Creating an object (instance) of the class
# person_object = Person(name="Alice", age=25)

# # Accessing attributes
# print(person_object.name)  # Output: Alice
# print(person_object.age)   # Output: 25

# Output:
# Alice
# 25

# In this example, the `__init__` method is the constructor for the `Person` class. It initializes the `name` and `age` attributes of the object when it is created. 
# When you create an instance of the `Person` class, such as `person_object`, the constructor is automatically called, setting the values for `name` and `age`.

# **Summary:**
# - A **constructor** is a special method (`__init__`) in a class.
# - It is automatically called when an object of the class is created.
# - The primary purpose is to initialize the attributes of the object.
# - Inside the constructor, attributes are initialized using the `self` keyword.

# 17)what is __init__?

# Ans:**`__init__` in Python - Simple Explanation:**

# `__init__` is a special method in Python that is part of a class. It stands for "initialize" and is commonly known as the **constructor**. The constructor is 
# automatically called when an object of the class is created, and its primary purpose is to initialize the attributes (properties) of the object.

# **Key Points:**

# 1. **Initialization:**
#    - The `__init__` method is responsible for initializing the attributes of an object during its creation.
#    - It is the first method called when an object is instantiated from the class.

# 2. **Parameters:**
#    - The `__init__` method takes `self` as its first parameter, which represents the instance of the class.
#    - Additional parameters can be included in the `__init__` method to accept values that will be used to initialize attributes.

# 3. **Attribute Assignment:**
#    - Inside the `__init__` method, you use the `self` keyword to assign values to the attributes.
#    - Attributes are the characteristics or properties of an object.

# **Example:**

# class Car:
#     def __init__(self, make, model, year):
#         # Initializing attributes
#         self.make = make
#         self.model = model
#         self.year = year

# # Creating an object (instance) of the class
# car_object = Car(make="Toyota", model="Camry", year=2022)

# # Accessing attributes
# print(car_object.make)   # Output: Toyota
# print(car_object.model)  # Output: Camry
# print(car_object.year)   # Output: 2022

# Output:
# Toyota
# Camry
# 2022

# In this example, the `__init__` method is the constructor for the `Car` class. It initializes the `make`, `model`, and `year` attributes of the object when it is 
# created. When you create an instance of the `Car` class, such as `car_object`, the constructor (`__init__`) is automatically called, setting the values for `make`, 
# `model`, and `year`.

# **Summary:**
# - `__init__` is a special method in a class, also known as the constructor.
# - It is automatically called when an object is created from the class.
# - The primary purpose is to initialize attributes of the object.
# - `self` is used to refer to the instance of the class.
# - Additional parameters can be included to accept values for initialization.

# 18)what is the difference method and constructor?

# Ans:**Difference between Method and Constructor in Python - Simple Explanation:**

# **Method:**
# - A method in Python is a function that is associated with an object.
# - It performs a specific action or behavior related to the object it belongs to.
# - Methods are defined within a class and are called on instances (objects) of that class.
# - They can take parameters and return values.

# **Constructor (`__init__`):**
# - The constructor is a special method in Python classes, denoted by `__init__`.
# - It is automatically called when an object of the class is created.
# - The primary purpose of the constructor is to initialize the attributes (properties) of the object.
# - The constructor is responsible for setting up the initial state of the object.

# **Key Differences:**

# 1. **Invocation:**
#    - **Method:** You explicitly call a method on an object using the dot notation (`object.method()`).
#    - **Constructor:** The constructor (`__init__`) is automatically invoked when an object is created.

# 2. **Purpose:**
#    - **Method:** Performs specific actions or behaviors associated with the object.
#    - **Constructor:** Initializes the attributes of the object, setting up its initial state.

# 3. **Name:**
#    - **Method:** Can have any name, not necessarily `__init__`.
#    - **Constructor:** Specifically named `__init__`.

# 4. **Return Type:**
#    - **Method:** Can return a value or perform an action without returning anything.
#    - **Constructor:** Typically does not return any value explicitly (returns `None`), as its primary purpose is initialization.

# **Example:**
# class Dog:
#     def __init__(self, name, age):
#         # Constructor to initialize attributes
#         self.name = name
#         self.age = age

#     def bark(self):
#         # Method to perform the action of barking
#         print(f"{self.name} is barking!")

# # Creating an instance of the class
# dog_instance = Dog(name="Buddy", age=3)

# # Calling a method on the object
# dog_instance.bark()  # Output: Buddy is barking!

# Output:Buddy is barking!

# In this example, `__init__` is the constructor responsible for initializing `name` and `age` attributes during object creation. The `bark` method is a regular method 
# associated with the `Dog` class, performing the action of printing a bark message.

# **Summary:**
# - Methods are functions associated with objects, performing specific actions.
# - Constructors (`__init__`) are special methods for initializing attributes, automatically called during object creation.
# - Methods are explicitly invoked, while constructors are automatically invoked.
# - Methods can have any name, but constructors are specifically named `__init__`.

# Ans:**Method vs. Constructor in Python - Simple Explanation:**

# **Method:**
# - A **method** in Python is a function that is associated with an object.
# - It defines the behavior or actions that objects of a class can perform.
# - Methods are defined within a class and are called on instances of that class.
# - They can take parameters, perform specific tasks, and return values.
# - Examples of methods include `walk()`, `talk()`, or `calculate_area()`.

# **Constructor (`__init__`):**
# - A **constructor** in Python is a special method called `__init__` that is used to initialize the attributes of an object when it is created.
# - It is automatically called when an object is instantiated from a class.
# - The constructor is responsible for setting up the initial state of the object by assigning values to its attributes.
# - It takes `self` (representing the instance of the class) as its first parameter, followed by any additional parameters needed for initialization.

# **Key Differences:**

# 1. **Purpose:**
#    - **Method:** Performs specific actions or tasks associated with objects.
#    - **Constructor (`__init__`):** Initializes the attributes of an object during its creation.

# 2. **Invocation:**
#    - **Method:** Explicitly called on instances of a class.
#    - **Constructor (`__init__`):** Automatically called when an object is created.

# 3. **Name:**
#    - **Method:** Can have any name that is meaningful for its purpose.
#    - **Constructor (`__init__`):** Has a fixed name `__init__` and serves as the class's constructor.

# 4. **Parameters:**
#    - **Method:** Can take any number of parameters, including `self` to reference the instance.
#    - **Constructor (`__init__`):** Takes `self` along with other parameters needed for attribute initialization.

# **Example:**
# class Dog:
#     def __init__(self, name, age):
#         # Constructor to initialize attributes
#         self.name = name
#         self.age = age

#     def bark(self):
#         # Method to perform a specific action
#         return f"{self.name} says 'Woof!'"

# # Creating an object of the class
# dog_object = Dog(name="Buddy", age=3)

# # Calling a method
# print(dog_object.bark())  # Output: Buddy says 'Woof!'

# # Accessing attributes initialized by the constructor
# print(dog_object.name)    # Output: Buddy
# print(dog_object.age)     # Output: 3

# Output:
# Buddy says 'Woof!'
# Buddy
# 3

# In this example, `bark()` is a method that performs the action of a dog barking. The constructor `__init__` initializes the `name` and `age` attributes when a `Dog` 
# object is created.

# **Summary:**
# - **Method:** Defines actions or tasks associated with objects, explicitly called.
# - **Constructor (`__init__`):** Initializes attributes during object creation, automatically called.
# - **Purpose:** Method performs actions, constructor initializes attributes.
# - **Name:** Method can have any name, constructor is named `__init__`.
# - **Invocation:** Method is called explicitly, constructor is automatically invoked during object creation.

# 19)what is the difference between instance variable and local variable?

# Ans:**Instance Variable vs. Local Variable - Simple Explanation:**

# **Instance Variable:**
# - An **instance variable** in Python is a variable that belongs to a specific instance (object) of a class.
# - It is defined inside a class but outside any method.
# - Each object created from the class has its own copy of the instance variable.
# - These variables represent the properties or attributes of individual objects and vary from object to object.

# **Local Variable:**
# - A **local variable** in Python is a variable that is defined within a function or method and is accessible only within that specific function or method.
# - It has a limited scope and exists only during the execution of the function where it is defined.
# - Local variables are used to store temporary data within a specific block of code and are not accessible outside that block.

# **Key Differences:**

# 1. **Scope:**
#    - **Instance Variable:** Exists throughout the lifespan of an object; its scope is the entire class.
#    - **Local Variable:** Exists only within the block (function or method) where it is defined; its scope is limited to that block.

# 2. **Accessibility:**
#    - **Instance Variable:** Accessible across different methods of the class and remains available as long as the object exists.
#    - **Local Variable:** Accessible only within the specific function or method where it is declared.

# 3. **Lifetime:**
#    - **Instance Variable:** Persists as long as the object exists; it is created when the object is instantiated and gets destroyed when the object is deleted.
#    - **Local Variable:** Created when the function is called and ceases to exist when the function completes execution.

# **Example:**

# class MyClass:
#     def __init__(self, instance_var):
#         # Instance Variable
#         self.instance_var = instance_var

#     def method_with_local_var(self):
#         # Local Variable
#         local_var = "I am a local variable"
#         print(local_var)

# # Creating an object of the class
# my_object = MyClass(instance_var="I am an instance variable")

# # Accessing instance variable
# print(my_object.instance_var)  # Output: I am an instance variable

# # Calling a method with a local variable
# my_object.method_with_local_var()  # Output: I am a local variable

# Attempting to access the local variable outside the method (will result in an error)
# print(local_var)  # Uncommenting this line will raise a NameError

# Output:
# I am an instance variable
# I am a local variable

# In this example, `instance_var` is an instance variable, and `local_var` is a local variable. The instance variable persists as long as the object exists, while the 
# local variable exists only within the method where it is defined. Attempting to access the local variable outside the method will result in an error.

# **Summary:**
# - **Instance Variable:** Belongs to an instance (object) of a class, accessible across methods, persists as long as the object exists.
# - **Local Variable:** Defined within a specific block (function or method), accessible only within that block, exists temporarily during the execution of the block.

# 20)what is self parameter?

# Ans:**`self` Parameter - Simple Explanation:**

# In Python, `self` is a convention used as the name for the first parameter of a method within a class. It refers to the instance of the class and is automatically 
# passed when calling a method on an object. The `self` parameter allows a method to access and modify attributes (variables) of the object it belongs to.

# **Key Points:**

# 1. **Reference to Instance:**
#    - `self` is not a keyword; it's a commonly used name for the first parameter of instance methods in a class.
#    - It serves as a reference to the instance (object) on which the method is called.

# 2. **Accessing Instance Variables:**
#    - Inside a class method, you use `self` to refer to instance variables.
#    - For example, `self.variable_name` refers to an instance variable.

# 3. **Invoking Other Methods:**
#    - When calling another method within the same class, you use `self.method_name()`.

# 4. **Instance-specific Operations:**
#    - `self` enables methods to perform operations specific to the instance to which they belong.

# **Example:**

# class MyClass:
#     def __init__(self, name):
#         # Instance Variable
#         self.name = name

#     def display_name(self):
#         # Accessing instance variable using self
#         print("Name:", self.name)

#     def greet(self):
#         # Calling another method within the same class
#         self.display_name()
#         print("Hello, welcome!")

# # Creating an object of the class
# my_object = MyClass(name="Alice")

# # Calling methods using the object
# my_object.greet()

# Output:
# Name: Alice
# Hello, welcome!

# In this example, `self.name` is an instance variable, and `self` is used to access it within the methods. The `greet` method calls the `display_name` method using 
# `self.display_name()`, demonstrating the use of `self` to invoke other methods within the class.

# **Summary:**
# - `self` is a convention for the first parameter in instance methods.
# - It refers to the instance (object) on which the method is called.
# - Allows access to instance variables and invocation of other methods within the class.
# - Facilitates performing operations specific to the instance.

# 21)what is access modifier?

# Ans:**Access Modifier - Simple Explanation:**

# In Python, access modifiers are mechanisms that control the visibility and accessibility of attributes and methods within a class. They determine whether a particular
# attribute or method can be accessed from outside the class or only from within the class. In Python, there are no strict access modifiers like in some other 
# programming languages (e.g., Java), but conventions are used to indicate the level of visibility.

# **Key Points:**

# 1. **Public (No Modifier):**
#    - By default, attributes and methods in Python classes are considered public.
#    - They can be accessed from anywhere, both within and outside the class.

# 2. **Protected (_ Single Underscore):**
#    - Attributes or methods with a single leading underscore (e.g., `_variable`) are considered conventionally protected.
#    - It suggests that the attribute or method should not be accessed directly from outside the class.
#    - It's a convention and does not enforce strict protection.

# 3. **Private (__ Double Underscore):**
#    - Attributes or methods with a double leading underscore (e.g., `__variable`) are considered conventionally private.
#    - It suggests that the attribute or method should not be accessed or modified directly from outside the class.
#    - Name mangling is applied, making it a bit harder to access directly, but it's not a strict enforcement.

# **Example:**

# class MyClass:
#     def __init__(self):
#         # Public attribute
#         self.public_variable = 42

#         # Protected attribute (convention)
#         self._protected_variable = "protected"

#         # Private attribute (convention)
#         self.__private_variable = "private"

#     def public_method(self):
#         print("Public method")

#     def _protected_method(self):
#         print("Protected method")

#     def __private_method(self):
#         print("Private method")

# # Creating an object of the class
# obj = MyClass()

# # Accessing public attributes and methods
# print(obj.public_variable)
# obj.public_method()

# # Accessing protected attributes and methods (convention)
# print(obj._protected_variable)
# obj._protected_method()

# # Accessing private attributes and methods (convention)
# # Note: This is not enforced as strictly private, and name mangling is applied
# print(obj._MyClass__private_variable)
# obj._MyClass__private_method()

# Output:
# 42
# Public method
# protected
# Protected method
# private
# Private method

#In this example, `public_variable` and `public_method` are public, `_protected_variable` and `_protected_method` are conventionally protected, and `__private_variable`
# and `__private_method` are conventionally private. While the conventions suggest the intended usage, Python does not enforce strict access control, and it relies on 
# developers to follow these conventions.

# **Summary:**
# - Public: Default visibility, accessible from anywhere.
# - Protected: Conventionally indicated by a single leading underscore, suggesting limited access.
# - Private: Conventionally indicated by a double leading underscore, suggesting restricted access; name mangling is applied.

# 22)what is the difference between private and public access modifier?

# Ans:**Public vs. Private Access Modifier - Simple Explanation:**

# In Python, the concepts of public and private access modifiers are conventions rather than strict enforcement. Here's a simple explanation of the differences:

# 1. **Public Access Modifier:**
#    - **Visibility:** Public attributes and methods are accessible from anywhere, both within and outside the class.
#    - **Syntax:** No special syntax is used for public members; they are declared without any leading underscores.
#    - **Example:**

# class MyClass:
#     def __init__(self):
#         self.public_variable = 42  # Public attribute

#     def public_method(self):
#         print("Public method")

#    - **Usage:** Suitable for attributes and methods that should be freely accessible from outside the class.

# 2. **Private Access Modifier:**
#    - **Visibility:** Private attributes and methods are conventionally considered private, indicating that they should not be accessed or modified directly from 
# outside the class.
#    - **Syntax:** Private members are indicated by a double leading underscore (e.g., `__variable` or `__method`).
#    - **Example:**
             
# class MyClass:
#     def __init__(self):
#         self.__private_variable = "private"  # Private attribute

#     def __private_method(self):
#         print("Private method")

#    - **Usage:** Intended for attributes and methods that should be restricted from direct external access.

# **Important Points:**
# - The use of single leading underscores (e.g., `_variable` or `_method`) is a convention for indicating protected members. While it suggests limited access, it does 
# not enforce strict protection.
# - Private members, marked by a double leading underscore, undergo name mangling, making them slightly harder to access directly from outside the class. However, this 
# is also not a strict enforcement of privacy.

# **Example:**

# class MyClass:
#     def __init__(self):
#         # Public attribute
#         self.public_variable = 42

#         # Private attribute (convention)
#         self.__private_variable = "private"

#     def public_method(self):
#         print("Public method")

#     def __private_method(self):
#         print("Private method")

# # Creating an object of the class
# obj = MyClass()

# # Accessing public attribute and method
# print(obj.public_variable)
# obj.public_method()

# # Attempting to access private attribute and method directly (name mangling applied)
# # Note: This is not a strict enforcement of privacy
# print(obj._MyClass__private_variable)
# obj._MyClass__private_method()

# Output:
# 42
# Public method
# private
# Private method

# In summary, public members are openly accessible, while private members are conventionally restricted to indicate that they should not be accessed directly from 
# outside the class. However, these conventions rely on developers adhering to best practices, as Python does not strictly enforce access control.

# 23)how to create a private method?

# Ans:In Python, you can create a private method by prefixing its name with double underscores (`__`). This naming convention signals that the method is intended for 
# private use within the class and should not be accessed directly from outside the class. Here's a simple explanation:

# **Creating a Private Method:**

# class MyClass:
#     def __init__(self):
#         # Public attribute
#         self.public_variable = 42

#         # Private attribute (convention)
#         self.__private_variable = "private"

#     def public_method(self):
#         print("Public method")

#     def __private_method(self):
#         print("Private method")

# # Creating an object of the class
# obj = MyClass()

# # Accessing public attribute and method
# print(obj.public_variable)
# obj.public_method()

# # Attempting to access private method directly (name mangling applied)
# # Note: This is not a strict enforcement of privacy
# obj._MyClass__private_method()

# Output:
# 42
# Public method
# Private method

# In this example, `__private_method` is a private method, and its name is prefixed with double underscores. This naming convention indicates that the method is 
# intended for internal use within the class. Keep in mind that while this convention discourages direct access from outside the class, it doesn't provide strict 
#     enforcement of privacy. The use of a single leading underscore (e.g., `_private_method`) is also a convention for indicating a protected method, suggesting 
# limited access.

# Remember that Python relies on developer conventions and does not have strict access control like some other programming languages.

# 24)what is __str__ method?

# Ans:In Python, the `__str__` method is a special method that you can define in a class to control how instances of that class are converted to strings. It is called by the built-in `str()` function and by the `print()` function when you try to print an object of the class. Here's a simple explanation:

# **Using `__str__` method:**

# class MyClass:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return f"MyClass instance with value: {self.value}"

# # Creating an object of the class
# obj = MyClass(42)

# # Using the print function implicitly calls the __str__ method
# print(obj)

# Output:MyClass instance with value: 42

# In this example, the `__str__` method is defined to return a string representation of the `MyClass` instance. When you use `print(obj)`, Python internally calls 
# `obj.__str__()` to obtain the string representation, and that's what gets printed.

# This method allows you to define a human-readable and informative string representation of your objects, making it easier for developers to understand and debug code.

# interview questions #
# data=[1,2,3,(33,56,7,[{"a":3000, "b":6000},90]),23]
# output:"b":6000

# data = [1, 2, 3, (33, 56, 7, [{"a": 3000, "b": 6000}, 90]), 23]
# output_value = data[3][3][0]["b"]

# output = f'b:{output_value}'
# print(output)
# Output:
# b:6000

# Inheritance
# In Python, inheritance is a mechanism that allows a class (subclass/derived class) to inherit properties and behaviors (attributes and methods) from another class 
# (superclass/base class). There are several types of inheritance in Python:

# Single Inheritance:

# A subclass inherits from only one superclass.
# Example:
# class Animal:
#     pass

# class Dog(Animal):
#     pass

# Multiple Inheritance:

# A subclass inherits from more than one superclass.
# Example
# class Bird:
#     pass

# class Mammal:
#     pass

# class Bat(Bird, Mammal):
#     pass

# Multilevel Inheritance:

# In this type, a subclass is derived from another subclass, forming a chain of inheritance.
# Example:
# class Animal:
#     pass

# class Mammal(Animal):
#     pass

# class Dog(Mammal):
#     pass

# Hierarchical Inheritance:

# Multiple subclasses inherit from a single superclass.
# Example:
# class Vehicle:
#     pass

# class Car(Vehicle):
#     pass

# class Bike(Vehicle):
#     pass

# Hybrid Inheritance:

# This is a combination of multiple types of inheritance.
# Example:
# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# class D(B, C):
#     pass

# Cyclic (or Circular) Inheritance:

# Involves a scenario where a class is derived from itself, either directly or indirectly through a chain of other classes.
# Example:
# class A(A):
#     pass

# Single level inheritance

# class User:
#     def  __init__(s,name,email,password):
#         s.name= name
#         s.email= email
#         s.password= password

#     def introuser(s):
#         return "my name is  "+s.name
    
# class Address(User):
#     def __init__(s,name,email,password,city,zipcode,state):
#         super().__init__(name,email,password)     #super ka use huwa parent class ke variable ko refer karne ke liye aur __init__use karna para because humne parent 
#         s.city= city                              #class mai constructor use kiya tha otherwise nahi use kiya hota constructor toh direct(.)dot daalke parent ke      
#         s.zipcode= zipcode                        #variable name ko refer karte.
#         s.state= state

#     def addressinfo(s):
#         return "i am from "+s.city
    
# obj=User("zaid","zaid@gmail.com","1as")
# print(obj.name)
# print(obj.email)
# print(obj.password)
# print(obj.introuser())

# obj2=Address("zaid","zaid@gmail.com","1as","mumbra","400612", "Maharastra")
# print(obj2.addressinfo())
# print(obj2.name)
# print(obj2.state)
# Output:
# zaid
# zaid@gmail.com
# 1as
# my name is  zaid
# i am from mumbra
# zaid
# Maharastra

# simple program of Single level inheritance

# class Parent:
#     name="abc"
#     age=30
#     eyecolor="brown"
#     height=5.2

#     def introParent(s):
#         print("this is parent class method")

# class Child(Parent):
#     name="xyz"
#     age=15
#     height=4.2

#     def introChild(s):
#         print("this is child class method")

# parent=Parent()
# print(parent.name)
# print(parent.age)
# print(parent.eyecolor)
# print(parent.height)
# parent.introParent()

# child=Child()
# print(child.name)
# print(child.age)
# print(child.eyecolor)
# print(child.height)
# child.introChild()
# child.introParent()
# Output:
# abc
# 30
# brown
# 5.2
# this is parent class method
# xyz
# 15
# brown
# 4.2
# this is child class method 
# this is parent class method

# Multilevel inheritance

# class GrandParent:
#     name="pqr"
#     age=60
#     eyecolor="yellow"
#     height=7
#     haircolor="green"

#     def introGrandParent(s):
#         print("this is grand parent class method")

# class Parent(GrandParent):
#     name="abc"
#     age=30
#     eyecolor="brown"
#     height=5.2

#     def introParent(s):
#         print("this is parent class method")

# class Child(Parent):
#     name="xyz"
#     age=15
#     height=4.2

#     def introChild(s):
#         print("this is child class method")

# grandparent=GrandParent()
# print(grandparent.name)
# print(grandparent.age)
# print(grandparent.eyecolor)
# print(grandparent.height)
# print(grandparent.haircolor)
# grandparent.introGrandParent()

# parent=Parent()
# print(parent.name)
# print(parent.age)
# print(parent.eyecolor)
# print(parent.height)
# print(parent.haircolor)
# parent.introParent()

# child=Child()
# print(child.name)
# print(child.age)
# print(child.eyecolor)
# print(child.height)
# print(child.haircolor)
# child.introChild()
# child.introParent()
# Output:
# pqr
# 60
# yellow
# 7
# green
# this is grand parent class method
# abc
# 30
# brown
# 5.2
# green
# this is parent class method
# xyz
# 15
# brown
# 4.2
# green
# this is child class method
# this is parent class method

# Multiple level inheritance

# class Mother:
#     name="jjj"
#     eyecolor="red"
#     haircolor="brown"

#     def mothermethod(s):
#         print("mother method called")

# class Father:
#     name="ooo"
#     eyecolor="green"

#     def fathermethod(s):
#         print("father method called")

# class Child(Father,Mother):
#     name="xyz"
#     age=15
#     height=4.2

#     def introChild(s):
#         print("this is child class method")

# child=Child()
# print(child.name)
# child.mothermethod()
# child.fathermethod()
# child.introChild()
#print(child.eyecolor) #eyecolor abhi child ka nahi hai toh yeh ab kya karega pehle child class mai dekhega eyecolor kya hai udhar nahi milega toh 
#print(child.haircolor)#class Child(Father,Mother):toh edhar dekhega pehle kya child class mai pass huwa hai toh pehle father pass huwa hai toh usme 
                      #eyecolor dekhega aur eyecolor milne pai father ka eyecolor print kar dega aur usme bhi nahi mila toh mother class mai check karega aur eyecolor  
                      #milne pai print kar dega aur nahi mila toh fir error show karega.
# Output:'
# xyz
# mother method called
# father method called
# this is child class method
# green
# brown

# hybrid level inheritance:combination of two or more than two types of inheritance

# # Base class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         pass

# # First-level derived classes (Single Inheritance)
# class Mammal(Animal):
#     def give_birth(self):
#         print(f"{self.name} is giving birth to live young.")

# class Bird(Animal):
#     def lay_eggs(self):
#         print(f"{self.name} is laying eggs.")

# # Second-level derived class (Multiple Inheritance)
# class Bat(Mammal, Bird):
#     def fly(self):
#         print(f"{self.name} can fly.")

# # Third-level derived class (Hybrid Inheritance)
# class FlyingFish(Bird):
#     def swim(self):
#         print(f"{self.name} can swim.")

# # Create instances and demonstrate hybrid inheritance
# bat = Bat("Batman")
# bat.speak()  # Inherited from Animal
# bat.give_birth()  # Inherited from Mammal
# bat.lay_eggs()  # Inherited from Bird
# bat.fly()  # Specific to Bat

# flying_fish = FlyingFish("Nemo")
# flying_fish.speak()  # Inherited from Animal
# flying_fish.lay_eggs()  # Inherited from Bird
# flying_fish.swim()  # Specific to FlyingFish
# Output:
# Batman is giving birth to live young.
# Batman is laying eggs.
# Batman can fly.
# Nemo is laying eggs.
# Nemo can swim.

# hierarchical level inheritance:

# # Base class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Derived classes (Hierarchical Inheritance)
# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} barks.")

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} meows.")

# class Cow(Animal):
#     def moo(self):
#         print(f"{self.name} moos.")

# # Create instances and demonstrate hierarchical inheritance
# dog = Dog("Buddy")
# dog.speak()  # Inherited from Animal
# dog.bark()  # Specific to Dog

# cat = Cat("Whiskers")
# cat.speak()  # Inherited from Animal
# cat.meow()  # Specific to Cat

# cow = Cow("Bessie")
# cow.speak()  # Inherited from Animal
# cow.moo()   # Specific to Cow

# Output:
# Buddy makes a sound.
# Buddy barks.
# Whiskers makes a sound.
# Whiskers meows.        
# Bessie makes a sound.  
# Bessie moos.

# HW #

#create a class user
    #- create a attribute that can count the number of object created with user class
    #- initialise the class with three attributes name, gender, salary
    #- create a method showdetails() which should print the name, gender, salary and unique account no for the user


#create a class bank
    #- create a private class variable and name it as balance
    #- initialise the class with three attributes name, gender and salary
    #- create a method deposite() which has amount parameter,
            #it should add the given amount in balance variable

    #- create a method withdraw(), which has amount paramter,
        #and uses the following constraints to withdraw money
            #1. withdraw > balance, it should return insuffient balance and display the current balance
            #2. withdraw >= 100 and withdraw <=balance , it should return Thank you for visiting
                    #and minus the withdraw amount from balance
                    #and display the current balance
            #3. withdraw < 100, it should return  you cannot withdraw less then 100 and display the current balance

    #- create a method, viewbalance(), which will show the account details and balance
    #- create a method, transfer(), which has two parameters amt, user
	#- the specified amount should be transfered to mentioned user account
	#- it should also minus the amount from balance and add the amount to mentioned users acount
	#- amount transfer should be done by using following contraints
	    #1. amt > balance, it should return insuffient balance and display the current balance
            #2. amt >= 1 and withdraw <=balance , it should return amt transfered successfully
                    #and minus the withdraw amount from balance & add the amt to specified user account
                    #and display the current balance
            #3. amt < 1, it should return  you cannot transfer less then 1 and display the current balance

# Create some test cases to check the system.

# Certainly! Below is an example implementation of the described classes (`User` and `Bank`) with methods and test cases:

# class User:
#     # Class attribute to count the number of objects
#     user_count = 0

#     def __init__(self, name, gender, salary):
#         # Instance attributes
#         self.name = name
#         self.gender = gender
#         self.salary = salary

#         # Increment the user count and assign a unique account number
#         User.user_count += 1
#         self.account_no = User.user_count

#     def show_details(self):
#         print(f"User Details - Name: {self.name}, Gender: {self.gender}, Salary: {self.salary}, Account No: {self.account_no}")

# class Bank:
#     # Private class variable
#     __balance = 0

#     def __init__(self, name, gender, salary):
#         # Instance attributes
#         self.name = name
#         self.gender = gender
#         self.salary = salary

#     def deposit(self, amount):
#         # Add the given amount to the balance
#         Bank.__balance += amount

#     def withdraw(self, amount):
#         if amount > Bank.__balance:
#             return f"Insufficient balance. Current Balance: {Bank.__balance}"
#         elif 100 <= amount <= Bank.__balance:
#             Bank.__balance -= amount
#             return f"Thank you for visiting. Current Balance: {Bank.__balance}"
#         else:
#             return f"You cannot withdraw less than 100. Current Balance: {Bank.__balance}"

#     def view_balance(self):
#         return f"Account Details - Name: {self.name}, Gender: {self.gender}, Salary: {self.salary}, Balance: {Bank.__balance}"

#     def transfer(self, amt, user):
#         if amt > Bank.__balance:
#             return f"Insufficient balance. Current Balance: {Bank.__balance}"
#         elif 1 <= amt <= Bank.__balance:
#             Bank.__balance -= amt
#             user.deposit(amt)
#             return f"Amount transferred successfully. Current Balance: {Bank.__balance}"
#         else:
#             return f"You cannot transfer less than 1. Current Balance: {Bank.__balance}"

# # Test cases
# user1 = User("Alice", "Female", 50000)
# user2 = User("Bob", "Male", 60000)

# bank = Bank("XYZ Bank", "Not Specified", 100000)

# bank.deposit(5000)
# print(bank.view_balance())

# user1.show_details()
# user2.show_details()

# print(bank.transfer(3000, user1))
# print(bank.view_balance())
# user1.show_details()
# Output:
# Account Details - Name: XYZ Bank, Gender: Not Specified, Salary: 100000, Balance: 5000
# User Details - Name: Alice, Gender: Female, Salary: 50000, Account No: 1
# User Details - Name: Bob, Gender: Male, Salary: 60000, Account No: 2
# Traceback (most recent call last):
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 10722, in <module>
#     print(bank.transfer(3000, user1))
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 10705, in transfer
#     user.deposit(amt)
#     ^^^^^^^^^^^^
# AttributeError: 'User' object has no attribute 'deposit'
# This example includes the implementation of the `User` and `Bank` classes along with some test cases to demonstrate their usage.

# class User:
#     count=987654342
#     def __init__(self,name,gender,salary):
#         self.name=name 
#         self.gender=gender
#         self.salary=salary
#         self.account_no=User.count
#         User.count+=1
    
#     def showDetails(s):
#         print(f"Name:{s.name} Gender:{s.gender} Salary:{s.salary} Account Number:{s.account_no}")

# class Bank(User):
#     def __init__(s,name,gender,salary):
#         super().__init__(name,gender,salary) #super() is a built-in function in Python that is used to call a method from the parent class. It provides a way for a 
                                               #subclass to invoke the methods or constructors of its parent class. In simple terms, super() allows you to access and 
                                               #use the functionality of the superclass (parent class) in the subclass (child class).super().__init__(name) is used to 
                                               #call the constructor of the Parent class, allowing the Child class to initialize the name attribute.

#         s.__balance=0

#     def deposite(s,amt):
#         s.__balance+=amt

#     def withdraw(s,amt):
#         if(amt>s.__balance):
#             print(f"insufficient balance \n current balance-:{s.__balance}")
#         elif(amt<=s.__balance and amt>=100):
#             s.__balance-=amt
#             print(f"your amt which is {amt} withdraw sucessfully from {s.account_no} \n your current balance is {s.__balance}")
#         elif(amt<100):
#             print(f"you cannot wihdraw less than 100 \n your current balance is {s.__balance}")
#         else:
#             print("invalid amount")

#     def viewBalance(s):
#         print(f"your current balance is {s.__balance}")
    
#     def transfer(s,amt,user):
#         if(amt>s.__balance):
#             print(f"insufficient balance \n current balance-:{s.__balance}")
#         elif(amt<=s.__balance and amt>=100):
#             s.__balance-=amt
#             print(f"your amt which is {amt} withdraw sucessfully from {s.account_no} \n your current balance is {s.__balance}")
#         elif(amt<100):
#             print(f"you cannot wihdraw less than 100 \n your current balance is {s.__balance}")
#         else:
#             print("invalid amount")

# obj1=Bank("Karan","male",23000)
# obj1.showDetails()
# obj1.viewBalance()
# obj1.deposite(1000)
# obj1.viewBalance()
# obj1.withdraw(100)

# obj2=Bank("priya","female",30000)
# obj2.showDetails()
# obj2.viewBalance()

# obj1.transfer(200,obj2)
# obj2.viewBalance()

# Output:
# Name:Karan Gender:male Salary:23000 Account Number:987654342
# your current balance is 0
# your current balance is 1000
# your amt which is 100 withdraw sucessfully from 987654342     
#  your current balance is 900
# Name:priya Gender:female Salary:30000 Account Number:987654343
# your current balance is 0
# your amt which is 200 withdraw sucessfully from 987654342     
#  your current balance is 700
# your current balance is 0

# Polymorphism:-
# there are two types of polymorphism are:
# compile time(method overloading):method overloading ko python support nahi karta hai.

# run time(method overriding):two different classes with same method and also with same attributes.


# Object Class:it is a superclass of all python classes
# In Python, the term "object class" is a bit ambiguous because all classes in Python inherently inherit from a common base class called `object`. 
# This base class provides some fundamental methods and attributes that are available to all objects in Python.

# Here's a simple explanation:

# - **Object Class (object):**
#   - In Python, every class implicitly inherits from the `object` class.
#   - The `object` class is the root of the class hierarchy in Python.
#   - It provides some basic functionalities that are common to all objects, such as the `__str__` method for string representation.
#   - When you define a class without explicitly specifying a superclass, it automatically becomes a subclass of `object`.
#   - Example:

# class MyClass:  # This class implicitly inherits from 'object'
#     def __init__(self, value):
#         self.value = value

# my_instance = MyClass(42)
# print(my_instance)  # Outputs: <__main__.MyClass object at 0x...>

# In summary, the `object` class is a foundational part of the Python class hierarchy, and every class you create is, by default, a subclass of this base class. 
# It provides essential methods and attributes that contribute to the common behavior shared by all objects in Python.

# In Python, polymorphism refers to the ability of different objects or functions to be used interchangeably, even though they may belong to different classes or 
# have different implementations. It allows a single interface (like a method or function) to work with various types of objects.

# There are two main types of polymorphism in Python:

# 1. **Compile-time Polymorphism (Method Overloading):**
#    - Involves defining multiple methods with the same name in the same class.
#    - The method that gets executed is determined by the number and types of arguments during compile-time.
#    - Example:

# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def add(self, a, b, c):
#         return a + b + c

# calc = Calculator()
# result1 = calc.add(2, 3)       # Calls the first add method
# result2 = calc.add(2, 3, 5)    # Calls the second add method

# Output:
# Traceback (most recent call last):
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 10795, in <module>
#     result1 = calc.add(2, 3)       # Calls the first add method
#               ^^^^^^^^^^^^^^
# TypeError: Calculator.add() missing 1 required positional argument: 'c'

# 2. **Run-time Polymorphism (Method Overriding):**
#    - Involves defining methods in the base class and allowing them to be overridden by the same-named methods in derived classes.
#    - The method that gets executed is determined by the actual type of the object during runtime.
#    - Example:

# class Animal:
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"

# my_dog = Dog()
# my_cat = Cat()

# print(my_dog.make_sound())    # Outputs: Woof!
# print(my_cat.make_sound())    # Outputs: Meow!

# In simple terms, polymorphism allows you to use a common interface for different objects, making your code more flexible and easier to 
# understand.

# Method Overloading:

# class Shape:
#     def area(s,r):
#         print(3.14*r*r)

#     def area(s,l,b):
#         print(l*b)

# circle=Shape()
# circle.area(5)
        
# rectangle=Shape()
# rectangle.area(5,2)

# Method overrding:
         
# class Animal:
#     def make_sound(self):
#         print("Generic  animal sound")

# class Dog:
#     def make_sound(self):
#         print("Woof!")

# dog=Dog()
# dog.make_sound()

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")
# Output:Woof!

# Abstraction:
# It is related to future implementation jiske help se child classes ya subclasses ko restrict kar detai hai kiske through abstarct method ke through agar tumko 
# parent class ke saare asbstract method ko subclass mai inherit karana hai toh necessary hai parent class ke saare abstract metthod ko subclass mai implement karna
# isko kehte hai Abstraction.
# Abstarct class ka object nahi ban sakta hai.
# yeh security provide karta hai.

# **Abstraction in Python:**

# Abstraction is a concept in Python programming that involves simplifying complex systems by modeling classes based on the essential features and hiding unnecessary 
# details. It allows programmers to focus on the relevant aspects of an object while ignoring the non-essential complexities.

# Here's a simple explanation:

# - **Abstraction:**
#   - In Python, abstraction is the process of hiding the implementation details and showing only the necessary features of an object.
#   - It helps in managing complexity by providing a clear separation between what an object does and how it achieves its functionality.
#   - Abstraction allows you to create abstract classes with abstract methods that define the interface without specifying the implementation.
#   - Abstract classes cannot be instantiated, and their subclasses must provide concrete implementations for the abstract methods.
#   - Example:

# from abc import ABC, abstractmethod

# # Abstract class with abstract method
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# # Concrete class implementing the abstract method
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# # Usage
# circle = Circle(5)
# print(circle.area())  # Outputs: 78.5

# In summary, abstraction in Python allows you to create abstract classes and abstract methods, enabling you to focus on essential features and 
# create a clear separation between the interface and the implementation details of your code.

########################################################################
# from abc  import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(s):
#         pass
#     def display(s):
#         print("this is concrete method")
# class  Circle(Shape):
#     def area(s):
#         print("hello")

# obj=Circle()
# obj.area()
# obj.display()
# Output:
# hello
# this is concrete method

# obj2=Shape() ## Abstarct class ka object nahi ban sakta hai.
# Output:
# Traceback (most recent call last):
#   File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\FirstCode.py", line 10888, in <module>
#     obj2=Shape()
#          ^^^^^^^
# TypeError: Can't instantiate abstract class Shape with abstract method area

# four pillars of OOP are:-
# 1)encapsulation(security):-Data ko bind aur wrap karke rakhna single unit mai for security purpose,private access specifier ko support karta hai.
# 2)inheritance(data reusability):
# 3)polymorphism(data reusability):
# 4)abstraction(security):

# difference between encapsulation and abstraction in python with simple english words

# In Python, encapsulation and abstraction are two related but distinct concepts.

# 1. **Encapsulation:**
#    - **Definition:** Encapsulation is the concept of bundling data (attributes) and the methods (functions) that operate on the data into a single unit known as a 
#    class.
#    - **Simple Explanation:** Think of encapsulation as putting related things together. In a class, you keep the data and the functions that work with that data 
#    together.
#    - **Example:** If you have a `Car` class, encapsulation means that the car's attributes (like color, model) and methods (like start, stop) are grouped together 
#    within the class.

# 2. **Abstraction:**
#    - **Definition:** Abstraction is the concept of simplifying complex systems by modeling classes based on the essential features and ignoring unnecessary details.
#    - **Simple Explanation:** Abstraction is about showing only what's necessary and hiding unnecessary details. You provide a simplified view of an object, focusing  
#        on what is important.
#    - **Example:** If you have a `Vehicle` class with methods like `start` and `stop`, you don't need to know the intricate details of how the engine works. 
#       Abstraction allows you to focus on the essential actions without worrying about the internal complexities.

# **In Summary:**
# - **Encapsulation:** Putting related attributes and methods together in a class.
# - **Abstraction:** Providing a simplified view of an object, focusing on essential features and hiding unnecessary details.

# These concepts work together to create clean, modular, and maintainable code in object-oriented programming.

# difference between inheritance and polymorphism in python with simple english words

# **Inheritance and Polymorphism: A Simple Explanation**

# 1. **Inheritance:**
#    - **Definition:** Inheritance is the concept where a new class (called the subclass or derived class) can inherit attributes and methods from an existing class 
#       (called the superclass or base class).
#    - **Simple Explanation:** Think of inheritance as a way to reuse code. If you have a class (e.g., `Animal`), you can create a new class (e.g., `Dog`) that 
#        automatically has all the characteristics of the original class.
#    - **Example:** If `Animal` has a method `eat()`, a `Dog` (which inherits from `Animal`) automatically has that method without explicitly defining it.

# 2. **Polymorphism:**
#    - **Definition:** Polymorphism is the ability of a single function or method to work with objects of different types. It allows one interface to be used for a 
#        general class of actions.
#    - **Simple Explanation:** Think of polymorphism as "many forms." A function can behave differently based on the type of object it's working with.
#    - **Example:** If you have a function `make_sound(animal)`, it can produce different sounds depending on whether the `animal` is a `Dog`, `Cat`, or any other class 
#        that has a `make_sound` method.

# **In Summary:**
# - **Inheritance:** Allows a new class to inherit attributes and methods from an existing class, promoting code reuse.
# - **Polymorphism:** Allows a single function or method to work with objects of different types, providing flexibility and a uniform interface.

# These concepts are fundamental to object-oriented programming and contribute to creating flexible, extensible, and maintainable code.

# Module:

# In Python, a module is a way to organize code into separate files or components. Here's a simple explanation of modules:

# 1. **Definition:**
#    - A module in Python is a file containing Python code, typically functions, classes, and variables, that can be reused in other Python programs.

# 2. **Purpose:**
#    - Modules help organize code by breaking it into smaller, manageable pieces. They promote code reusability, making it easier to maintain and collaborate on larger 
# projects.

# 3. **Creation:**
#    - To create a module, you simply write your Python code in a separate file with a `.py` extension. This file becomes a module that can be imported into other 
# Python scripts.

# 4. **Importing:**
#    - You can use the `import` keyword to bring the functionality of a module into your current script. This allows you to access functions, classes, and variables 
# defined in that module.

#    # Example of importing a module
# class MathOperations:
#     def add(self, a, b):
#         return a + b

#     def add_three(self, a, b, c):
#         return a + b + c

# 5. **Organization:**
#    - Modules help organize code logically, grouping related functionality together. For instance, you might have a module for handling database operations, another 
# for mathematical functions, etc.

# 6. **Standard Library:**
#    - Python comes with a rich set of built-in modules known as the standard library. These modules provide a wide range of functionality, from working with files to 
# handling network operations.

# # Example of using a standard library module
# import os

# # Accessing a function from the os module
# current_directory = os.getcwd()

# In summary, modules in Python are a way to structure and reuse code, making it easier to manage, understand, and maintain larger programs.

# yeh module1 mai rahega(file banake)
# x=10
# def greet():
#     return "hello"

# yeh module2 mai rahega(file banake)
# import module

# import m1
# print(m1.greet())
# print(m1.x)
# Output:
# hello
# 10

# import using alias

# import m1 as m
# print(m.greet())
# print(m.x)
# Output:
# hello
# 10

# import specific items

# from m1 import greet
# print(greet())
# Output:hello

# from m1 import greet, x
# print(greet())
# print(x)
# Output:
# hello
# 10

# Package #
# package:It is a collection of modules.

# library:It is a collection of packages and modules.

# pehle ek library banaye(folder) 
# Aur library ke andarr package1(folder) aur package2(folder) banaye
# package1 mai __init__.py(file) banega{empty rahega yeh}

# package1 mai module1.py(file) banega 
# def greet():
#     return "hello"
# x=23

# package2 mai __init__.py(file) banega{empty rahega yeh}
# package2 mai module2.py(file) banega 

# def say():
#     return "hi"

# Aur library ke bahar banega mainscript.py(file) jisme joh import karna hai woh karegai aur output print karegai.

# from package1 import module1
# from package2 import module2
# print(module1.greet())
# print(module1.x)
# print(module2.say())
# Output:
# hello
# 23
# hi

# from package1 import module1 as m1
# from package2 import module2 as m2
# print(m1.greet())
# print(m1.x)
# print(m2.say())
# Output:
# hello
# 23
# hi

# from package1.module1 import greet,x
# from package2.module2 import say
# print(greet())
# print(x)
# print(say())
# Output:
# hello
# 23
# hi

# Exception Handling

# Exception:logical error ko kehte hai exception,program ke flow ko terminate kar deta hai yeh,isko handle kar sakte hai using exception handling.

# Error:syntax error ,hardware failure,environmental failure ko kehte hai error,isko handle nahi kar sakte hai.

# try:try block ke andarr wahi code ko likhte hai jaha pai doubt lagta hai ki yaha pai logical exception raise(logical error aa sakta hai)ho 
# sakta hai.

# except:except block ke andarr message ko likhte hai ki woh logical error kya aara hai try block mai.

# n1=int(input("Enter first number"))
# n2=int(input("Enter second number"))
# op=input("Enter operator")

# match  op :
#     case "+":
#         print(n1+n2)
#     case  "-" :
#         print(n1-n2)
#     case  "*" :
#         print(n1*n2)
#     case  "/" :
#         try:
#             print(n1/n2)
#         except:
#             print("zero division error")
#     case _:
#         print("invalid operator")

# print("All works done!")
# Output:
# Enter first number2
# Enter second number3
# Enter operator+
# 5
# All works done!
# Output:
# Enter first number10
# Enter second number0
# Enter operator/
# zero division error
# All works done!


# print("hey")
# try:
#     age=int(input("enter your age: "))
#     print(age*10)
# except:
#     print("please enter numbers only")
# print("bye")
# Output:
# hey
# enter your age: 10
# 100
# bye
# Output:
# hey
# enter your age: zaid
# please enter numbers only
# bye

# try block mai error aaya toh except block chalega.
# try block mai error nahi aaya toh else block chalega.
# try block mai error aaye ya nahi aaye par finally block hamesha chalega.
# except Exception as e:It can handle all types of exception(logical errors).
# try block mai error aane ke baad yeh siddha except block pai jump karega and message print karega uske baad ka kuch bhi messgae{print("hello")}
# print nahi hoga.

# Single except block used program
# print("hey")
# try:
#     age=int(input("enter age"))
#     print(age*10)
#     print(100/age)
# except Exception as e:
#     print(e)

# print("bye")
# Output:
# hey
# enter agech
# invalid literal for int() with base 10: 'ch'
# bye
# Output:
# hey
# enter age0
# 0
# division by zero
# bye
# Output:
# hey
# enter age22
# 220
# 4.545454545454546
# bye

# Multiple except used program

# print("hey")
# try:
#     age=int(input("Enter Your Age : "))
#     print(age*10)
#     print(100/age)
# except ValueError as e:
#     print("please enter numbers only")
# except ZeroDivisionError as e:
#     print("please enter numbers which is greater than 0 ")
# except Exception as e:
#     print("something went wrong")
# print("bye")
# Output:
# hey
# Enter Your Age : ch
# please enter numbers only
# bye
# Output:
# hey
# Enter Your Age : 0
# 0
# please enter numbers which is greater than 0 
# bye
# Output:
# hey
# Enter Your Age : 26
# 260
# 3.8461538461538463
# bye

# print("hi")
# try:
#     print("hello")
#     print(10/0)
#     print("hey")
# except:
#     print("abc")
# else:
#     print("xyz")
# finally:
#     print("done")
# Output:
# hi
# hello
# abc
# done

# print("hi")
# try:
#     print("hello")
#     print(10/10)
#     print("hey")
# except:
#     print("abc")
# else:
#     print("xyz")
# finally:
#     print("done")
# Output:
# hi
# hello
# 1.0
# hey
# xyz
# done
    
# print("hi")
# try:
#     print("hello")
#     print(10/10)
#     try:
#         print("!!!")
#         int("a")
#     except:
#         print("????")
#     print("hey")
# except:
#     print("abc")
# else:
#     print("xyz")
# finally:
#     print("done")
# Output:
# hi
# hello
# 1.0
# !!!
# ????
# hey
# xyz
# done

# Exception class:It is a parent class of all exception.

# Custom Exception:khudka exception bana sakte hai isme using raise.

# class NegativeException(Exception):
#     def __init__(s):
#         super().__init__("negative exception occured")

# n=int(input("enter number :"))
# def check_negative(n):
#     if n<0:
#         raise NegativeException()
#     return n

# try:
#     res=check_negative(n)
#     print(res)
# except NegativeException as e:
#     print(e)
# Output:
# enter number :23
# 23
# Output:
# enter number :-1
# negative exception occured

# File Handling
# File handling in Python refers to the process of working with files on your computer. This involves tasks such as reading from files, writing to 
# files, and manipulating file data. Python provides built-in functions and methods that allow you to open, create, read, write, and close files.

# File handling in Python allows you to perform operations such as reading data from files, writing data to files, and appending data to existing 
# files. Let's discuss each of these operations in detail:

# 1. **Reading from Files**:
#    - To read data from a file, you first need to open it using the `open()` function with the appropriate mode (`"r"` for reading).
#    - You can then use various methods to read data from the file, such as:
#      - `read()`: Reads the entire contents of the file as a single string.
#      - `readline()`: Reads one line from the file.
#      - `readlines()`: Reads all lines from the file and returns them as a list of strings.

#    Example:
# with open("example.txt", "r") as file:
#     data = file.read()  # Read the entire file
#     line = file.readline()  # Read one line from the file
#     lines = file.readlines()  # Read all lines from the file

# 2. **Writing to Files**:
#    - To write data to a file, you open the file in write mode (`"w"`).
#    - You can then use the `write()` method to write data to the file. Note that this operation will overwrite the existing content of the file.
#    - Alternatively, you can use the `writelines()` method to write a list of strings to the file.

#    Example:
# with open("example.txt", "w") as file:
#     file.write("Hello, World!")  # Write data to the file

# 3. **Appending to Files**:
#    - To append data to an existing file, you open the file in append mode (`"a"`).
#    - You can then use the `write()` method to append data to the file. This operation will add new data to the end of the file without 
# overwriting existing content.

#    Example:
# with open("example.txt", "a") as file:
#     file.write("This is a new line.")  # Append data to the file

# 4. **Closing Files**:
#   - It's essential to close files after you finish working with them to free up system resources and ensure that any changes are saved properly.
#   - You can close files using the `close()` method or by using a `with` statement, which automatically closes the file when you exit the block.

#    Example:
# file = open("example.txt", "r")
# data = file.read()
# file.close()
# # or
# with open("example.txt", "r") as file:
#     data = file.read()

# Quastech Code
# File handling in Python is a versatile and powerful feature that allows you to work with files efficiently for various purposes.

# "r" read karne ke kaam aata hai yeh aur yeh naya file nahi banata hai exist file mai he content dhundta hai yeh.(/)
# file=open("file handling/first.txt","r")
# content=file.read()
# print(content)
# file.close
# Output:my name is zaid

# "r" read karne ke kaam aata hai yeh aur yeh naya file nahi banata hai exist file mai he content dhundta hai yeh.(/)
# file=open("firstt.txt","r")
# content=file.read()
# print(content)
# file.close()
# Output:
# File "c:\Users\Zaid Ansari\OneDrive\Desktop\Quastech Python\file handling\main.py", line 8, in <module>
#     file=open("firstt.txt","r")
#          ^^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'firstt.txt'

# "r" read karne ke kaam aata hai yeh aur yeh naya file nahi banata hai exist file mai he content dhundta hai yeh.(/)
# try:
#     file=open("firstt.txt","r")
#     content=file.read()
#     print(content)
#     file.close()
# except Exception as e:
#     print(e)
# Output:[Errno 2] No such file or directory: 'firstt.txt'

# "rb" read karne ke kaam aata hai binary file ko yeh aur yeh naya file nahi banata hai exist file mai he content dhundta hai yeh.(/) 
# isme output bhi aata hai binary mai.
# try:
#     file=open("mock marks.xlsx","rb")
#     content=file.read()
#     print(content)
#     file.close()
# except Exception as e:
#     print(e)

# "with" jab used karegai toh apne ko close karne ki zaroorat nahi parti hai aur yeh zyaada safer hota hai.
# "rb" read karne ke kaam aata hai binary file ko yeh aur yeh naya file nahi banata hai exist file mai he content dhundta hai yeh.(/) 
# isme output bhi aata hai binary mai.
# try:
#     with open("mock marks.xlsx","rb") as file:
#         content=file.read()
#         print(content)
# except Exception as e:
#     print(e)

# "w" yeh write karne ke liye used hota hai aur yeh harr baar naya file banayega even file exist ho woh naam se tabb bhi naya file banayega.
# file=open("file handling/first.txt","w")
# file.write("this is write mode text")
# file.write("my name is zaid")
# file.close()
# Output:this is write mode textmy name is zaid

# "w" yeh write karne ke liye used hota hai aur yeh harr baar naya file banayega even file exist ho woh naam se tabb bhi naya file banayega.
# file=open("second.txt","w")
# file.write("this is write mode text")
# file.close()
# Output:this is write mode text

# "a" yeh append karne ke liye used hota hai aur yeh harr baar naya file banayega even file exist ho woh naam se tabb bhi naya file banayega.
# isme ek senctence ke baad uske aagai ka sentence aayega.
# file=open("file handling/first.txt","a")
# file.write("this is write mode text")
# file.close()
# Output:this is write mode textmy name is zaidthis is write mode text

# Multhreading:It is used to perform mutiple task at a same time simultaneously.

# import time
# import threading
# x="24"
# def show():
#     print("Loading....")
#     time.sleep(5)
#     global x 
#     x=int(x)
#     print("hello")
# def display():
#     print("hii")
# t1=threading.Thread(target=show)
# t2=threading.Thread(target=display)
# t1.start()
# t2.start()
# t1.join()
# print("square of x is ",x**2)
# print("hey")
# Output:
# Loading....
# hii
# hello
# square of x is  576
# hey

# Explanation:
# ### 1. `import time`:
# - This line imports the `time` module in Python, which provides functions for working with time-related tasks.

# ### 2. `import threading`:
# - This line imports the `threading` module, which enables multithreading support in Python by providing classes and functions for working with 
# threads.

# ### 3. `x="24"`:
# - This line assigns the string value `"24"` to the variable `x`.

# ### 4. `def show():`:
# - This line defines a function named `show()`. This function will be executed by one of the threads.

# ### 5. `print("Loading....")`:
# - This line prints the message "Loading...." to the console.

# ### 6. `time.sleep(5)`:
# - This line pauses the execution of the current thread for 5 seconds using the `sleep()` function from the `time` module.

# ### 7. `global x`:
# - This line declares the variable `x` as global within the `show()` function, allowing it to be modified inside the function.

# ### 8. `x=int(x)`:
# - This line converts the string value of `x` to an integer using the `int()` function and updates the value of `x`.

# ### 9. `print("hello")`:
# - This line prints the message "hello" to the console.

# ### 10. `def display():`:
# - This line defines another function named `display()`, which will be executed by the second thread.

# ### 11. `print("hii")`:
# - This line prints the message "hii" to the console.

# ### 12. `t1=threading.Thread(target=show)`:
# - This line creates a new `Thread` object named `t1` with the `show()` function as its target. This means that when `t1` is started, it will 
# execute the `show()` function.

# ### 13. `t2=threading.Thread(target=display)`:
# - This line creates another `Thread` object named `t2` with the `display()` function as its target.

# ### 14. `t1.start()` and `t2.start()`:
# - These lines start the execution of the threads `t1` and `t2`, respectively. Once started, each thread will execute its target function 
# concurrently.

# ### 15. `t1.join()`:
# - This line blocks the main thread until `t1` has completed its execution.

# ### 16. `print("square of x is ",x**2)`:
# - This line calculates the square of the integer value of `x` and prints it along with the message "square of x is " to the console.

# ### 17. `print("hey")`:
# - This line prints the message "hey" to the console.

# In summary, this program demonstrates the use of multithreading in Python to execute multiple tasks concurrently, allowing for improved 
# efficiency and responsiveness in applications. It also showcases the synchronization of threads using the `join()` method to ensure that certain 
# operations are completed before others proceed.

# import time
# import threading
# def worker():
#     print("worker starting")
#     time.sleep(5)
#     print("worker finishing")

# #create threads
# threads=[]
# for _ in range(5):
#     t=threading.Thread(target=worker)
#     threads.append(t)
#     t.start()

# #wait for all threads to finish
# for t in  threads:
#     t.join()
# print("All threads finished")
# Output:
# worker starting
# worker starting
# worker starting
# worker starting
# worker starting
# worker finishing
# worker finishing
# worker finishing
# worker finishing
# worker finishing

# Explanation:

# ### 1. `import time`:
# - This line imports the `time` module in Python, which provides functions for working with time-related tasks.

# ### 2. `import threading`:
# - This line imports the `threading` module, which enables multithreading support in Python by providing classes and functions for working with 
# threads.

# ### 3. `def worker():`:
# - This line defines a function named `worker()`. This function will be executed by each thread.

# ### 4. `print("worker starting")`:
# - This line prints the message "worker starting" to the console when a thread starts executing the `worker()` function.

# ### 5. `time.sleep(5)`:
# - This line pauses the execution of each thread for 5 seconds using the `sleep()` function from the `time` module.

# ### 6. `print("worker finishing")`:
# - This line prints the message "worker finishing" to the console when a thread completes execution of the `worker()` function.

# ### 7. `threads=[]`:
# - This line initializes an empty list named `threads` to store the thread objects.

# ### 8. `for _ in range(5):`:
# - This line starts a loop that iterates 5 times.

# ### 9. `t=threading.Thread(target=worker)`:
# - This line creates a new `Thread` object `t` with the `worker()` function as its target. Each thread created will execute the `worker()` 
# function.

# ### 10. `threads.append(t)`:
# - This line appends the newly created thread object `t` to the `threads` list.

# ### 11. `t.start()`:
# - This line starts the execution of the thread `t`. Once started, each thread will execute the `worker()` function concurrently.

# ### 12. `for t in  threads:`:
# - This line starts a loop that iterates over each thread object in the `threads` list.

# ### 13. `t.join()`:
# - This line blocks the main thread until each thread `t` has completed its execution.

# ### 14. `print("All threads finished")`:
# - This line prints the message "All threads finished" to the console after all threads have completed their execution.

# In summary, this program demonstrates the use of multithreading in Python to execute multiple tasks concurrently. Each thread executes the 
# `worker()` function, and the main thread waits for all threads to finish before printing a completion message.

# Synchronous:isme jab tak pehla kaam nahi hoga tabb tak aagai ka kaam process nahi hoga.

# Asynchronous:isme multiple kaam saath mai karega aur muthithreading asynchronous karne ke kaam aata hai.

# import time
# import threading
# class File(threading.Thread):
#     def run(s):
#         print("download file start")
#         print("Loading....file")
#         time.sleep(2)
#         print("download file completed")
    
#     def downloadfile(s):
#         print("download file start")
#         print("Loading....file")
#         time.sleep(2)
#         print("download file completed")

# class Video(threading.Thread):
#     def run(s):
#         print("downlaod  video start")
#         print("Loading....Video")
#         time.sleep(5)
#         print("downlaod  video completed")

#     def downloadvideo(s):
#         print("download video start")
#         print("Loading....video")
#         time.sleep(5)
#         print("download video completed")

# file=File()
# video=Video()
# start=time.time()
# # file.downloadfile()
# # video.downloadvideo()
# file.start()
# video.start()
# file.join()
# video.join()
# end=time.time()
# print(end-start)
# print("All tasks completed")

# Output:
# download file start
# Loading....file      
# downlaod  video start
# Loading....Video     
# download file completed
# downlaod  video completed
# 5.004589319229126
# All tasks completed

# Database Connectivity
# Terminal:python
# Terminal:exit()
# Terminal:pip install pymysql

# import pymysql as p
# print("done...")
# Output:done...

# import pymysql as p
# connection=p.connect(
#     user="root",
#     password="ansarizaid1234",
#     host="localhost",
#     port=3306,
#     database="my_cascade"
# )
# cursor = connection.cursor()

# select all users
# sql="select * from user"
# cursor.execute(sql)
# rows=cursor.fetchall()
# print(rows)
# print("done...")
# connection.close()
# Output:
# ((1, 'Priya', 'Vikroli', 'pra@gmail.com', '1122abb'), (2, 'Zaid', 'Mumbra', 'za@gmail.com', '1122abb'), (3, 'Karan', 'Diva', 'ka@gmail.com',
# '1122abb'), (4, 'Amol', 'Thane', 'am@gmail.com', '1122abb'), (5, 'Rohan', 'Kalva', 'ro@gmail.com', '1122abb'))
# done...

# cursor = connection.cursor()
# This statement creates a "cursor" object that allows Python to interact with the MySQL database through the established connection.
#  Think of a cursor as a tool or a pointer that helps you navigate through the rows of data in a database. It's like having a finger that can 
#  point to different rows in a table, allowing you to read or modify the data.

# In other words, when you want to execute SQL queries and retrieve results from the database, you first need to create a cursor. This cursor acts 
# as your intermediary or assistant, helping you send SQL commands to the database server and receive the results back.

# Once you have a cursor, you can use it to execute SQL queries, fetch data from the database, and perform various operations like inserting,
# updating, or deleting records. So, creating a cursor is the initial step in interacting with the database using Python.

# sql="""select user.name,course.course_name from user inner join user_course on user.id=user_course.user_id 
# inner join course on user_course.course_id=course.id"""
# cursor.execute(sql)
# rows=cursor.fetchall()
# print(rows)
# print("done...")
# connection.close()
# Output:
# (('Priya', 'Java'), ('Zaid', 'Java'), ('Zaid', 'Web Development'), ('Karan', 'Web Development'), ('Rohan', 'Python'), ('Rohan', 'Python'))
# done...
# rows=cursor.fetchone()
# print(rows)
# connection.close()
# Output:
# (1, 'Priya', 'Vikroli', 'pra@gmail.com', '1122abb')
# done...
# rows=cursor.fetchmany(3)
# print(rows)
# connection.close()
# Output:
# ((1, 'Priya', 'Vikroli', 'pra@gmail.com', '1122abb'), (2, 'Zaid', 'Mumbra', 'za@gmail.com', '1122abb'), (3, 'Karan', 'Diva', 'ka@gmail.com',
#  '1122abb'))
# done...
# for row in rows:
#     print(row)
# Output:
# (1, 'Priya', 'Vikroli', 'pra@gmail.com', '1122abb')       
# (2, 'Zaid', 'Mumbra', 'za@gmail.com', '1122abb')
# (3, 'Karan', 'Diva', 'ka@gmail.com', '1122abb')
# (4, 'Amol', 'Thane', 'am@gmail.com', '1122abb')
# (5, 'Rohan', 'Kalva', 'ro@gmail.com', '1122abb')
# done...
# print("done...")

# select by id
# id=3
# sql="select * from user where id=%s"   #%s is placeholder
# cursor.execute(sql,id)
# rows=cursor.fetchone()
# print(rows)
# print("done...")
# connection.close()
# Output:
# (3, 'Karan', 'Diva', 'ka@gmail.com', '1122abb')
# done...

# insert user
# t=(8,"prashant","ulhasnagar","prashant@gmail.com","1234a")
# sql= "insert into user values(%s,%s,%s,%s,%s)"
# res=cursor.execute(sql,t)
# print(res)
# connection.commit()
# connection.close()
# Output:1

# Update user
# t=("prashant","ulhasnagar","prashant88@gmail.com","1234ab",8)
# sql = "update user set name=%s,city=%s,email=%s,password=%s where id=%s"
# res=cursor.execute(sql,t)
# print(res)
# connection.commit()
# connection.close()
# Output:1

#  delete user
# id=8
# sql="delete from user where id=%s"
# res=cursor.execute(sql,id)
# print(res)
# connection.commit()
# connection.close()
# Output:1

# import pymysql as p
# connection=p.connect(
#     user="root",
#     password="ansarizaid1234",
#     host="localhost",
#     port=3306,
#     database="my_cascade"
# )
# cursor = connection.cursor()
# # select all users
# sql="select * from user"
# cursor.execute(sql)
# rows=cursor.fetchall()
# print(rows)
# for row in rows:
#     print(row)
# print("done...")
# connection.close()

# # select by id
# id=3
# sql="select * from user where id=%s"   #%s is placeholder
# cursor.execute(sql,id)
# rows=cursor.fetchone()
# print(rows)
# print("done...")
# connection.close()

# # insert user
# t=(8,"prashant","ulhasnagar","prashant@gmail.com","1234a")
# sql= "insert into user values(%s,%s,%s,%s,%s)"
# res=cursor.execute(sql,t)
# print(res)
# connection.commit()
# connection.close()

# # Update user
# t=("prashant","ulhasnagar","prashant88@gmail.com","1234ab",8)
# sql = "update user set name=%s,city=%s,email=%s,password=%s where id=%s"
# res=cursor.execute(sql,t)
# print(res)
# connection.commit()
# connection.close()

# #  delete user
# id=8
# sql="delete from user where id=%s"
# res=cursor.execute(sql,id)
# print(res)
# connection.commit()
# connection.close()

# def select():
#     cursor = connection.cursor()
#     sql="select * from user"
#     cursor.execute(sql)
#     rows=cursor.fetchall()
#     print(rows)
#     for row in rows:
#         print(row)
#     print("done...")
#     connection.close()

# def selectById(id):
#     cursor = connection.cursor()
#     sql="select * from user where id=%s"   #%s is placeholder
#     cursor.execute(sql,id)
#     rows=cursor.fetchone()
#     print(rows)
#     print("done...")
#     connection.close()

# def insertUser(t):
#     cursor = connection.cursor()
#     sql= "insert into user values(%s,%s,%s,%s,%s)"
#     res=cursor.execute(sql,t)
#     print(res)
#     connection.commit()
#     connection.close()

# def updateUser(t):
#     cursor = connection.cursor()
#     sql = "update user set name=%s,city=%s,email=%s,password=%s where id=%s"
#     res=cursor.execute(sql,t)
#     print(res)
#     connection.commit()
#     connection.close()

# def deleteUser(id):
#     cursor = connection.cursor()
#     sql="delete from user where id=%s"
#     res=cursor.execute(sql,id)
#     print(res)
#     connection.commit()
#     connection.close()

# select()
# Output:
# ((1, 'Priya', 'Vikroli', 'pra@gmail.com', '1122abb'), (2, 'Zaid', 'Mumbra', 'za@gmail.com', '1122abb'), (3, 'Karan', 'Diva', 'ka@gmail.com',
# '1122abb'), (4, 'Amol', 'Thane', 'am@gmail.com', '1122abb'), (5, 'Rohan', 'Kalva', 'ro@gmail.com', '1122abb'))
# (1, 'Priya', 'Vikroli', 'pra@gmail.com', '1122abb')       
# (2, 'Zaid', 'Mumbra', 'za@gmail.com', '1122abb')
# (3, 'Karan', 'Diva', 'ka@gmail.com', '1122abb')
# (4, 'Amol', 'Thane', 'am@gmail.com', '1122abb')
# (5, 'Rohan', 'Kalva', 'ro@gmail.com', '1122abb')
# done...
    
# selectById(2)
# Output:
# (2, 'Zaid', 'Mumbra', 'za@gmail.com', '1122abb')
# done...

# import pymysql as p

# # Establish connection
# connection = p.connect(
#     user="root",
#     password="ansarizaid1234",
#     host="localhost",
#     port=3306,
#     database="my_cascade"
# )
# cursor = connection.cursor()

# # Function to select all users
# def select_all():
#     cursor.execute("SELECT * FROM user")
#     rows = cursor.fetchall()
#     print(rows)

# # Function to select user by ID
# def select_by_id(id):
#     cursor.execute("SELECT * FROM user WHERE id=%s", (id,))
#     row = cursor.fetchone()
#     print(row)

# # Function to insert user
# def insert_user(values):
#     cursor.execute("INSERT INTO user VALUES (%s, %s, %s, %s, %s)", values)
#     connection.commit()

# # Function to update user
# def update_user(values):
#     cursor.execute("UPDATE user SET name=%s, city=%s, email=%s, password=%s WHERE id=%s", values)
#     connection.commit()

# # Function to delete user
# def delete_user(id):
#     cursor.execute("DELETE FROM user WHERE id=%s", (id,))
#     connection.commit()

# while True:
#     print("1. Select all users")
#     print("2. Select user by ID")
#     print("3. Insert user")
#     print("4. Update user")
#     print("5. Delete user")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         select_all()
#     elif choice == '2':
#         id = input("Enter user ID: ")
#         select_by_id(id)
#     elif choice == '3':
#         values = (input("Enter ID: "), input("Enter name: "), input("Enter city: "), input("Enter email: "), input("Enter password: "))
#         insert_user(values)
#     elif choice == '4':
#         values = (input("Enter name: "), input("Enter city: "), input("Enter email: "), input("Enter password: "), input("Enter ID: "))
#         update_user(values)
#     elif choice == '5':
#         id = input("Enter user ID to delete: ")
#         delete_user(id)
#     elif choice == '6':
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.")

# # Close connection
# connection.close()

# Output:
# 1. Select all users
# 2. Select user by ID
# 3. Insert user      
# 4. Update user      
# 5. Delete user      
# 6. Exit
# Enter your choice: 1
# ((1, 'Priya', 'Vikroli', 'pra@gmail.com', '1122abb'), (2, 'Zaid', 'Mumbra', 'za@gmail.com', '1122abb'), (3, 'Karan', 'Diva', 'ka@gmail.com',
# '1122abb'), (4, 'Amol', 'Thane', 'am@gmail.com', '1122abb'), (5, 'Rohan', 'Kalva', 'ro@gmail.com', '1122abb'))

# Output:
# 1. Select all users
# 2. Select user by ID
# 3. Insert user
# 4. Update user
# 5. Delete user
# 6. Exit
# Enter your choice: 2
# Enter user ID: 3
# (3, 'Karan', 'Diva', 'ka@gmail.com', '1122abb')

# Output:
# 1. Select all users
# 2. Select user by ID
# 3. Insert user
# 4. Update user
# 5. Delete user
# 6. Exit
# Enter your choice: 3
# Enter ID: 6
# Enter name: "vaibhav"
# Enter city: "sion"
# Enter email: "vaibhav@gmail.com"
# Enter password: "vaibhav1234"
# ((1, 'Priya', 'Vikroli', 'pra@gmail.com', '1122abb'), (2, 'Zaid', 'Mumbra', 'za@gmail.com', '1122abb'), (3, 'Karan', 'Diva', 'ka@gmail.com',
# '1122abb'), (4, 'Amol', 'Thane', 'am@gmail.com', '1122abb'), (5, 'Rohan', 'Kalva', 'ro@gmail.com', '1122abb'), (6, '"vaibhav"', '"sion"',
# '"vaibhav@gmail.com"', '"vaibhav1234"'))

# Output:
# 1. Select all users
# 2. Select user by ID
# 3. Insert user      
# 4. Update user      
# 5. Delete user      
# 6. Exit
# Enter your choice: 4
# Enter name: "VAIBHAV"
# Enter city: "SION"
# Enter email: "VAIBHAV@GMAIL.COM"
# Enter password: "VAIBHAV1234"
# Enter ID: 6
# ((1, 'Priya', 'Vikroli', 'pra@gmail.com', '1122abb'), (2, 'Zaid', 'Mumbra', 'za@gmail.com', '1122abb'), (3, 'Karan', 'Diva', 'ka@gmail.com',
# '1122abb'), (4, 'Amol', 'Thane', 'am@gmail.com', '1122abb'), (5, 'Rohan', 'Kalva', 'ro@gmail.com', '1122abb'), (6, '"VAIBHAV"', '"SION"',
# '"VAIBHAV@GMAIL.COM"', '"VAIBHAV1234"'))

# Output:
# 1. Select all users
# 2. Select user by ID
# 3. Insert user      
# 4. Update user      
# 5. Delete user      
# 6. Exit
# Enter your choice: 5
# Enter user ID to delete: 6
# ((1, 'Priya', 'Vikroli', 'pra@gmail.com', '1122abb'), (2, 'Zaid', 'Mumbra', 'za@gmail.com', '1122abb'), (3, 'Karan', 'Diva', 'ka@gmail.com',
# '1122abb'), (4, 'Amol', 'Thane', 'am@gmail.com', '1122abb'), (5, 'Rohan', 'Kalva', 'ro@gmail.com', '1122abb'))

# Output:
# 1. Select all users
# 2. Select user by ID
# 3. Insert user
# 4. Update user
# 5. Delete user
# 6. Exit
# Enter your choice: 6
# Exiting...

# Regular Expression

# Regular expressions, often abbreviated as regex or regexp, are powerful tools for pattern matching and text manipulation. In Python, the re 
# module provides support for regular expressions.

# import re

# text="The quick  brown fox jumps over the lazy dog."
# pattern = r'\bfox\b'
# matches=re.findall(pattern, text)
# print(matches)
# Output:['fox']

# text="My email is example@example.com"
# pattern=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
# matches=re.findall(pattern, text)
# print(matches)
# Output:['example@example.com']

# text="My phone numbers are 123-456-7890 and 987-654-3210"
# pattern=r"\b\d{3}-\d{3}-\d{4}\b"
# matches=re.findall(pattern,text)
# print(matches)
# Output:['123-456-7890', '987-654-3210']

# text="Hello,my name is John"
# pattern=r'John'
# new_text=re.sub(pattern,'Alice',text)
# print(new_text)
# Output:Hello,my name is Alice

# def is_valid_password(password):
#     pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
#     return bool(re.match(pattern,password))
# print(is_valid_password('Password123'))
# print(is_valid_password('pass'))
# Output:
# True
# False

# Django support mvt and api but not mvc

# What is Django
# Django is a high-level web framework written in Python that allows developers to quickly build web applications. It provides a 
# set of tools, libraries, and patterns to help streamline the development process and encourages the use of clean, pragmatic design.

# Difference between Django and Flask
# Django->Framework hai,heavy weight web application ke liye used hota hai

# Flask->Library hai,light weight web application ke liye used hota hai

# Difference between mvt and mvc
# In simple terms, both MVT (Model-View-Template) and MVC (Model-View-Controller) are architectural patterns used for designing web applications. 
# Here's a brief explanation of each:

# 1. **MVC (Model-View-Controller):**
#    - **Model:** Represents the data and business logic of the application. It interacts with the database and handles data manipulation.
#    - **View:** Represents the user interface (UI) of the application. It displays data to the user and captures user interactions.
#    - **Controller:** Acts as an intermediary between the model and view. It receives input from the user via the view, processes it using the 
# model, and updates the view with the results.

# 2. **MVT (Model-View-Template):**
#    - **Model:** Similar to MVC, the model represents the data and business logic of the application.
#    - **View:** In MVT, the view is responsible for rendering the user interface. It defines how data is presented to the user but doesn't handle 
# user interactions.
#    - **Template:** This is unique to MVT. Templates are used to generate dynamic HTML pages by inserting data into predefined placeholders. 
# Templates encapsulate the presentation logic but are simpler than views in MVC.

# The key difference between MVT and MVC lies in the role of the view/template component:
# - In MVC, the view is responsible for both rendering the UI and handling user interactions.
# - In MVT, the view is only responsible for rendering the UI, while the template is used for generating dynamic content based on data.

# Overall, both patterns aim to separate concerns and promote a more organized and maintainable codebase. MVT, as used in Django, simplifies the 
# presentation layer by introducing templates, which can be advantageous for developers working with HTML and frontend technologies.

# asgi.py
# ASGI (Asynchronous Server Gateway Interface) is a specification used in Django and other Python web frameworks for handling asynchronous 
# request/response operations, such as WebSocket connections, long polling, and streaming HTTP responses.

# In simple terms, ASGI allows Django to handle real-time communication and asynchronous tasks, which are typically beyond the capabilities of 
# traditional synchronous HTTP requests. ASGI servers can handle multiple connections concurrently, making them suitable for applications that 
# require bidirectional communication or long-running tasks.

# The `asgi.py` file in a Django project serves as the entry point for ASGI applications. It contains an ASGI application instance that connects 
# Django's synchronous codebase with asynchronous servers and middleware. When Django receives a request, it passes it to the ASGI application 
# defined in `asgi.py`, which then handles the request asynchronously.

# In summary, `asgi.py` enables Django to support asynchronous operations and real-time communication by providing an interface for connecting 
# with ASGI servers and middleware.

# settings.py
# In Django, `settings.py` is a configuration file that contains various settings and options for your Django project. It serves as a central 
# place to configure the behavior of your project, such as database settings, static files configuration, middleware settings, and much more.

# Here's a breakdown of what `settings.py` is used for in simple English:

# 1. **Database Configuration**: You specify the database engine, name, user, password, host, and other details needed to connect your Django 
# project to a database. This allows Django to interact with your database to store and retrieve data for your application.

# 2. **Static Files Configuration**: You define the directories where your static files (such as CSS, JavaScript, and images) are located. Django 
# uses this information to serve static files during development and collect them into a single location for production.

# 3. **Template Configuration**: You specify the directories where your Django templates are located. Templates are HTML files with Django 
# template language tags that allow you to dynamically generate HTML content.

# 4. **Middleware Configuration**: You list the middleware classes that Django should use for request/response processing. Middleware is code that 
# runs before and after each request, allowing you to modify request or response objects, perform authentication, and more.

# 5. **Installed Apps**: You list the names of Django apps that are installed in your project. Each app may contain models, views, URLs, and other 
# components that contribute to your project's functionality.

# 6. **Debugging and Security Settings**: You configure settings related to debugging and security, such as whether debug mode is enabled, allowed 
# hosts, secret key, CSRF protection, and more.

# 7. **Internationalization and Localization**: You configure settings related to internationalization (i18n) and localization (l10n), such as 
# default language, time zone, and localization paths.

# 8. **Logging Configuration**: You specify how Django should handle logging, including log levels, output formats, and handlers.

# 9. **Custom Settings**: You can define custom settings specific to your project or application that you want to access throughout your codebase.

# Overall, `settings.py` is a vital component of a Django project that allows you to customize and configure various aspects of your application's 
# behavior. It provides a convenient way to centralize configuration settings and manage the behavior of your Django project.

# urls.py
# In Django, `urls.py` is a Python module used to define URL patterns for your web application. It acts as a router that maps URL patterns to 
# views, allowing Django to determine which view function should handle a particular URL.

# Here's a breakdown of what `urls.py` is used for in simple English:

# 1. **Defining URL Patterns**: You define URL patterns using regular expressions or path converters to match incoming URLs. These patterns can 
# include placeholders for dynamic parts of the URL, such as `<int:pk>` for an integer parameter or `<slug:slug>` for a slug parameter.

# 2. **Mapping URLs to View Functions**: You associate each URL pattern with a view function that should be executed when the corresponding URL is 
# accessed. This allows Django to direct incoming requests to the appropriate view for processing.

# 3. **Namespacing URL Patterns**: You can organize URL patterns into different namespaces to avoid naming conflicts and provide better 
# organization for your URL structure. Namespaces help differentiate URLs from different parts of your application.

# 4. **Including URLs from Other Modules**: You can include URL patterns from other `urls.py` modules using the `include()` function. This allows 
# you to modularize your URL configuration and organize your URL patterns into smaller, more manageable components.

# 5. **Passing URL Parameters to View Functions**: URL patterns can capture parts of the URL as parameters and pass them to the associated view 
# function as arguments. This allows your view functions to access dynamic data from the URL, such as an ID or slug, and use it to generate a 
# response.

# 6. **Defining URL Names**: You can assign names to URL patterns using the `name` argument. This allows you to refer to URLs by their names in 
# templates and view functions instead of hardcoding the URLs, which makes your code more maintainable and easier to update.

# Overall, `urls.py` serves as a central location for defining the URL configuration of your Django application. It allows you to map URLs to view 
# functions, organize your URL structure, and handle dynamic URL parameters, providing a flexible and maintainable way to define how incoming 
# requests are handled.

# wsgi.py
# In Django, `wsgi.py` is a Python file that serves as the entry point for running your Django application using a WSGI (Web Server Gateway 
# Interface) server. Here's a simple explanation of its usage:

# 1. **WSGI Server Integration**: When you deploy your Django application to a production environment, you typically use a WSGI server like 
# Gunicorn, uWSGI, or mod_wsgi to serve your application to the web. `wsgi.py` acts as the gateway between your Django application and the WSGI 
# server.

# 2. **WSGI Application Object**: Inside `wsgi.py`, there's usually a variable named `application` that represents your Django application as a 
# WSGI application object. This object is a callable that the WSGI server uses to handle HTTP requests and responses.

# 3. **Initialization and Configuration**: You can also perform initialization and configuration tasks within `wsgi.py`. This might include 
# setting up environment variables, configuring logging, or any other necessary setup steps before your Django application starts serving requests.

# 4. **Deployment**: When deploying your Django application, you specify `wsgi.py` as the entry point for the WSGI server. The server loads the 
# WSGI application object from `wsgi.py` and starts serving incoming HTTP requests using your Django application.

# In essence, `wsgi.py` plays a crucial role in deploying your Django application by providing the interface between your application and the WSGI 
# server, enabling it to handle web traffic effectively.

# views.py
# In Django, `views.py` is a Python file where you define the logic for handling HTTP requests and generating HTTP responses. Here's a 
# simple explanation of its usage:

# 1. **Request Handling**: Each function or class-based view defined in `views.py` corresponds to a particular URL endpoint in your Django 
# application. When a request is made to a URL, Django's URL resolver determines which view function to call based on the URL configuration.

# 2. **Business Logic**: Inside the view functions, you write the business logic for processing the incoming HTTP request. This may involve 
# querying the database, performing calculations, or any other necessary operations to generate a response.

# 3. **Response Generation**: After processing the request, the view function constructs an HTTP response object, typically using Django's 
# `HttpResponse` class or one of its subclasses. This response object can include HTML content, JSON data, or any other content type required by 
# the client.

# 4. **Rendering Templates**: In addition to generating responses programmatically, views can also render HTML templates using Django's template 
# engine. Templates allow you to separate the presentation logic from the business logic, making your code cleaner and more maintainable.

# 5. **Class-Based Views**: In addition to function-based views, Django also supports class-based views, which are defined as Python classes. 
# Class-based views offer a more structured way to organize your view logic and promote code reuse through inheritance.

# 6. **URL Mapping**: Once defined, the view functions or class-based views in `views.py` need to be mapped to specific URL patterns in your 
# Django application. This is typically done in the `urls.py` module using URL patterns defined with `path()` or `re_path()` functions.

# In summary, `views.py` serves as the central location for defining the logic to handle incoming HTTP requests, process data, and generate 
# appropriate HTTP responses in a Django web application.

# db.sqlite3

# In Django, `db.sqlite3` is a database file that is automatically created when you start a new Django project. Here's a simple explanation of its 
# usage:

# 1. **Database Storage**: `db.sqlite3` serves as the default database for your Django project. It stores all the data related to your application, 
# including models, user information, and any other data that your application needs to persist.

# 2. **SQLite Database**: By default, Django uses SQLite as its database engine for development purposes. SQLite is a lightweight, file-based 
# database engine that doesn't require a separate server process, making it convenient for development and testing.

# 3. **Data Schema**: When you define models in your Django application using Python classes, Django automatically creates corresponding database 
# tables in `db.sqlite3`. Each model class represents a table in the database, and each instance of the model represents a row in that table.

# 4. **Migrations**: As you make changes to your models over time, such as adding new fields or modifying existing ones, Django generates database 
# migration files to apply those changes to the database schema. These migration files are stored in the `migrations` directory of your Django app 
# and are used to keep the database schema in sync with your models.

# 5. **Development and Testing**: During development and testing of your Django application, `db.sqlite3` is used as the database backend by 
# default. It provides a simple and portable way to work with your application's data without the need for additional configuration.

# 6. **Production Deployment**: In production environments, you may choose to use a different database backend such as PostgreSQL, MySQL, or Oracle. 
# In such cases, you would configure Django to use the appropriate database engine, and `db.sqlite3` would no longer be used.

# In summary, `db.sqlite3` is the default SQLite database file used by Django for development and testing purposes. It stores the data for your 
# Django application and is managed automatically by Django's ORM (Object-Relational Mapping) system.

# from .views import firstView->(yaani ki isey folder ke views mai se import karo firstView naam ke function ko)

