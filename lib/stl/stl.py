def q1(value):
    #  abs(value) 
    #method returns the absolute value of the given number. 
    #If the number is a complex number, abs() returns its magnitude.
    
    """
    Paramaters:
    (int)
    (float)
    (complex)
    

    Return:
    For integers - integer absolute value is returned
    For floating numbers - floating absolute value is returned
    For complex numbers - float magnitude of the number is returned

    complex = (3 - 4j)

    """
    print(abs(value))


def q2(iterable):
    """
    any(iterable)

    function returns True if any element of an iterable is True. If not, any() returns False.
    
    Param:
    function takes an iterable (list, string, dictionary etc.) in Python.
    
    Return:
    True, if at least one element of an iterable is true
    False, if all elements are false or if an iterable is empty

    """
    print(any(iterable))

def q3(iterable):
    """
    all(iterable)
    
    function returns True if all elements in the given iterable are true. If not, it returns False.

    Param:
    iterable

    Return:
    True - If all elements in an iterable are true (or empty iterable)
    False - If any element in an iterable is false

    """

    print(all(iterable))

def q4():
    """
    ascii(object)

    method returns a string containing a printable representation of an object. 
    It escapes the non-ASCII characters in the string using escapes.

    Param:
    object

    Return:
    A string containing a printable representation of an object.
    """
    s1= 'python'
    s2= 'pythön'
    s3= 'Pyth\xf6n'

    print(s1)
    print(s2)
    print(s3)

    print("*----*")

    print(ascii(s1))
    print(ascii(s2))
    print(ascii(s3))

def q5(integer):
    """
    bin(int)
    
    method converts and returns the binary equivalent string of a given integer.

    Param:
    int

    Return:
    method returns the binary (string) equivalent to the given integer.

    """
    print('The binary equivalent of 5 is:', bin(integer))

def q6(value):
    """
    bool(value)
    method converts a value to Boolean (True or False) using the standard truth testing procedure.

    Param:
    In general use, bool() takes a single parameter (value).
    If you do not pass a value, bool() returns False.

    Return:
    False if the value is false or omitted
    True if the value is true

    """
    print(bool(value))

def q7():
    """
    bytearray(source, encoding, errors)
    returns a bytearray object which is an array of the given bytes.

    Param:
    takes 3 optional parameters:
    source (Optional) - source to initialize the array of bytes.
    encoding (Optional) - if the source is a string, the encoding of the string.
    errors (Optional) - if the source is a string, the action to take when the encoding conversion fails

    """
    pass

def q8(obje):
    """
    callable(object)
    returns True if the object passed appears callable. If not, it returns False.
    
    Param:
    object

    Return:
    True - if the object appears callable
    False - if the object is not callable.

    """
    print(callable(obje))

def q9():
    """
    bytes(source, encoding, errors)
    returns a immutable bytes object initialized with the given size and data.
    If you want to use the mutable version, use bytearray() method.

    Param:
    source (Optional) - source to initialize the array of bytes.
    encoding (Optional) - if the source is a string, the encoding of the string.
    errors (Optional) - if the source is a string, the action to take when the encoding conversion fails

    """

def q10(integer):
    """
    chr(int)
    returns a character (a string) from an integer (represents unicode code point of the character).

    Param:
    int

    Return:
    a character (a string) whose Unicode code point is the integer i
    If the integer i is outside the range, ValueError will be raised.

    """
    print(chr(integer))

def q11():
    """
    compile()
    method returns a Python code object from the source (normal string, a byte string, or an AST object).

    Ex.

    'sumstring' file from which the code was read. If it wasn't read from a file, you can give a name yourself

    codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
    codeObejct = compile(codeInString, 'sumstring', 'exec')

    exec(codeObejct)
    

    Output

    sum = 11

    """
    pass

def q12():
    """
    exec()
    method executes the dynamically created program, which is either a string or a code object.

    Ex 1
    program = 'a = 5\nb=10\nprint("Sum =", a+b)'
    exec(program)
    
    Output

    Sum = 15
    
    Ex 2 Allow user to provide input
    program = input('Enter a program:')
    exec(program)

    Enter a program: [print(item) for item in [1, 2, 3]]
    1
    2
    3

    """
    pass

