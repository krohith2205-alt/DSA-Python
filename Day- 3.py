'''python project---> POP / OOP ---> DSA (Logic Based --> Pattern based --> Platform)

POP(Procedure Oriented Programming): Dividing the entire code into

blocks: procedure --> Functions (def)

Functions --> A reusable block of code (or) A block of statements which performs a specific task

Syntax:

def <funcname>(parameters):
    """ Doc String"""
    statement(s)...
    ..............      # body of func
    return value(s)...
fname(args) # func call    '''

# Simple scenario to understand

def add(a,b):
    """Addition Function"""
    c= a+b
    return c  #addition
print(add(4,6))
c,d= 'codegnan','python'
print(add(c,d))  # concatenation
e,f= map(input("Enter the values").split(','))
print(add(e,f))
print(add[1,3,4],[4,6,7]) # merging
print(add(1,2,3,4)) # positional arguments fail    

# Variable length arguments: *args we can pass any number of positional

#arguments: data will be stored in tuple...()

def sample(*a):
    """Demo of variable length arguments"""
    print(a)
    print(type(a))  # default it stores in tuple format
sample()
sample(2,3,4,5)
sample('codegnan',[1,23,5],'rohith',2+5j)

marks= [20,15,22,31]
sample(marks)
sample(*marks)
a,*b,c= 12,'code','poll',23,4,8
print(a)
print(b)
print(c)  

def add(*a):
    """perform addition for numeric values"""
    print(a)
    result= 0
    for i in a:
        #print(i)
        result= result + i
    return result
print(add(2,3,4))
print(add(2,'codegnan',3,4))  

# Keyword arguments: we can pass the name for the arguments

def batch(name,age,place="vizag"):
# def batch(name="rohith",age,place='Andhra Pradesh'): # error: non default always follows
    """keyword arguments usage"""
    print(f'{name} is in {place} and age is {age} years')
batch('Codegnan',1,'Vizag')
batch(place='Andhra Pradesh',name='Codegnan',age=22)
# keyword arguments only needs name matching not order
batch(name='rohith',age=25)
# default arguments can accept a value as default    

print(4,5)
print(4,5,sep=':') #here keyword argument is sep and we are changing
# the default value for sep

# keyword variable length arguments (**kwarngs) any number of

# keyword arguments, data is stored in dictionary 

def batch(**a):
    """keyword variable length arguments usage"""
    print(a)
    print(type(a))
batch()
batch(name="rohith",age=22,place="Visakapatnam",branch="ECE")

data={'names':['shanthi','kamala'],
      'place':['Visakhapatnam','Narsipatnam']}
# batch(**data)
data.update({'batch':'PFS-VSP-004'})
batch(**data)

# Task: Create a function with the usage of *args and **kwargs

'''
def gn(*a,**b):
    ....
    ......
'''
