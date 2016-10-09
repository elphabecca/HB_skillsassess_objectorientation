"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Polymorphism (Interchangeability of components) - This is the idea that despite the type of 
        information being passed (string, int, list), all instances will go through a 
        similar process.  Said another way, polymorphism helps us simplify code because 
        we don't have to write a bunch of conditional statments for different types of input.

   Encapsulation (Keeping everything "together") - Encapsulation helps the programmer
        maintain a degree of control over their code by grouping certain attributes
        and methods under a uniting class.  Since definitions within a class can only be
        accessed via that class, it helps to group or chunk variables or functions that
        aren't meant to be used outside the scope of the class.

   Abstraction (Hiding details we don't need) - Abstraction is about making code
        simpler and easier to read through the "hiding" of things.  It's not really
        "hiding" so much as it what I've just decided to call "organized hierarchical chunking".
        If you can describe the general attributes of an object through a parent object, then
        you don't have to re-describe or re-write all those general attributes, as they
        are already described elswhere and shared via inheritance.  

2. What is a class?

    A class is a smarter dictionary.  It can house data like a dictionary, but apply a
    pre-determined structure and/or attributes to the data.  It's sort of like a 
    skeleton -- you can make a lot of varied humans based off of the same blueprint 
    of a skeleton.

3. What is an instance attribute?

    An instance attribute is a detail that pertains to a specific instance of an
    object. For example, all objects in class Cat are species "feline", but not
    all are named "Mr. Fluffy Boots".  Mr. Fluffy Boots is an instance attribute
    because it pertains to the instance of Mr. Fluffy Boots, whereas species = "feline"
    is a class attribute because it pertains to all objects of class Cat.

4. What is a method?

    A method is a function within a class.  Housing a function within a class
    protects the function from being used outside it's intended use-case(s).

5. What is an instance in object orientation?

    When you create an item in a class, it's referred to as an instance (or an object)
    of the class.  The creation of an instance is called instatiation.  Object and instance 
    can be used interchangeably. 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is a detail or piece of information that is pre-determined
   for the class, whereas an instance attribute is a piece of information specific
   to a particular instance.  Let's say I have a class "Friends" - a class attribute
   would be something that pertains to all of my friends, like being human or
   breathing oxygen or being nice. An instance attribute would be something they
   each have but is different depending on the instance (so an instance attribute is
   set directly on the object).  Examples of this would be things like liking sushi,
   their name, or their gender.  Class attributes can be adjusted for very, very 
   special cases (like my cats who are my friends but not human), but in general should 
   apply to the whole class.


"""


# Parts 2 through 5:
# Create your classes and class methods
# http://fellowship.hackbrightacademy.com/materials/skills/object-orientation/

# Part 2
""" Directions: Make Python classes that could store the each of the following 
three pieces of data. Use the dictionaries below as examples to guide you in 
creating class definitions for the following objects. Define an __init__ method 
to allow callers of this class to provide initial values for each attribute. """

class Student(object):
    """A class containing first name, last name, and addresses for students."""

    def __init__(self, first_name, last_name, street_address):
        """Identifies first name, last name, and street address for the student.

        Auto-adjusts for some capitalization. """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.street_address = street_address.title()

class Question(object):
    """ A class for questions and answers."""

    def __init__(self, question, correct_answer):
        """The question and correct answer"""
        self.question = question
        self.correct_answer = correct_answer

class Exam(object):
    """Exam Class.

    Very Serious."""

    def __init__(self, name):
        """Name the exam, create an empty list for questions.

        Auto-adjusts for some capitalization in Exam Name."""
        self.name = name.title()
        self.questions = []

# Part 3
# Add methods to work above.

# Part 4
# Make a real exam.

# Part 5
# Inheritance