def q13():
    """
    classmethod()
    method returns a class method for the given function.
    classmethod() is considered un-Pythonic so in newer Python versions, 
    you can use the @classmethod decorator for classmethod definition.

    @classmethod
    def func(cls, args...)

    Ex 1

    class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

    # create printAge class method
    Person.printAge = classmethod(Person.printAge)
 
    Person.printAge()


    Output 

    The age is: 25

    """
    pass

def q14():
    """
    complex()
    method returns a complex number when real and imaginary parts are provided, or it converts a string to a complex number.
    
    Param:
    real - real part. If real is omitted, it defaults to 0.
    imag - imaginary part. If imag is omitted, it defaults to 0.

    Return:
    As suggested by the name, complex() method returns a complex number.

    If the string passed to this method is not a valid complex number, ValueError exception is raised.
    """

    # Ex 1

    z = complex(2, -3)
    print(z)
            
    z = complex(1)
    print(z)
            
    z = complex()
    print(z)
            
    z = complex('5-9j')
    print(z)
    """


    Ex 2

    a = 2+3j
    print('a =',a)
    print('Type of a is',type(a))

    b = -2j
    print('b =',b)
    print('Type of b is',type(a))

    c = 0j
    print('c =',c)
    print('Type of c is',type(c))


    """

def q15():
    """
    delattr() 
    deletes an attribute from the object (if the object allows it).

    Param:
    object - the object from which name attribute is to be removed
    name -  a string which must be the name of the attribute to be removed from the object

    Return:
    delattr() doesn't return any value (returns None). It only removes an attribute (if the object allows it).
    """

    class Coordinate:
      x = 10
      y = -5
      z = 0

    point1 = Coordinate() 

    print('x = ',point1.x)
    print('y = ',point1.y)
    print('z = ',point1.z)

    #delattr(Coordinate, 'z')

    # !!!! You can also delete attribute of an object using "del" operator.

    del Coordinate.z

    print('--After deleting z attribute--')
    print('x = ',point1.x)
    print('y = ',point1.y)

    # Raises Error
    print('z = ',point1.z)
    # # Output
    # x =  10
    # y =  -5
    # z =  0
    # --After deleting z attribute--
    # x =  10
    # y =  -5
    # Traceback (most recent call last):
    #   File "python", line 19, in <module>
    # AttributeError: 'Coordinate' object has no attribute 'z'

def q16():
    """
    dict()
    constructor creates a dictionary in Python.

    Param:
    dict(**kwarg)
    dict(mapping, **kwarg)
    dict(iterable, **kwarg)

    Return:
    doesn't return any value (returns None).

    """
 
    # # Ex 1 Create Dictionary Using keyword arguments only
    # numbers = dict(x=5, y=0)
    # print('numbers =', numbers)
    # print(type(numbers))

    # empty = dict()
    # print('empty =', empty)
    # print(type(empty))

    
    # # Ex 2 Create Dictionary Using Iterable
    # # keyword argument is not passed
    # numbers1 = dict([('x', 5), ('y', -5)])
    # print('numbers1 =',numbers1)

    # # keyword argument is also passed
    # numbers2 = dict([('x', 5), ('y', -5)], z=8)
    # print('numbers2 =',numbers2)

    # # zip() creates an iterable in Python 3
    # numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
    # print('numbers3 =',numbers3)

    
    # Ex 3 Create Dictionary Using Mapping
    numbers1 = dict({'x': 4, 'y': 5})
    print('numbers1 =',numbers1)

    # you don't need to use dict() in above code
    numbers2 = {'x': 4, 'y': 5}
    print('numbers2 =',numbers2)

    # keyword argument is also passed
    numbers3 = dict({'x': 4, 'y': 5}, z=8)
    print('numbers3 =',numbers3)

