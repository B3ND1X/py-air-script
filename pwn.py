#!/usr/bin/python
import os
import time
with open('INFO.txt') as f:
    contents = f.read()
    print(contents)

menu_options = {
    1: 'ATTACK ALL NETWORKS',
    2: 'SCAN FOR NETWORKS',
    3: 'CRACK CAPTURED HANDSHAKES',
    4: 'VIEW LOG',
    5: 'REMOVE CAPTURED HANDSHAKES',
    6: 'INSTALL DEPENDENCIES/UPDATE',
    7: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1(self):
     print('Handle option \'ATTACK ALL NETWORKS\'')

def option2(self):
     print('Handle option \'SCAN FOR NETWORKS\'')

def option3(self):
     print('Handle option \'CRACK CAPTURED HANDSHAKES\'')
     
def option4(self):
     print('Handle option \'VIEW LOG\'')
     
def option5(self):
     print('Handle option \'REMOVE CAPTURED HANDSHAKES\'')
     
def option6(self):
     print('Handle option \'INSTALL DEPENDENCIES/UPDATE\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1: 
           option1(os.system("sudo ./run.py"))
        elif option == 2:
            option2(os.system("sudo ./quick-scan.py"))
        elif option == 3:
            option3(os.system("sudo ./crack.py"))
        elif option == 4:
            option4(os.system("sudo ./log.py"))
        elif option == 5:
            option5(os.system("sudo ./clean.py"))
        elif option == 6:
            option6(os.system("sudo ./install.py"))
        elif option == 7:
            print('Goodbye!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 7.')
