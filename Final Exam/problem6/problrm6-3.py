# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:02:21 2019

@author: Sangye Tenphel
"""

# Problem 6-3
# 15.0/15.0 points (graded)
# You change your mind once more. You want to keep the behavior from Part 2, but now you would like:

# >>> pe.say('the sky is blue')
# Prof. eric says: I believe that eric says: the sky is blue 

# >>> ae.say('the sky is blue')
# Prof. eric says: It is obvious that I believe that eric says: the sky is blue 

# Change the Professor class definition in order to achieve this. You may have to modify your implmentation for a previous part to get
# this to work.

# Paste ONLY the Professor class in the box below. Do not leave any debugging print statements.

# For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test
# cases.

class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer): 
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return "Prof. " + Person.say(self, 'It is obvious that ' + Lecturer.lecture(self, stuff))
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)
# As written, this code leads to an infinite loop when using the Arrogant Professor class.

# Change the definition of ArrogantProfessor so that the following behavior is achieved:

e = Person('eric') 
le = Lecturer('eric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric')