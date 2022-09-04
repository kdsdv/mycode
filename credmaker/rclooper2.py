#!/usr/bin/env python3
''' Python Basics
    Lab 35: Write to Files / Creating Output Fles from Data Sets
    CREATE MOCK CREDENTIAL FILES FROM USER INPUT OR CSV TEST FILE | kdsdv '''

# Creates admin.rc files manually from prompting the user
def createManually():
    print(f'\nCreating manually...')

    filename = 'admin.rc'
    authURL = input("What is the OS_AUTH_URL? ")
    projectName = input("What is the OS_PROJECT_NAME? ")
    projectDomain = input("What is the OS_PROJECT_DOMAIN_NAME? ")
    username = input("What is the OS_USERNAME? ")
    userDomain = input("What is the OS_USER_DOMAIN_NAME? ")
    password = input("What is the OS_PASSWORD? ")

    rcInfo(filename, authURL, projectName, projectDomain, username, userDomain, password)

    print(f'{filename} has been created\n')

# Creates x number of admin.rc files from a csv file
def createCSV():
    fileNo = 0 # counts the number of admin.rc files created
    
    print(f'\nCreating from CSV file....')

    with open('csv_users.txt', 'r') as fileIn:
        for line in fileIn:
            authURL, projectName, projectDomain, username, userDomain, password = line.strip().split(',')
            fileNo += 1 # increases counter by one

            if fileNo >= 1 and fileNo <= 9:
                filename = 'admin0' + str(fileNo) + '.rc'
            else:
                filename = 'admin' + str(fileNo) + '.rc'

            rcInfo(filename, authURL, projectName, projectDomain, username, userDomain, password)

    print(f'{fileNo} admin.rc files have been created\n')

# Information retrieved from csv_users.txt and 26 separate admin.rc files were created
def rcInfo(fName, aURL, pName, pDomain, user, uDomain, pwd):
    with open(fName, 'w') as fileOut:
        fileOut.write(f'export OS_AUTH_URL={aURL}\n')
        fileOut.write(f'export OS_IDENTITY_API_VERSION=3\n')
        fileOut.write(f'export OS_PROJECT_NAME={pName}\n')
        fileOut.write(f'export OS_PROJECT_DOMAIN_NAME={pDomain}\n')
        fileOut.write(f'export OS_USERNAME={user}\n')
        fileOut.write(f'export OS_USER_DOMAIN_NAME={uDomain}\n')
        fileOut.write(f'export OS_PASSWORD={pwd}\n')

# Write a program that reads the data in csv_users.txt, and use it to create 26 separate admin.rc files
def main():
    createRC = '' # the users response

    print('CREATE RUNNING CONFIGURATION FILE\n')

    while createRC != 'q':
        createRC = input('Press 1 to create manually, Press 2 to create from CSV file, or Press q to quit: ')

        if createRC.lower() == 'q': # quit program
            break
        elif createRC == '1':
            createManually() # Manually create admin.rc file by prompting the user
        elif createRC == '2':
            createCSV() # Creating x number of admin.rc files from a CSV file
        else:
            print(f'\nInvalid entry. Restarting...') # restart program until a valid response is entered

main()
