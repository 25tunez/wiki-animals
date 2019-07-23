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

#display on tkinter
main = tk.Tk()
main.title("Animal List") 
main.geometry("300x150+450+250")
msg = tk.Message(main, text = "According to wikipedia, The terms below apply to many or all taxa in a particular biological family, class, or clade.\n",  width = 280)
msg.pack()
animals = ", ".join(animals)
tk.Message(main, text = animals, width = 280).pack()
main.mainloop()
