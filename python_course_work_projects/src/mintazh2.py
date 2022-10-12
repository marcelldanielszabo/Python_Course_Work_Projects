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

my_list = [
    {"course": "VEMISAB132P", "name": "John", "neptun": "KEISAK", "theory": [6, 9, 9, 9, 5], "practice":[3, 8, 9, 8]},
    {"course": "VEMISAB144A", "name": "John", "neptun": "KEISAK", "theory": [3, 2, 5, 7, 5], "practice":[3, 6, 9, 6]},
    {"course": "VEMISAB132P", "name": "Kevin", "neptun": "FKSJDE", "theory": [6, 9, 10, 10, 4], "practice":[9, 7, 9, 8]},
    {"course": "VEMISAB144O", "name": "Kevin", "neptun": "FKSJDE", "theory": [7, 2, 2, 6, 0], "practice":[3, 8, 9, 6], "result": 43},
    {"course": "VEMISAB144O", "name": "Bob", "neptun": "ZZRWD", "theory": [1, 9, 9, 3, 3], "practice":[9, 6, 9, 8], "result": 57},
    {"course": "VEMISAB144A", "name": "Joe", "neptun": "TTWQS","theory": [6, 6, 2, 3, 1], "practice":[3, 2, 9, 6]},
    {"course": "VEMISAB132P", "name": "Joe", "neptun": "TTWQS","theory": [6, 4, 2, 4, 5], "practice":[3, 8, 5, 8]},
    {"course": "VEMISAB144O", "name": "Peter", "neptun": "NVMCX","theory": [], "practice":[]},
    {"course": "VEMISAB144A", "name": "Bob", "neptun": "ZZRWD","theory": [1, 4, 4, 5, 8], "practice":[3, 8, 7, 9]},
    {"course": "VEMISAB132P", "name": "Peter", "neptun": "NVMCX","theory": [1, 1, 0, 0, 0], "practice":[1, 4, 9, 8]}
]

#A filter() függvény segítségével szűrd le a VEMISAB132P és VEMISAB144A kurzusokhoz tartozó
#eredményeket, majd
#b) egy külön függvény segítségével határozd meg, hogy mennyit szereztek meg a hallgatók az
#adott tárgy elméleti és gyakorlati pontjaiból, az eredményt írd vissza a listába „result” kulccsal
#c) rendezd növekvő sorrendbe azokat a bejegyzéseket, amikben szerepel már az összesített
#eredmény
#d) írasd ki a három legtöbb pontot szerzett hallgatót nevét, a kapcsolódó kurzust és az elért
#pontszámot!
#
def Calculate_Sum_From_Two_Lists(list_a,list_b):
    sum=0
    for point in list_a+list_b:
        sum+=point
    return sum

def MintaZH_Main():
    for item in list(filter(lambda x: x["course"]=="VEMISAB132P" or x["course"]=="VEMISAB144A",my_list)):
        item["result"] = Calculate_Sum_From_Two_Lists(item["theory"], item["practice"])
    result = sorted(list(filter(lambda x: "result" in x, my_list)), key = lambda x: x["result"])
    for res in result[-3:]:
        print(res["name"],res["course"], res["result"])


def MintaZH_Main2():
    for item in my_list:
        if(item["course"] == "VEMISAB132P" or item["course"]=="VEMISAB144A"):
            item["result"] = Calculate_Sum_From_Two_Lists(item["theory"], item["practice"])
    result = sorted(list(filter(lambda x: "result" in x, my_list)), key = lambda x: x["result"])
            
    for i in range(len(result)-3,len(result)):
        print(result[i]["name"],result[i]["course"],result[i]["result"])          
