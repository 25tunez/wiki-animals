#create a "framework" to build tkinter interface
import animalScript as aS
import tkinter as tk
        
def test_size_input():
    #testing the size input
    pass

def test_position_input():
    #testing the position input
    pass

soup = aS.getSoup()
soup = aS.enhanceSoup(soup)
animals = aS.getAnimals(soup)
print(animals)
