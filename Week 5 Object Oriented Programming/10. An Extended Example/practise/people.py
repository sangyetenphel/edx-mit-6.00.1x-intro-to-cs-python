# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 20:02:21 2019

@author: Sangye Tenphel
"""
import datetime

class Person(object):
    def __init__(self, name):
        '''create a person called name'''
        self.name = name
        self.birthday = None
        self.lastName = name.split(" ")[-1]
        
    def getLastName(self):
        '''return self's last name'''
        return self.lastName
    
    def setBirthday(self, month, day, year):
        ''' set self's birthday to birthDate'''
        self.birthday = datetime.date(year, month, day)
        
    def get_age(self):
        '''return self's current age in days'''
        if self.birthday == None:
            raise ValueError('first give me your birthday!')
        return datetime.date.today() - self.birthday
    
    def __lt__(self, other): # sort() in descending order for sorting the names in the list
        """return True if self's name is lexicographically
            less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
            
    def __str__(self):
        '''return self's name'''
        return self.name
    
class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1    
        
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        print(self.getLastName() + " says " + utterance)

class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.classYear = classYear
    
    def getClass(self):
        return self.classYear
    
    def speak(self, utterance):
        MITPerson.speak(self, "Dude, " + utterance)
        
class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student) 

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.deparment = department
        
    def speak(self, utterance):
        new = "In deparment " + str(self.deparment) + " we say "
        return MITPerson.speak(self, new + utterance)
        
    def lecture(self, topic):
        Professor.speak(self, 'It is obvious that ' + topic)
        
class Grades(object):
    '''A mapping from students to a list of grades'''
    def __init__(self):
        '''Create empty grade book'''
        self.students = []  # list of Student objects
        self.grades = {}    # maps idNum -> List of grades
        self.isSorted = True  # true if self.sorted is sorted
        
    def addStudent(self, student):
        """Assumes: is of type student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate Student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    
    def addGrades(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError: # change to keyerror !!!!!!!!
            raise ValueError("Student not in grade book")
    
    def getGrades(self, student):
        '''Return a list of grades for student'''
        try:
            return self.grades[student.getIdNum()][:] # return copy of student's grades
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        '''Returns a list of all the students in the grade book'''
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        #return self.students[:]
        for s in self.students:
            yield s
    
def gradeReport(course):
    '''Assumes: course is of type grades'''
    report = []
    for s in course.allStudents(): # use methood to prevent data; preserves information hiding
        total = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            total += g
            numGrades += 1
        try:
            avgGrades = total / numGrades
            report.append(str(s) + "\'s mean grade is " + str(avgGrades))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)
        
    
               
        