import os
from difflib import get_close_matches
import subprocess as sbp
import time

def monitor(id):
    try:
        time.sleep(1.5)
        sbp.run("adb -s " + id + " shell am monitor", shell=True)
        time.sleep(2)
        quit()
    except KeyboardInterrupt:
        print("\nExiting device monitoring...")
        time.sleep(2)
        quit()

def main():
    try:
        device = os.popen("adb devices").read().split('\n', 1)[1].split("device")[0].strip()
        cheaker = list(device)
        if cheaker == []:
            print("No device detected")
            b = input("Restart program?(y/n): ")
            if b == 'y':
                main()
            elif b == 'n':
                quit()
            else:
                print("Error you may not writed 'y' or 'n', aborting program.")
        a = get_close_matches('emulator', [device])
        if a != []:
            print("Detected emulator,continue...")
            monitor(device)
        else:
            print("Detected " + device + " device, continue... ")
            monitor(device)
    except IndexError:
        print("ADB module not found, are you sure that you installed it?\n If you are in Windows just copy the .py(this) file to adb, and run it.")
        input()
        quit()
if __name__ == '__main__':
    main()