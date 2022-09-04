#!/usr/bin/env python3
''' Python Basics
    Lab 35: Write to Files / Creating Output Fles from Data Sets
    CREATE 26 MOCK CREDENTIAL FILES FROM CSV TEST FILE | kdsdv '''

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
    fileNo = 0 # counts the number of admin.rc files created

    with open('csv_users.txt', 'r') as fileIn:
        for line in fileIn:
            authURL, projectName, projectDomain, username, userDomain, password = line.strip().split(',')
            fileNo += 1 # increases counter by one
            
            if fileNo >= 1 and fileNo <= 9:
                filename = 'admin0' + str(fileNo) + '.rc'
            else:
                filename = 'admin' + str(fileNo) + '.rc'
            
            rcInfo(filename, authURL, projectName, projectDomain, username, userDomain, password)
    
    print(f'{fileNo} admin.rc files have been created')

main()