def q17():
    """
    dir()
    method tries to return a list of valid attributes of the object.

    Param:
    object (optional) - dir() attempts to return all attributes of this object.
    
    Return:
    If the object has __dir__() method, the method will be called and must return the list of attributes.
    
    If the object doesn't have __dir__() method, this method tries to find information from the __dict__ attribute (if defined), and from type object. In this case, the list returned from dir() may not be complete.
    
    If an object is not passed to dir() method, it returns the list of names in the current local scope.

    """

    # # Ex 1
    # number = [1, 2, 3]
    # print(dir(number))

    # print('\nReturn Value from empty dir()')
    # print(dir())

    """
    ['__add__', '__class__', '__contains__', '__delattr__', 
    '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', 
    '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', 
    '__iadd__', '__imul__', '__init__', '__init_subclass__', 
    '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__',
    '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
    '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', 
    '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 
    'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

    Return Value from empty dir()
    ['__annotations__', '__builtins__', '__doc__', '__loader__', 
    '__name__', '__package__', '__spec__', 'number']

    """

    class Person:
      def __dir__(self):
        return ['age', 'name', 'salary']
      
      def ass(self):
        print("ass")

    teacher = Person()
    print(dir(teacher))

    """
    ['age', 'name', 'salary']

    """
def q18():
    """
    divmod()
    method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
    
    Param:
    x - a non-complex number (numerator)
    y - a non-complex number (denominator)

    Return:
    (q, r) - a pair of numbers (a tuple) consisting of quotient q and remainder r

    If x and y are integers, the return value from divmod() is same as (a // b, x % y).
    If either x or y is a float, the result is (q, x%y). Here, q is the whole part of the quotient.

    """
    print('divmod(8, 3) = ', divmod(8, 3))
    print('divmod(3, 8) = ', divmod(3, 8))
    print('divmod(5, 5) = ', divmod(5, 5))

    # divmod() with Floats
    print('divmod(8.0, 3) = ', divmod(8.0, 3))
    print('divmod(3, 8.0) = ', divmod(3, 8.0))
    print('divmod(7.5, 2.5) = ', divmod(7.5, 2.5))
    print('divmod(2.6, 0.5) = ', divmod(2.6, 0.5))

    # Output
    """
    divmod(8, 3) =  (2, 2)
    divmod(3, 8) =  (0, 3)
    divmod(5, 5) =  (1, 0)
    divmod(8.0, 3) =  (2.0, 2.0)
    divmod(3, 8.0) =  (0.0, 3.0)
    divmod(7.5, 2.5) =  (3.0, 0.0)
    divmod(2.6, 0.5) =  (5.0, 0.10000000000000009)
    """

def q19():
    """
    enumerate()
                (sayaç)
    method adds counter to an iterable and returns it (the enumerate object).

    Param:
    iterable - a sequence, an iterator, or objects that supports iteration
    start (optional) - enumerate() starts counting from this number. If start is omitted, 0 is taken as start.

    Return:
    method adds counter to an iterable and returns it. The returned object is a enumerate object.
    You can convert enumerate objects to list and tuple using list() and tuple() method respectively.
    """
    


    # # Ex 1
    # grocery = ['bread', 'milk', 'butter']
    # enumerateGrocery = enumerate(grocery)

    # print(type(enumerateGrocery))

    # # converting to list
    # print(list(enumerateGrocery))

    # # changing the default counter
    # enumerateGrocery = enumerate(grocery, 10)
    # print(list(enumerateGrocery))

    """
    <class 'enumerate'>
    [(0, 'bread'), (1, 'milk'), (2, 'butter')]
    [(10, 'bread'), (11, 'milk'), (12, 'butter')]
    """

    # Ex 2 Looping Over an Enumerate object
    grocery = ['bread', 'milk', 'butter']

    for item in enumerate(grocery):
      print(item)

    print('\n')
    for count, item in enumerate(grocery):
      print(count, item)

    print('\n')
    # changing default start value
    for count, item in enumerate(grocery, 100):
      print(count, item)

    """
    (0, 'bread')
    (1, 'milk')
    (2, 'butter')

    0 bread
    1 milk
    2 butter

    100 bread
    101 milk
    102 butter
    """

