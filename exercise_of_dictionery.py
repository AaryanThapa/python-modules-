set = ("A set is a collection of object")
mutable = ("Which can be changed. for  example:list,dictionery")
immutable = ("Which cannot be changed.for example:Tuple")

input = int(input("Enter the word:"))

if input == "set":
    print(set)
elif input == "mutable":
    print(mutable)
elif input == "immutable":
    print(immutable)
else:
    print("Sorry!!! word not found")