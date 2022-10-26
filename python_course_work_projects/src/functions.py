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

from .lambda_func import *

from .mintazh2 import *

from .mintazh3 import *

from .zh4 import *
#==============================================================#
#==============================MAIN============================#
#==============================================================#

def Print_Array_Of_Numbers(array):
    """
    Print_Array_Of_Numbers _summary_

    Args:
        array (array): array of integers
    """    
    #traversing a list with a for loop
    for num in array:
        print(num)
        
def Max_Value_In_Array(array):
    """
    Max_Value_In_Array 
    Function returns max value from input array

    Args:
        array (array): integer array

    Returns:
        integer: biggest value of input array
    """    
    return max(array)
    
def Arrays_With_For_Loops_Example(numbers):
    """
    Arrays_With_For_Loops_Example _summary_

    Args:
        numbers (array): array contains only integers for the following subfunctions

    Returns:
        boolean: E_OK
    """
    returnValue = E_NOT_OK
    try:
       
        Print_Array_Of_Numbers(numbers)
        print("Max:", Max_Value_In_Array(numbers))
        
    except:
        print("An exception occurred")
    else:
        returnValue = E_OK
        
    return returnValue

def Dictionary_Example(my_dict):
    # print full dictionary
    print(my_dict)
    #get elements
    print(my_dict["name"]) # John
    print(my_dict["age"]) # 30
    #nested list
    print(my_dict["numbers"][0]) # 34   
    #nested dictionary
    print(my_dict["params"]["weight"]) #80

    #add new key-value pair to the nested dictionary
    my_dict["params"]["foot"] = 42
    print(my_dict)
    #delete a key-value pair from the nested dictionary
    del my_dict["params"]["size"]
    print(my_dict)
    #update value by key
    my_dict["params"]["weight"] = 90
    print(my_dict)

def Dictionary_Example_For_Loops(My_Dictionary):
    """
    Dictionary_Example_For_Loops 
    Traversing trought a dictionary with a for loop, and check if instance is string or list.

    Args:
        my_dict (dict): Dictionary

    Returns:
        boolean: E_OK, constants, value is True
    """    
    
    for i in My_Dictionary:
        if isinstance(My_Dictionary[i], str):
            print(i, ":", My_Dictionary[i])
        if isinstance(My_Dictionary[i], list):
            for Number in My_Dictionary[i]:
                print(Number)
    return E_OK
    
def Generate_List(my_list):
    print(my_list) 
    my_list.clear()
    print(my_list) # []
    my_list = []
    for i in range(10):
        my_list.append(i**2)
    print(my_list) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def main():  # pragma: no cover
    #numbers = [ 6,3,5,7,2,4,5]
    #my_list = [ "p","y","t","h","o","n"]
    #nested_list = [[2,3,4], [1,4,1,6,64], [3,6,9,12]]
    #my_list2 = [5,2,4,7,4,2,17]
    #Arrays_With_For_Loops_Example(numbers)
    #Dictionary_Example(EXAMPLE_DICT)
    #Dictionary_Example_For_Loops(EXAMPLE_DICT)
    #Generate_List(my_list)
    #Lambda_Expression_Collector_Function()
    #print("Largest in Nested List:", GetLargestElementInNestedList(nested_list))
    #print("Map Element", GetMapElement(my_list2))
    #print("Odd Numbers", GetOddNumbersFromList(my_list2))
    #MintaZH_Main()
    #MintaZH_Main2()
    MainZH4()

