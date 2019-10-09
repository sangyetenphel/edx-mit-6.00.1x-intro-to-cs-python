# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:51:48 2019

@author: Sangye Tenphel
"""

# =============================================================================
# class Animal(object):
#     def __init__(self, age):
#         self.age = age
#         self.name = None
#         
#     def getAge(self):
#         return self.age
#     
#     def getName(self):
#         return self.name
#     
#     def setAge(self, age):
#         self.age = age
#         
#     def setName(self, name = ''):
#         self.name = name
#         
#     def __str__(self):
#         return "Animal: " + str(self.getName()) + " : " + str(self.getAge())
# =============================================================================

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
        
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name 
    
    def set_age(self, newage): 
        self.age = newage 
        
    def set_name(self, newname=""):
        self.name = newname 
        
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)    
    
class Cat(Animal):        
    def speak(self):
        print('Meow')
        
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

class Rabbit(Animal):
    def speak(self):
        print('puuf')
        
    def __str__(self):
        return "Rabbit:"+str(self.name)+":"+str(self.age)    
        
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
        
    def get_friends(self):
        return self.friends
    
    def set_friends(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
        
    def speak(self):
        print('Hello')
        
    def age_diff(self, other):
        diff = self.age - other.age
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
            
    def __str__(self):
        return "Person:"+str(self.name)+":"+str(self.age) 
        
import random

class Student(Person):
    def __init__(self, name, age, major = None):
        Person.__init__(self, name, age)
        self.major = major
    
    def change_major(self, major):
        self.major = major
        
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("Get a job")
        elif 0.25 <= r < 0.5:
            print("Work Hard, Study!!")
        elif 0.5 <= r < 0.75:
            print("Practise what you learned.")
        else:
            print("Be smart..")
            
    def __str__(self):
        return "Student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
        
        
        
        