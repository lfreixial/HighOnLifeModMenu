import queue
import threading
from pymem import *
from pymem.process import *
import menu

# the game process
pm = Pymem("Oregon-Win64-Shipping.exe") 

# gets the base address of the game module
gameModule = module_from_name(pm.process_handle, "Oregon-Win64-Shipping.exe").lpBaseOfDll


cheatsList = []
cheats_queue = queue.Queue()

# get the pointer address from the base and the offset
def getPointerAddress(base, offset):
    address = pm.read_longlong(base)
    for i in offset:
        if i != offset[-1]:
            address = pm.read_longlong(address + i)
    return address + offset[-1]


## Will be called from the menu by the buttons and then will add the cheat function to the queue
def unlimtedStaminaActivator(queue_list):
    queue_list.put(unlimtedStamina)

def unlimtedAmmoActivator(queue_list):
    queue_list.put(unlimtedAmmo)

def unlimtedShotgunAmmoActivator(queue_list):
    queue_list.put(unlimtedShotgunAmmo)

# unstable - crashes after 10 mins
def unlimtedStamina():
    pm.write_float(getPointerAddress(gameModule+0x05F590A0, [0x118,0x20,0x138,0x60,0x120,0x68,0xAD0]), 50.0)

# does not work - pointer is wrong
def unlimtedAmmo():
    pm.write_bytes(getPointerAddress(gameModule+0x05F54CB8, [0x3B0,0x28,0x2F0,0x1E0,0x40,0xF0,0xE0]), b'\x0f\x00\x00\x00', 4) # unlimted ammo

# does not work - pointer is wrong
def unlimtedShotgunAmmo():
    pm.write_bytes(getPointerAddress(gameModule+0x05F590A0, [0x30,0xA8,0x248,0x2F0,0x28,0x8,0xE0]), b'\x03\x00\x00\x00' ,4) # unlimted shotgun ammo

# main loop for the cheats, will read from the queue and add it to the cheatsList which will be executed   
def main(cheat_queue):

    while True:
        try:
            cheats = cheat_queue.get(timeout=0.3) # get the cheat from the queue
            cheatsList.append(cheats) # add the cheat to the list
            if cheats == "quit": # if the cheat is quit then
                break
        except queue.Empty:
            pass
        
        # excute all the cheats
        for cheat in cheatsList:
            cheat()
 
if __name__ == '__main__':
    gui = menu.Menu(cheats_queue) # create the menu  
    mainThread = threading.Thread(target=main, args=(cheats_queue,)) # starts the main loop in a thread with the queue passed as an argument
    mainThread.daemon = True # makes the thread a daemon so it will close when the main thread closes
    mainThread.start() # starts the thread
    gui.root.mainloop() # starts the menu