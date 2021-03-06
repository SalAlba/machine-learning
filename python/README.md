# Learn Python
[![License](https://img.shields.io/github/license/salalba/matplotlib)](https://github.com/SalAlba/matplotlib/blob/master/LICENSE)
This project aims to introduce the Python programming language,we will go deep and explore python features.
:warning: information/data in `<` `>` should be changed :warning:

## Authors

* **Salem Albarudy** - [Website](salem-albarudy.com) | [GitHub](https://github.com/salalba) | [Linkedin](https://linkedin.com/in/salem-albarudy/)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


## Table of contents
+ [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
+ [Install python](#Install-python)
  - [Linux/Ubuntu](#)
  - [MacOS](#)
  - [Windows](#)
+ [Virtual environment](#Virtual-environment)
+ [Install packages](#Install-packages)
  - [Pip](#)
  - [Conda](#)
+ [Quick start](#Quick-start)
+ [Scalar types](#Scalar-types)
+ [Lists, Tuples, Dictionaries.](#Lists-Tuples-Dictionaries)
+ [...](#)
+ [...](#)
+ [...](#)
+ [...](#)
+ [...](#)
+ [...](#)
+ [...](#)
+ [...](#)
+ [License](#License)
+ [Resources](#Resources)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
+ machine with operating system best choices (Linux/Ubuntu).
+ Python >= 3.*.
+ pip3.

> :warning: information/data in `<` `>` should be changed :warning:

### Installing

A step by step series of examples that tell you how to get a development env running

1. clone the repo to your local machine using

``` repo
    $ git https://github.com/SalAlba/machine-learning.git
    $ cd machine-learning
```

## Install Python

### Check Python version

**Linux/Ubuntu** open the terminal and print, in case if you don't have any information print it mean your machine don't have any python version and you have to install one :smile:.

``` bash
  $ python --version
  # output >> Python 3.8.5
```

check where is installed

``` bash
  $ whereis python

  # output
  # python: 
  #   /usr/bin/python2.7
  #   /usr/bin/python
  #   /usr/bin/python3.8-config
  #   /usr/bin/python3.8
  #   /usr/bin/python2.7-config
  #   /usr/lib/python2.7
  #   /etc/python2.7
  #   /etc/python3.8
  #   /usr/local/lib/python2.7
  #   /usr/local/lib/python3.8
  #   /usr/include/python3.8
```


**MacOs** open the terminal and print, in case if you don't have any information print it mean your machine don't have any python version and you have to install one :smile:.

``` bash
  $ python --version
  # output >> Python 3.8.5
```

**Windows** open the CMD (command line),  in case if you don't have any information print it mean your machine don't have any python version and you have to install one :smile:.

``` bash
  > python --version
  # output >> Python 3.8.5
```

## Virtual environment

### First way [Linux/Ubuntu][MacOS][Windows]
:warning: You should have installed a Python version on your machine, if have install just conda on machine could be not enough for some operating system like windows. to be sure you have to [check Python version](#check-Python-version)

``` bash
  $ python -m venv <VIRTUAL_ENVIRONMENT_NAME>

  # ex.
  $ python -m venv venv
  $ python -m venv my_env
```

activate/deactivate virtual environment on `linux`&`macOS`
``` bash
  $ source path/to/my_env/bin/activate

  # ex.
  $ source venv/bin/activate
  
  $ deactivate
```

activate/deactivate virtual environment on `windows`
``` bash
  $ path/to/my_env/Script/activate

  # ex.
  $ source venv/Script/activate
  
  $ deactivate
```

### Second way using anaconda [Linux/Ubuntu][MacOS][Windows]

open anaconda prompt and do the stuff bellow.

> By default, environments are installed into the envs directory in your conda directory.

``` bash
  $ conda create --name <VIRTUAL_ENVIRONMENT_NAME>

  # ex.
  $ conda create --name my_env_name
```

To create an environment with a specific version of Python.

``` bash
  $ conda create -n my_env_name python=3.6
```

Specifying a location for an environment.

``` bash
  $ conda create --prefix ./my_env_name
```


activate/deactivate virtual environment on `linux`&`macOS`&`windows`
``` bash
  $ conda activate <VIRTUAL_ENVIRONMENT_NAME>

  # ex.
  $ conda activate my_env_name
  
  $ conda deactivate
```


## Install packages
A python package is a collection of modules. Modules that are related to each other are mainly put in the same package. When a module from an external package is required in a program, that package can be imported and its modules can be put to use. [[2.5.]](#Resources)

> Any Python file, whose name is the module’s name property without the .py extension, is a module.

### pip. PyPI
pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes. [[2.6.]](#Resources)

+ [pip - The Python Package Installer :heart:](https://pip.pypa.io/en/stable/)
+ [Installation](https://pip.pypa.io/en/stable/installing.html)
+ [Usage](https://pip.pypa.io/en/stable/)

To install python package 

:warning: information/data in `<` `>` should be changed :warning:

``` bash
  $ pip install <PACKAGE_NAME>
  [...]
  Successfully installed PACKAGE_NAME

  # ex. of installing package pandas
  $ pip install pandas

  $ pip install PACKAGE_NAME            # latest version
  $ pip install PACKAGE_NAME==1.0.4     # specific version
  $ pip install 'PACKAGE_NAME>=1.0.4'   # minimum version
  $ pip install -r requirements.txt     # requirements files
```

Install python package from file, This is useful if the target machine does not have a network connection:

``` bash
  $ pip install <PACKAGE_NAME.whl>
  [...]
  Successfully installed PACKAGE_NAME
```

> TODO install python package without network and with multi relation with another packages
> TODO install python package on Linux user account don't have permission


show list of all packages installed 
``` bash
  $ pip list
  $ pip list --outdated
```

Show what files were installed:
``` bash
  $ pip show <PACKAGE_NAME>

  $ pip show --files <PACKAGE_NAME>
```

Upgrade a package:
``` bash
  $ pip install --upgrade <PACKAGE_NAME>
```

Uninstall a package:
``` bash
  $ pip uninstall <PACKAGE_NAME>
```


### Conda

``` bash
  $ conda install <PACKAGE_NAME>
  [...]
  Successfully installed PACKAGE_NAME

  # ex. of installing package pandas
  $ conda install pandas
```

Install python package from file, This is useful if the target machine does not have a network connection:

``` bash
  $ conda install <PACKAGE_NAME.whl>
  [...]
  Successfully installed PACKAGE_NAME
```

> TODO install python package without network and with multi relation with another packages


show list of all packages installed 
``` bash
  $ conda list
```

Show what files were installed:
``` bash
  $ conda show <PACKAGE_NAME>
```

Upgrade a package:
``` bash
  $ conda install --upgrade <PACKAGE_NAME>
```

Uninstall a package:
``` bash
  $ conda uninstall <PACKAGE_NAME>
```

In case you have user account on linux machine with limit permissions do this
``` bash
  $ cd ~
  $ /opt/anaconda3/bin/conda create -n my_root --clone=/opt/anaconda3
  $ ~/.conda/envs/my_root/bin/python
  $ ~/.conda/envs/my_root/bin/conda install pandas
  $ ~/.conda/envs/my_root/bin/conda update --all
```  

## Quick start

[**Scalar types**](#Scalar-types) Scalar types, have integers (ex. 1, 5, -12), float numbers (ex. 3.14, $5e^{-16} = 5 . 10^{-16}$), strings (ex. 'hi there') and boolean variables (True, False)


[**Variables**](#) we can use variables to store different (any) values like numbers, strings, objects, we create variables using operator equal `=`, ex. below show how to create variable called `x` storing integer value.

``` python
x = 2
print(x)
print(x + 3)
```


> A variable name must start with a letter or the underscore character

> A variable name cannot start with a number

> A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

> Variable names are case-sensitive (age, Age and AGE are three different variables)


[**Strings**](#) are sequences of characters, in Python3 case they are full Unicode.

``` python

str1 = "Hi There!"

str2 = 'Hi There!'

str3 = '''
  Hi there
  What to do      
  '''

str4 = """
  Hi there
  What to do      
  """

print(str1)
print(str2)
print(str3)
print(str4)
```


[**Lists, Tuples, Dictionaries.**](#Lists-Tuples-Dictionaries) objects which can store collections

**Lists**
``` python

list_a = [1,2,3]
print(list_a)

list_b = [1,'a',3, 'd']
print(list_b)
```

**Tuples**
``` python

# ex.1.
tuple_a = 1, 2, 3
print(tuple_a)

# ex.2.
tuple_b = (1, 2, 3)
print(tuple_b)

```

**list vs tuple**
> list are mutable (we can change the values in list).

> tuple are immutable (we can't change the values in tuple).

``` python

# lists
list_a = [1,2,3]
print(list_a[1])  # 2
list_a[1] = 55    # mutable
print(list_a[1])  # 5


# tuples
tuple_a = 1, 2, 3
print(tuple_a[1]) # 2
# tuple_a[1] = 55 # immutable
# print(tuple_a[1])

# TypeError: 'tuple' object does not support item assignment

```

**Dicts**
``` python
dict_a = {
  'key_1': 'value_1',
  'key_2': 2,
  'key_3': True,
  'key_4': [],
  'key_5': {},
  'key_6': (),
  'key_7': object,
  'key_8': None,
  9: 9,
  10: 10,
}

print(dict_a)
```

**Sets**
```python
set_a = {'ada', 1, 'ada', 9, False, 'b'}
print(set_a)
```

> sets save just the unique values, in ex. above will be just one `ada`.

[**Control Flow**](#)
```python
x = 2
if x > 1:
  print('more than 1')

if x == 1:
  print('equal 1')
else:
  print('not equal')
```

[**loops**](#)
``` python
for i in range(4):
  print(i)
```

``` python
for i in [4,6,8,9]:
  print(i)
```

``` python
x = 3
while x > 0:
  print(x)
  x -= 1
```

[**Functions**](#)
``` python
def func_1():
  print('Hi there')

func_1()
```

```python
def pow_2(arg1):
  return arg1**2

r = pow_2(4)
print(r)
```

```python
def sum(arg1, arg2):
  return arg1 + arg2

r = sum(3,6)
print(r)
```

```python
def func_2(arg1, arg2, *args, **kwargs):
  print(arg1)
  print(arg2)
  print(args)
  print(kwargs)


func_2('ada', 33)

func_2('ada', 33, False, 44)

func_2('ada', 33, show=False, age=44)

```
## Scalar types
<!-- 

https://stackoverflow.com/questions/30340555/are-numbers-considered-objects-in-python

https://stackoverflow.com/questions/15376509/when-is-i-x-different-from-i-i-x-in-python/15376520#15376520

https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/
 -->

A scalar is a type that can have a single value such as 42, 3.14, or 'Hi there'. 

The commonly used scalar types in Python are:

* int : Any integer.

* float : Floating point number (64 bit precision).

* complex : Numbers with an optional imaginary component.

* bool : True, False.

* str : A sequence of characters (can contain unicode characters).

* bytes : A sequence of unsigned 8-bit entities, used for manipulating binary data.

* NoneType (None) : Python's null, every instance of None is of NoneType.

> Python doesn't have  primitive types, every type is an object.



``` python

int_ = 123
float_ = 3.14
complex_ = 1 + 2j
str_ = 'Salem'
bool_ = True
none_ = None


print(int_)
print(type(int_)) #  <class 'int'>
print('Is object :', isinstance(int_, object)) # True
print()


print(float_)
print(type(float_)) # <class 'float'>
print('Is object :', isinstance(float_, object)) # True
print()

print(complex_)
print(type(complex_)) # <class 'complex'>
print('Is object :', isinstance(complex_, object)) # True
print()


print(str_)
print(type(str_)) # <class 'str'>
print('Is object :', isinstance(str_, object)) # True
print()


print(bool_)
print(type(bool_)) # <class 'bool'>
print('Is object :', isinstance(bool_, object)) # True
print()


print(none_)
print(type(none_)) # <class 'NoneType'>
print('Is object :', isinstance(none_, object)) # True
print()

```

### Operators
quick view of operations can be done on types.

**Assignment**
we use for that the equal symbol `=`.

``` python

# name_of_var = some_value

a = 12

```

**Arithmetic Operators**

``` python

'''
+    Addition
-    Subtraction
*    Multiplication
/    Division
//   Floor Division
%    Modulo
**   Power
'''

print(1 + 2)
print(3.14 + 5)

print(5 - 3)
print(2 - 3.14)

print(6 * 2)

print(2 ** 3)
print(4 ** 2)

print(4/2)
print(8/4)

print(4//2)
print(8//3)

print(4%2)
print(4%3)
print(2%4)
print(1%4)
print(3%4)

```


more about modulo

``` python
# https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/

print('0%3 : ', 0%3)
print('1%3 : ', 1%3)
print('2%3 : ', 2%3)
print('3%3 : ', 3%3)
print('4%3 : ', 4%3)
print('5%3 : ', 5%3)
print('6%3 : ', 6%3)
print('7%3 : ', 7%3)
print('8%3 : ', 8%3)

print()
print('-0%3 : ', -0%3)
print('-1%3 : ', -1%3)
print('-2%3 : ', -2%3)
print('-3%3 : ', -3%3)
print('-4%3 : ', -4%3)
print('-5%3 : ', -5%3)
print('-6%3 : ', -6%3)
print('-7%3 : ', -7%3)
print('-8%3 : ', -8%3)
```


where can we use modulo

``` python

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

print(days[ (1) % len(days) ])
print(days[ (7) % len(days) ])
print(days[ (6) % len(days) ])

print(days[ (6+1) % len(days) ]) # Sun + 1 = Mon
print(days[ (6+3) % len(days) ]) # Sun + 3 = Wed

print(days[ (1-1) % len(days) ]) # Tue - 1 = Mon
print(days[ (1-5) % len(days) ]) # Tue - 5 = Fri
print(days[ (1-14) % len(days) ]) # Tue - 14 = Tue
print(days[ (1-15) % len(days) ]) # Tue - 15 = Mon

```


**Comparison Operators**
``` python

'''

==   Equal To
>    Greater Than
>=   Greater Than or Equal To
<    Less Than
<=   Less Than or Equal To
!=   Not Equal

'''

print(4 == 4)
print(3 == 1)
print(True == False)
print(3.14 == 3.14)
print(1 == 1.0)

print(1 < 1.0)
print(True > False)


print( 1 < 2 < 3)
print( 5 >= 4 == 4)

```

**Boolean Operators**
``` python
and
or
not
```

```

-----------------------------------
and
-----------------------------------
a       b       | q
-----------------------------------
True    True    | True
True    False   | False
False   True    | False
False   False   | False



-----------------------------------
or
-----------------------------------
a       b       | q
-----------------------------------
True    True    | True
True    False   | True
False   True    | True
False   False   | False



-----------------------------------
not
-----------------------------------
a      | q
-----------------------------------
True    | False
False   | True


```

### Converting types 


``` python

int_ = 1
float_ = 1.0
complex_ = 1 + 0j
str_ = 'Salem'
bool_ = True
none_ = None


print(int(int_))      # 1
print(float(int_))    # 1.0
print(complex(int_))  # (1+0j)
print(str(int_))      # '1'
print(bool(int_))     # True
print(bool(0))        # False
print()

print(int(float_))      # 1
print(float(float_))    # 1.0
print(complex(float_))  # (1+0j)
print(str(float_))      # 1.0
print(bool(float_))     # True
print(bool(0.0))        # False
print()

# print(int(complex_))      # TypeError: can't convert complex to int
# print(float(complex_))    # TypeError: can't convert complex to float
print(complex(complex_))  # (1+0j)
print(str(complex_))      # (1+0j)
print(bool(complex_))     # True
print(bool((0+0j)))       # False
print()

# print(int(str_))      # ValueError: invalid literal for int() with base 10: 'Salem'
# print(float(str_))    # ValueError: could not convert string to float: 'Salem'
# print(complex(str_))  # ValueError: complex() arg is a malformed string
print(int('1'))        # 1
print(float('1'))      # 1.0
print(complex('1'))    # (1+0j)
print(str(str_))        # Salem
print(bool(str_))       # True
print(bool(''))         # False
print()

print(int(True))      # 1
print(float(True))    # 1.0
print(complex(True))  # (1+0j)
print(str(True))      # True
print(bool(True))     # True
print()

print(int(False))      # 0
print(float(False))    # 0.0
print(complex(False))  # (0+0j)
print(str(False))      # False
print(bool(False))     # False
print()

# print(int(none_))      # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
# print(float(none_))    # TypeError: float() argument must be a string or a number, not 'NoneType'
# print(complex(none_))  # TypeError: complex() first argument must be a string or a number, not 'NoneType'
print(str(none_))      # 'None'
print(bool(none_))     # False
print()

```


> help(str)
> help(int)


**Replace values**
``` python

# ...
a = 2
b = 3

tmp = a
a = b
b = tmp


# ...
a = 2
b = 3
b, a = a, b
```


## Lists, Tuples, Dictionaries.
TODO ...


## License
[![License](https://img.shields.io/github/license/salalba/matplotlib)](https://github.com/SalAlba/matplotlib/blob/master/LICENSE)

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details, Copyright 2020 © <a href="https://github.com/SalAlba/" target="_blank">Salem Albarudy</a>.


## Resources

### 1. Books
+ [[1.0.] ...](#)
+ [[1.1.] Przetwarzanie i analiza danych w języku python](#)
  - [Helion](https://helion.pl/ksiazki/przetwarzanie-i-analiza-danych-w-jezyku-python-marek-gagolewski-anna-cena-maciej-bartoszuk,e_17yd.htm#format/e)
  - [PWN](https://ksiegarnia.pwn.pl/Przetwarzanie-i-analiza-danych-w-jezyku-Python,634359876,p.html)
+ [[1..] ...](#)

### 2. Websites
+ [[2.0.] ...](#)
+ [[2.1.] Python's documentation](https://www.python.org/doc/)
+ [[2.2.] Python Notes](https://jpt-pynotes.readthedocs.io/en/latest/index.html)
+ [[2.3.] Learn Python Programming](https://www.programiz.com/python-programming)
+ [[2.5.] What are Python packages?](https://www.educative.io/edpresso/what-are-python-packages)
+ [[2.6.] pip. PyPI](https://pypi.org/project/pip/)


### 3. Youtube
+ [[3.0.] Owner of the chanel | Chanel name | Tutorial name ](#)

### 4. Papers
+ [[4.0] ... ](#)

