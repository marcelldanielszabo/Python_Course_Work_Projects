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

from statistics import mean 

#==============================================================#
#==============================MAIN============================#
#==============================================================#

export = {
    "cars":[
          { "brand": "Ford",   "model" : "Focus",  "year": 2020, "fuel type": "petrol",  "consumptions": [ 4.1, 5.2, 4.5, 5.3, 4.7]},
          { "brand": "Ford",   "model" : "Modeo","year": 2020, "fuel type": "diesel",  "consumptions": [ 6.1, 6.2, 5.5, 6.9, 9.1]},
          { "brand": "Opel",   "model" : "Astra",   "year": 2016, "fuel type": "petrol",  "consumptions": [ 5.2, 5.1, 5.5, 4.9, 4.9]},
          { "brand": "VW",     "model" : "Golf",    "year": 2021, "fuel type": "diesel",   "consumptions": [ 4.8, 4.8, 4.9, 5.1, 4.8]},
          { "brand": "Honda","model" : "Civic",   "year": 2018, "fuel type": "petrol",  "consumptions": [ 8.5, 7.3, 6.2, 6.7, 7.5]},
          { "brand": "Fiat",     "model" : "500",     "year": 2022, "fuel type": "petrol",  "consumptions": [ 4.9, 4.7, 4.8, 4.7, 5.1]}
             ],
     "motorbikes" : [
          { "brand": "KTM",        "model" : "Duke",      "year": 2022, "type": "naked",   "consumptions": [ 3.1, 3.2, 3.5, 3.3, 2.7]},
          { "brand": "BMW",      "model" : "F1200GS", "year": 2020, "type": "enduro", "consumptions": [ 4.1, 5.2, 4.5, 4.3, 5.2]},
          { "brand": "Kawasaki","model" : "Z400",       "year": 2019, "type": "naked",   "consumptions": [ 3.1, 3.4, 2.5, 3.3, 3.2]},
          { "brand": "Yamaha",  "model" : "MT-07",    "year": 2020, "type": "enduro", "consumptions": [ 3.7, 3.4, 2.9, 3.4, 3.2]},
          { "brand": "Honda",    "model" : "CBR650R","year": 2021, "type": "sport",    "consumptions": [ 4.7, 4.4, 4.9, 5.4, 5.2]},
     ]
}

class Vehicle:
    def __init__(self, _marka, _modell, _gyartas, _fogyasztas):
        self.marka = _marka
        self.modell = _modell
        self.gyartas = _gyartas
        self.fogyasztas = _fogyasztas
    def getFogyasztas(self):
        return mean(self.fogyasztas)

class Car(Vehicle):
    def __init__(self, _marka, _modell, _gyartas, _fogyasztas, _uzemanyag):
        super().__init__( _marka, _modell, _gyartas, _fogyasztas)
        self.uzemanyag = _uzemanyag

    def __str__(self):
        return self.marka + ", " + self.modell + ", " + self.gyartas + ", " + self.uzemanyag + ", "+ str(self.getFogyasztas())

class Motorbikes(Vehicle):
    def __init__(self, _marka, _modell, _gyartas, _fogyasztas, _motortipus):
        super().__init__( _marka, _modell, _gyartas, _fogyasztas)
        self.motortipus = _motortipus

    def __str__(self):
        return self.marka + ", " + self.modell + ", " + self.gyartas + ", " + self.motortipus + ", "+ str(self.getFogyasztas())


def MainZH4():
    vehicle_list = []
    for item in export:
        for a in item:
            vehicle_list.append(Car(a["marka"], a["modell"], a["gyartas"], a["fogyasztas"], a["uzemanyag"]))
        for b in item:
            vehicle_list.append(Motorbikes(b["marka"], b["modell"], b["gyartas"], b["fogyasztas"], b["motortipus"]))
    for vhcl in vehicle_list:
        print(vhcl)