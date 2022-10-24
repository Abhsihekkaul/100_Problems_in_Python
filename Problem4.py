'''
Question:
Write a program which accepts a sequence of comma-separated numbers from console and 
generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')'''


InputNumbers = input("Enter the numbers separated by commas : ")
if not InputNumbers:
    raise ValueError("You didn't input anything ")
ListForm = InputNumbers.split(",")
TupleForm = tuple(ListForm)
print(ListForm)
print(TupleForm)
