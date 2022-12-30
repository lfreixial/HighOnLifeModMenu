import customtkinter
import main

class Menu(object):
    def __init__(self, queue_list):
        self.queue_list = queue_list # the queue list from main.py
        self.root = customtkinter.CTk()
        self.root.geometry("400x400") # set the size of the window
        self.root.title("High On Life ModMenu") 
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.label = customtkinter.CTkLabel(master=self.frame, text="High On Life ModMenu", font=("Arial", 24))
        self.label.pack(pady=12, padx=10)

         # genereates a button and when it is pressed it will call a lambda function which will call the cheat activator function from main.py passing in the queue list
        self.button = customtkinter.CTkButton(master=self.frame, text="Infinite Pistol Ammo", command=lambda: main.unlimtedAmmoActivator(self.queue_list))
        self.button.pack(pady=12, padx=10)

        self.button = customtkinter.CTkButton(master=self.frame, text="Infinite Shotgun Ammo", command=lambda: main.unlimtedShotgunAmmoActivator(self.queue_list))
        self.button.pack(pady=12, padx=10)

        self.button = customtkinter.CTkButton(master=self.frame, text="Infinite Fuel", command=lambda: main.unlimtedStaminaActivator(self.queue_list))
        self.button.pack(pady=12, padx=10)