#!/usr/bin/env python3
"""Python Basics
   Lab 23: Moving and Renaming Files and Folders
   CHALLENGE 01 | kdsdv"""

# access shutil and os to organize files on the local system
import shutil
import os

def main():
    """CHALLANGE 01: Add comments and adhere to best practice standards"""

    # start in the home directory
    os.chdir('/home/student/mycode/')

    # move file to directory
    shutil.move('raynor.obj', 'ceph_storage/')
    
    # prompt user for new filename for kerrigan.obj file
    xname = input('What is the new name for kerrigan.obj? ')

    # move current kerrigan.obj file to ceph_storage directory with new filename
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
   
main()
