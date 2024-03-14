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
# isme ek senctence ke baad uske aagai sentence aayega.
# file=open("file handling/first.txt","a")
# file.write("this is write mode text")
# file.close()
# Output:this is write mode textmy name is zaidthis is write mode text
