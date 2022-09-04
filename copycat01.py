#!/usr/bin/env python3
"""Python Basics
   Lab 22: Copying Files and Folders
   CHALLANGE 01 | kdsdv"""

# access shutil and os to move around or organize files on the local system 
import shutil
import os

def main():
    """CHALLANGE 01: Rewrite the script, ~/mycode/copycat01.py,
    so it adheres to the best pratice standards."""

    # move to the working directory
    os.chdir("/home/student/mycode/")

    # copy fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy entire directoryA to directoryB
    shutil.copytree("5g_research/", "5g_research_backup/")

main()

