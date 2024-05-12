# Serialization:-
# import json

# data={'name':'john','age':30,'city':'New York'}
# json_string=json.dumps(data)
# print(json_string)
# Output:{"name": "john", "age": 30, "city": "New York"}

# import json

# data={'name':'john','age':30,'city':'New York'}
# json_string=json.dumps(data)
# print(type(json_string))
# Output:<class 'str'>

# This process is called as serialization.

# Deserialization:-:

import json
json_string='{"name":"john","age":30,"city":"New York"}'
data=json.loads(json_string)
print(data)
# Output:{'name': 'john', 'age': 30, 'city': 'New York'}
print(type(data))
# Output:<class 'dict'>

# Deserialization:iska matlab hai ki json ko convert karna python object mai.

# Python ke object ko json mai convert karna hai toh dumps used hota hai.
# json ko python ke object mai firse le aana.

# json se python mai convert kiya toh dictionary type aaya.
# json:it is a collection of key value pairs.