def q20():
    """
    built-in function returns a static method for a given function.
    Using staticmethod() is considered a un-Pythonic way of creating a static function.

    Hence, in newer versions of Python, you can use the @staticmethod decorator.

    The syntax of @staticmethod is:

    @staticmethod
    def func(args, ...)
    
    Param:
    function - function that needs to be converted to a static method

    Return:
    returns a static method for a function passed as the parameter.
    """

    """
    What is a static method ? 

    Static methods, much like class methods, are methods that are bound to a "class" rather than its object.
    So, they are not dependent on the state of the object.

    The difference between a static method and a class method is:
    -Static method knows nothing about the class and just deals with the parameters.
    -Class method works with the class since its parameter is always the class itself.

    They can be called both by the class and its object.

    """

    # # Ex 1
    # class Mathematics:

    #     def addNumbers(x, y):
    #         return x + y

    # # create addNumbers static method
    # Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

    # print('The sum is:', Mathematics.addNumbers(5, 10))

    """
    The sum is: 15

    """


    """
    When do you use static methods?

    Static methods have a limited use case because, like class methods or any other methods within a class, 
    they cannot access the properties of the class itself.

    However, when you need a utility function that doesn't access any properties of a class 
    but makes sense that it belongs to the class, we use static functions.

    """

    # Ex 2  Create a utility function as a static method

    class Dates:
        def __init__(self, date):
            self.date = date

        def getDate(self):
            return self.date

        @staticmethod
        def toDashDate(date):
            return date.replace("/", "-")

    date = Dates("15-12-2016")
    dateFromDB = "15/12/2016"
    dateWithDash = Dates.toDashDate(dateFromDB)

    if(date.getDate() == dateWithDash):
        print("Equal")
    else:
        print("Unequal")

    # Equal

def q21():
    """
    filter()

    method filters the given iterable with the help of a function 
    that tests each element in the iterable to be true or not.

    Param:
    function -function that tests if elements of an iterable return true or false
            If None, the function defaults to Identity function - which returns false if any elements are false

    iterable

    """

    pass

def q22():
    """
    eval()

    function runs the python code 
    (which is passed as an argument) within the program.

    Param:
    expression - the string parsed and evaluated as a Python expression
    globals (optional) - a dictionary
    locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.

    """

    x = 1
    print(eval("x+1"))

def q23():
    """
    float()

    returns a floating point number from a number or a string.

    """

    print(type(float("23.4")))

def q24():
    """
    frozenset()

    """
    pass

def q25():
    """
    getattr()

    method returns the value of the named attribute of an object. 
    If not found, it returns the default value provided to the function.
    and returns an attribute error
    """

    class Person:
        age = 23
        name = "Adam"

    person = Person()

    # when default value is provided
    print('The sex is:', getattr(person, 'sex', 'Male'))

    # when no default value is provided
    print('The sex is:', getattr(person, 'sex'))

def q26():
    """
    globals()

    A symbol table is a data structure maintained by a compiler which contains all necessary information about the program.

These include variable names, methods, classes, etc.

There are mainly two kinds of symbol table.

    Local symbol table
    Global symbol table

Local symbol table stores all information related to the local scope of the program, and is accessed in Python using locals() method.

The local scope could be within a function, within a class, etc.

Likewise, a Global symbol table stores all information related to the global scope of the program, and is accessed in Python using globals() method.

The global scope contains all functions, variables that are not associated with any class or function.


    """
    pass

def q27():
    """
    exec()

    method executes the dynamically created program, which is either a string or a code object.

    """
    pass

def q28():
    """
    hasattr()

    method returns true if an object has the given named attribute and false if it does not.

    Param:
    object - object whose named attribute is to be checked
    name - name of the attribute to be searched

    Return:
    boolean
    """
    class Person:
        age = 23
        name = 'Adam'

    person = Person()

    print('Person has age?:', hasattr(person, 'age'))
    print('Person has salary?:', hasattr(person, 'salary'))

def q29():
    """
    help()

    method calls the built-in Python help system.

    Param:
        object (optional) - you want to generate the help of the given object

    """
    help(dict)


def q30():
    """
    hex()
    converts an integer number to the corresponding hexadecimal string.

    Param:
    int

    Return:
    The returned hexadecimal string starts with the prefix 0x 
    indicating it's in hexadecimal form.

    """

    print(hex(14))
q30()