#######################################################
###
#######################################################

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # this also works --> Employee.__init__(self, first, last, pay)
        # super() keeps things simple
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())

dev_1 = Developer("Adam", "Damron", 50000, "Python")
dev_2 = Developer("Test", "Employee", 60000, "Java")

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

###
# Use these commands to get a True or False statement
#print(issubclass(Manager, Employee))
#print(isinstance(dev_1, Employee))
###

#print(mgr_1.email)

#mgr_1.add_emp(dev_2)
#mgr_1.remove_emp(dev_1)

#mgr_1.print_emp()

#print(dev_1.email)
#print(dev_1.prog_lang)

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)



#Cool command
#print(help(Developer))


#######################################################

'''

#######################################################
#
#######################################################

class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay @ self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

#######################################################
### This tutorial I lost at the end. He went on to describe static methods.
### As far as I know, static methods don't call the class in the method.
### @classmethod's are used to call the first argument into the function, aka Object(firstArgument)
### @staticmethod's are used to associate the method with the class but no need to call the class into the function
#######################################################



#######################################################
# Testing adding a second function, this time decreasing the price.
# Doing this to keep from having to look these commands up again and again.
#######################################################

class Pizza:

    num_of_pizzas = 0
    dec_amount = 1.50

    def __init__(self, topping, price):
        self.topping = topping
        self.price = price

        Pizza.num_of_pizzas += 1

    def fullPie(self):
        return "The {} pizza will cost you ${}".format(self.topping, self.price)

    def dec_price(self):
        self.price = int(self.price / self.dec_amount)
        
pie1 = Pizza('pepperoni', 20)
print(Pizza.fullPie(pie1))

print("Applying a 50% off coupon..")
pie1.dec_price()

print(Pizza.fullPie(pie1))

#Changing the value of the instanced's object's price
print("Applying a different coupon, 75% off..")
pie1.dec_amount = 1.75
pie1.dec_price()

#Printing out the new value of the first pizza
print(Pizza.fullPie(pie1))
print(Pizza.num_of_pizzas)

#Getting methods from the instance pie1 and from the object Pizza
#print(pie1.__dict__)
#print(Pizza.__dict__)


#######################################################
### 
#######################################################



#######################################################
# Adding a function to this one.
# It decreases the amount of the video game object, and prints it.
# Going to try it again on my own.
#######################################################

class Game:

    dec_amount = 1.25
    
    def __init__(self, name, genre, price):
        self.name = name
        self.genre = genre
        self.price = price

    def fullGame(self):
        return "It's {} for {} which is an {} game".format(self.price, self.name, self.genre)

    def price_dec(self):
        self.price = int(self.price/self.dec_amount)

game1 = Game("Halo", "Action", 60)
game2 = Game("Red Dead Redemption", "RPG", 70)

print(Game.fullGame(game1))
print(Game.fullGame(game2))

# Applying price_inc, giving them a discount
print(game1.price)
print("Applying discount, 25% off...")
game1.price_dec()
print(game1.price)



#######################################################
# I did it again!!
#######################################################

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person(self):
        return "{} is {} years old".format(self.name, self.age)

firstname = People("Adam", 32)
print(People.person(firstname))
print(firstname.person())
print(firstname.person())
#######################################################
### More practice. Seems like I've gotten it down.
#######################################################



#######################################################
# This time I'm creating a Pokemon. Giving him a name, a type, and a size.
# Practicing my Object creation. Passing traits to an instance of an object, and printing that.
#######################################################

class Pokemon:
    def __init__(self, name, ofType, size):
        self.name = name
        self.ofType = ofType
        self.size = size

    def pokemon(self):
        return "The {} Pokemon is a {} type and is usually {}-sized.".format(self.name, self.ofType, self.size)

poke1 = Pokemon("Pikachu", "Lightning", "small")
poke2 = Pokemon("Charmander", "Fire", "medium")
poke3 = Pokemon("Squirtle", "Water", "small")
poke4 = Pokemon("Onyx", "Rock", "extra large")
poke5 = Pokemon("Mewtwo", "?????", "medium")

print(Pokemon.pokemon(poke1))
print(Pokemon.pokemon(poke2))
print(Pokemon.pokemon(poke3))
print(Pokemon.pokemon(poke4))
print(Pokemon.pokemon(poke5))


#######################################################
### I DID IT!!
#######################################################
###
###
###

# So, here's what I do:

# 1. Create an object
        - give the object an uppercase name
        - use a semi-colon
        
# 2. First function is a constructor
        - put self as the first argument
        - then add argument names for each one you want to pass to the object
        - create self.whatever for each argument
        - DON'T pass self.self = self into the initializer/constructor
        
# 3. Second function is what I want to return
        - I put a function here that returns a value, so far just to print that instanced object

# 4. Create an instance
        - This will just be whatever = Object("I can pass all my arguments here ", "separated by comma's")
        
# 5. Print that instance
        - I use the print command, and in the parantheses I add the "super"-Object's name
        - Followed by the function inside the object that I want to use, so far I've only used return
        - Followed by the instance name that I created in the last step

###
###
###
#######################################################



#######################################################
# This is the first time I got it right without looking. I think.
# I'll do it one more time just to make sure. Want to make sure it sticks.
#######################################################

class Game:
    def __init__(self, name, genre, price):
        self.name = name
        self.genre = genre
        self.price = price

    def fullGame(self):
        return "It's {} for {} which is an {} game".format(self.price, self.name, self.genre)

game1 = Game("Halo", "Action", 60)
game2 = Game("Red Dead Redemption", "RPG", 75)

print(Game.fullGame(game1))
print(Game.fullGame(game2))
#######################################################
### This time I got it right. I printed the object, the method in the object, then the instance name. Obj.method(instance_name)
### Worked like a charm.
### Still, I need to learn arrays, because typing up each object and printing out each object is too long.
### This could be done with a loop, and the objects could be created easier somehow.
#######################################################



#######################################################
# Here I will try to recreate the Pizza object, without viewing other code.
# I will create a video game object.
#######################################################

class Game:
    def __init__(self, name, genre, price):
        self.name = name
        self.genre = genre
        self.price = price

    def fullGame(self):
        return '{} is an {} game that costs ${}.'.format(self.name, self.genre, self.price)



#This creates an instance of the Game object.
#Must create an instance of the object to give it attributes
game1 = Game("Halo", "FPS", 60)

#This doesn't work, because I'm just calling the Object and passing the instance into it.
#
#Game(game1())
#
#I need to tell the terminal to print, and to print the object, with the method, and the name of the instance I created

print(game1.name)
print(Game.fullGame(game1))
#######################################################
#What I forgot to do here was run the print command, pass the object into it, then the method, followed by the instance.
#Seems overcomplicated. I feel like there's an easier way.
#So, in retrospect, I can print the value of the instance object's name by typing print(instance_name.value_i_want)
print(game1.name)
#And also, I can print the returned object's function value by typing print(Object_Name.functionName(instance_name))
print(Game.fullGame(game1))
#######################################################



#######################################################
#This is me trying to copy code from Cody Schafer
#######################################################

class Pizza:
    def __init__(self, kind, size, price):
        self.kind = kind
        self.size = size
        self.price = price

    def fullPizza(self):
        return 'One {} {} pizza will cost {}'.format(self.size, self.kind, self.price)


pizza1 = Pizza("Pepperoni", "Large", "12.78")
pizza2 = Pizza("Supreme", "Large", "15.89")

#pizza1.fullPizza() <-- THIS DOES NOTHING??

#This prints the kind of pizza it is
print(pizza1.kind)

#This will pass the pizza1 elements into the object Pizza
#And will return with the fullPizza method
print(Pizza.fullPizza(pizza1))
print(Pizza.fullPizza(pizza2))

#######################################################
### I got stuck on the bottom. Getting the object to print has proven difficult.
### I should look into creating an array though, because typing 
#######################################################



#######################################################
#This one is from Cody Schafer's youtube. Python OOP Tutorial 1
#Works well, helps me understand initializing objects with a constructor
#and passing arguments to an object
#######################################################

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)
#print(emp_2)

#print(emp_1.email)
#print(emp_2.email)

#print(emp_1.fullname(self))

# These two lines do the exact same thing
emp_1.fullname()
Employee.fullname(emp_1)


#######################################################
# This was from Live Python youtube channel, helped understand about __init__
# Not sure I still grasp it. Something easy will click soon.
#######################################################

class Tweet:
    def __init__(self, message):
        self.message = message

    def print_tweet(self):
        print(self.message)

t = Tweet('an instance of Tweet')
t.print_tweet()

a = Tweet("Test")
b = Tweet("Test2")

print(a.message)
print(b.message)

a.message = '140 characters.'
b.message = 'Something entirely different'


#This will return a type object 'Tweet' has no attribute 'message' error
#print(Tweet.message)

print(a.message)
print(b.message)


#######################################################
# This is the Bottle test. I'm still trying to figure out Object's,
# how to call them, how to assign them attributes, etc.
#######################################################


class Bottle:

    is_hairy = True
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        pass

    def callBottle(self):
        print("{} will be {} years old tomorrow!".format(self.name, self.age))

    def getBottle(self):
        print("{} is {} years old.".format(self.name, self.age))

Bottle.name = ("Hola", 23)
Bottle.age = ("test", 60)

print(Bottle.name[0] + " is " + str(Bottle.name[1]) + " years old bro.")



bo1 = Bottle("Jim Bean", 95)
bo1.getBottle()
bo2 = Bottle("Skyy Vodka", 35)
bo2.getBottle()

#######################################################
### Bottle test still unresolved. Seems to work but makes little sense.
#######################################################


#######################################################
# Everything below needs to be reviewed to see where I messed up
#######################################################
import os

class Bottle:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def name(self):
        return self.name

    def age(self):
        return self.age

    
nameInput = input("Enter name for Bottle: ")
ageInput = input("Enter age of Bottle: ")

bo = Bottle(nameInput, ageInput)

print("You're bottle, " + bo.name + ", is " + bo.age + " year's old.")
'''
