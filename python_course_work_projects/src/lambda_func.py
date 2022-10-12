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

def ReadDataByValue_GetPoint(item):
    """
    ReadDataByValue_GetPoint 
    
    Args:
        item (list): List from which the element needs to be returned

    Returns:
        string: the point value from the given list 
    """    
    return item["point"]

def ReadDataByValue_GetName(item):
    """
    ReadDataByValue_GetName 
    
    Args:
        item (list): List from which the element needs to be returned

    Returns:
        string: the namr value from the given list 
    """    
    return item["name"]


def Lambda_Expression_Collector_Function():
    
    #Lambda function a^2
    pow2l = lambda a: a**2
    print("Lambda 1:", pow2l(3))
    
    #Lambda function a^b
    powl = lambda a,b: a**b
    print("Lambda 2:", powl(5,3))

    #Lambda: absolute value, if-else statement
    abs = lambda x: x if x>=0 else -x
    print("Lambda 3:",abs(5))
    print("Lambda 4:",abs(-5))
    
    sqrt = lambda x: math.sqrt(x) if x>=0 else None
    print("Lambda 5:",sqrt(25))
    print("Lambda 6:",sqrt(-25))
    
    my_list = [ 1,5,8,4,3]
    print("List:",my_list)
    my_list.sort() # sort() modifies the original list
    print("Sorted List:",sorted(my_list)) #sorted() return a new sorted list

    #Sorting list with nested dictionaries by custom function using key
    student =[
        {"name" :  "John", "neptun" :  "FJEAJD", "point" : 78},
        {"name" :  "Kevin", "neptun" :  "ZHEAJD", "point" : 66},
        {"name" :  "Bob", "neptun" :  "UTEAJD", "point" : 92}
        ]
    
    #sort list by point, 
    student.sort(key = ReadDataByValue_GetPoint)
    print(student)
    #Sort list by name (reverse order)
    student.sort(key = ReadDataByValue_GetName, reverse = True)
    print(student)
    #sorted(student, key=getPoint)
    
    #Sort list by neptun with lambda function
    student.sort(key=lambda item: item["neptun"])
    print(student)

def GetLargestElementInNestedList(nested_list):
    #Step1: Lambda function to sort nested lists
    sortList = lambda x: (sorted(i) for i in x)
    res = sortList(nested_list)
    print(list(res))
    #Step2: Lambda function to get the largest element of sorted lists
    le = lambda x, func: [y[-1] for y in func(x)]
    return le(nested_list, sortList)

def GetMapElement(my_list2):
   
    resultList = list(map(lambda x: x**2, my_list2))
    return resultList

def GetOddNumbersFromList(my_list2):
    return list(filter(lambda x: x%2!=0,my_list2))