# AdbController
Installation:

  Linux:
  
    sudo apt update
    
    sudo apt install python3.8 // Installing Python3.8
    
    sudo apt install git //Installing Git
    
    sudo apt install android-tools-adb //Installing ADB
    
    git clone https://github.com/UnOSdev/AdbController //Downloading the program files

  Windows:
  
    Download and install Python3.8: https://www.python.org/downloads/release/python-385/
    
    Download and install Git: https://git-scm.com/downloads
    
    Download ADB: https://www.xda-developers.com/install-adb-windows-macos-linux/ (Extract the zip to any folder)



This program can control your android phone by ADB module, without root.

NOTE: This program tested on Linux(Ubuntu 20.04 LTS), but dont worry its may working in Windows too, you need just take "ADBcontroller.py" to adb directory and run it.
If you find any bug, contact me for it.

ًWork function list:

  Stop App/Service: 'stop'
  
  All packages list: 'list'
  
  Open application: 'open'
  
  Restart device: 'reboot' 
  
  Apps activity: 'monitor'
  
  Clear the app data: 'clear'
  
  Delete the package/app/service: 'delete'
  
  Take THE FULL information about the package/app/service : 'fullinfo'
  
  Package's used apk's: 'apkpath' 
  
  Install '.apk' package from 'apks' folder: 'install'
  
  Realtime device log: 'livelog'

The program absolutely does not need superuser or root rights.
The only thing you need is to enable USB debugging on you'r android phone.

Ubayda
