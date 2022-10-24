'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

'''
class PrintClass:
    def getstring(self,String1):
        self.String1 = String1
        return String1
    def printString(self):
        return print(self.String1)
def testClass():
    test = PrintClass()
    test.getstring(input("Enter a String : "))
    test.printString()

testClass()
