String Data Type
Python Strings are arrays of bytes representing Unicode characters. In Python, there is no character data type, a character is a string of length one. It is represented by str class.

Strings in Python can be created using single quotes, double quotes or even triple quotes. We can access individual characters of a String using index.




s = 'Welcome to the Geeks World'
print(s)
​
# check data type 
print(type(s))
​
# access string with index
print(s[1])
print(s[2])
print(s[-1])

Output
Welcome to the Geeks World
<class 'str'>
e
l
d
List Data Type
Lists are similar to arrays found in other languages. They are an ordered and mutable collection of items. It is very flexible as items in a list do not need to be of the same type.

Creating a List in Python

Lists in Python can be created by just placing sequence inside the square brackets[].




# Empty list
a = []
​
# list with int values
a = [1, 2, 3]
print(a)
​
# list with mixed values int and String
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

Output
[1, 2, 3]
['Geeks', 'For', 'Geeks', 4, 5]
Access List Items

In order to access the list items refer to index number. In Python, negative sequence indexes represent positions from end of the array. Instead of having to compute offset as in List[len(List)-3], it is enough to just write List[-3]. Negative indexing means beginning from end, -1 refers to last item, -2 refers to second-last item, etc.




a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])
​
print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])

Output
Accessing element from the list
Geeks
Geeks
Accessing element using negative indexing
Geeks
Geeks
Tuple Data Type
Tuple is an ordered collection of Python objects. The only difference between a tuple and a list is that tuples are immutable. Tuples cannot be modified after it is created.

Creating a Tuple in Python

In Python, tuples are created by placing a sequence of values separated by a ‘comma’ with or without the use of parentheses for grouping data sequence. Tuples can contain any number of elements and of any datatype (like strings, integers, lists, etc.).

Note: Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple. 




# initiate empty tuple
tup1 = ()
​
tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)

Output
Tuple with the use of String:  ('Geeks', 'For')
Note  - The creation of a Python tuple without the use of parentheses is known as Tuple Packing. 

Access Tuple Items

In order to access tuple items refer to the index number. Use the index operator [ ] to access an item in a tuple.




tup1 = (1, 2, 3, 4, 5)
​
# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

Output
1
5
3
