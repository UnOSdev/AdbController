import subprocess as sbp
from difflib import get_close_matches
import os
import time


def welcome():
    print(
        "Hello, welcome to ADBcontroller, write 'connect' to connect to device/emulator\n write 'help' for more information.\n TURN ON USB DEBUGGING BEFORE USING THIS PROGRAM")

    def inpat():
        try:
            i = input()
            if i == 'connect':
                print("Connecting please wait...")
                time.sleep(0.5)
                print("...")
                main()
            elif i == 'help':
                print(
                    "ADBcontroller \n Version = 0.1 \n Ubayda \n Alfa Realese \n Notes: \n ADBcontroller can connect only to first device in the adb devices list \n "
                    " If your pc connected to more than 1 devices, you must disconnect the devices that you dont gonna use \n its a little bug and im gonna fixed it in lesser time\n"
                    " Thank you for using ADBcontroller ")
                inpat()
            elif i == 'exit':
                print("See ya")
                quit()
            else:
                print("Unknown command, please try again!")
                inpat()
        except KeyboardInterrupt:
            print("If you want to exit just write it!")
            inpat()
    inpat()


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
            shell(device)
        else:
            print("Detected " + device + " device, continue... ")
            shell(device)
    except IndexError:
        print("ADB module not found, are you sure that you installed it?\n If you are in Windows just copy the .py(this) file to adb, and run it.")
        input()
        quit()


def shell(id):
    try:
        c = input("print 'help' for available commands: ")
        if c == 'open':
            v = input("Write package/app name: ")
            sbp.run("adb -s " + id + " shell monkey --pct-syskeys 0 -p " + v + " 1 ", shell=True, stdout=sbp.DEVNULL)
            print("Done!\n" + v + " must be opened.")
            shell(id)
        elif c == 'install':
            a = sbp.getoutput('ls apks/')
            if a == "ls: cannot access 'apks/': No such file or directory":
                print("'apks' folder didn't found did you created it?")
                shell(id)
            else:
                print(a)
                pass
            v = input("Write the .apk file name that in 'apks' folder: ")
            os.system('adb -s '+ id +' install apks/'+ v)
            shell(id)
        elif c == 'livelog':
            try:
                print("Type 'CTRL + C' to exit!")
                time.sleep(2)
                print("Oh i forgot to say, that logs are very fa...")
                time.sleep(1.5)
                sbp.run("adb -s "+ id + " logcat",shell=True)
            except KeyboardInterrupt:
                print("\nStopping...")
                shell(id)
        elif c == 'stop':
            v = input("Write package/app/service name: ")
            sbp.run("adb -s " + id + " shell am force-stop " + v, shell=True, stdout=sbp.DEVNULL)
            print("Done!\n" + v + " must be stopped.")
            shell(id)
        elif c == "reboot":
            sbp.run("adb -s " + id + " shell reboot", shell=True, stdout=sbp.DEVNULL)
            print("\nAbd restarted your device, the program gonna quit")
            quit()
        elif c == 'exit':
            print("bye bye")
            quit()
        elif c == 'monitor':
            try:
                sbp.run("adb -s " + id + " shell am monitor",shell=True)
                shell(id)
            except KeyboardInterrupt:
                print("\nExiting device monitoring...")
                shell(id)
        elif c == 'clear':
            v = input("What package/app/service data you want to clean/reset")
            sbp.run("adb -s " + id + " shell pm clear " + v, shell=True, stdout=sbp.DEVNULL)
            print("Done!\n" + v + " data must be cleared.")
            shell(id)
        elif c == 'list':
            os.system("adb -s " + id + " shell pm list package")
            print("These is the full list of the installed packages")
            shell(id)
        elif c == 'help':
            print(
                " Stop App/Service: 'stop'\n All packages list: 'list'\n Open application: 'open'\n Restart device: "
                "'reboot' \n Apps activity: 'monitor'\n Clear the app data: 'clear'\n Delete the package/app/service: "
                "'delete'\n Take THE FULL information about the package/app/service : 'fullinfo'\n Package's used apk's: "
                "'apkpath'\n Install package from 'apks' file: 'install' \n Realtime device log: 'livelog' ")
            shell(id)
        elif c == 'delete':
            v = input("package/app/service name: ")
            sbp.run("adb -s " + id + " shell pm uninstall " + v, shell=True, stdout=sbp.DEVNULL)
            print("Done!\n" + v + " must be deleted from your device")
            shell(id)
        elif c == 'fullinfo':
            v = input("package/app/service name: ")
            os.system("adb -s " + id + " shell pm dump " + v)
            print("\nThis is the full information about "+ v)
            shell(id)
        elif c == 'apkpath':
            v = input("package/app/service name: ")
            os.system("adb -s " + id + " shell pm path "+ v)
            print("APK list of "+ v)
            shell(id)
        else:
            print("Unknown command...")
            shell(id)
    except KeyboardInterrupt:
        print("\n\nIf you want to exit just write it!")
        shell(id)

if __name__ == "__main__":
    welcome()
