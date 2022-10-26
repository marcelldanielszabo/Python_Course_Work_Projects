# Created by: Marcell Daniel Szabo
# Template created by: rochacbruno
# License - See file: LICENSE

#==============================================================#
#===========================IMPORTS============================#
#==============================================================#
import sys
import os
import argparse
import math
#==============================================================#
#==========================INCLUDES============================#
#==============================================================#

from ..base import *

#==============================================================#
#==============================MAIN============================#
#==============================================================#

redmine = [
 { "project" : "GINOP-2.2.1", "role":"developer", "name" : "Jack", "hours" : [ 6,3,1,2,1] },
 { "project" : "TAMOP-A.2.1", "role":"developer", "name" : "Kevin", "hours" : [ 2,4,7,5,5] },
 { "project" : "KFI-2022/02", "role":"developer", "name" : "Robert", "hours" : [ 1,4,3,6,1] },
 { "projects" : [ "TAMOP-A.2.1","KFI-2022/02" ], "role":"manager" , "name" : "Tom", },
 { "project" : "GINOP-2.2.1" , "role":"developer", "name" : "Bob", "hours" : [ 2,5,7,6,2] },
 { "project" : "KFI-2022/02", "role":"developer", "name" : "William", "hours" : [ 6,3,1,2,6] },
 { "project" : "TAMOP-A.2.1", "role":"developer", "name" : "Jack", "hours" : [ 1,1,3,0,6] },
 { "project" : "GINOP-2.2.1" , "role":"developer", "name" : "Mark", "hours" : [ 6,4,1,3,3] },
 { "project" : "KFI-2022/02", "role":"developer", "name" : "Michael", "hours" : [ 5,4,7,6,6] },
 { "project" : "GINOP-2.2.1" , "role":"developer", "name" : "Maria", "hours" : [ 3,2,1,2,2] },
 { "project" : "GINOP-2.2.1" , "role":"developer", "name" : "Ryan","hours" : [ 6,3,3,1,5] },
 { "projects" : [ "GINOP-2.2.1", ], "role":"manager" , "name" : "Scott"}
]

class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, project, hours):
        super().__init__(name)
        self.project = project
        self.hours = hours
    def getSum(self):
        return sum(self.hours)
    def __str__(self):
        return self.name + ", " + str(self.getSum())

class Manager(Employee):
    def __init__(self, name, projects):
        super().__init__(name)
        self.projects = projects
    def __str__(self):
        return self.name+ ", " + ", ".join(self.projects)

def MainZH3():
    employee = []
    for item in redmine:
        if item["role"]=="developer":
            employee.append(Developer(item["name"], item["project"], item["hours"]))
    if item["role"]=="manager":
        employee.append(Manager(item["name"], item["projects"]))
    for empl in employee:
        print(empl)