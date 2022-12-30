A simple python mod menu for the game High On Life.

This program works by replacing the value in memory with the value that we want, this in theory allows us to hack the game however the pointers are not stable and will crash or not point to the correct memory address.

This program makes use of a menu (tkinter/custometkinter) to select the cheats it can then add a value to the queue (in this case a function with the cheats) and then another thread will be able to read from that queue and save it to a variable to constantly execute the cheat (update the value in memory)