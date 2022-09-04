''' Python Basics
    Lab 44: Producing Graphs and Charts
    PIE MAKER (piemaker.py) | kdsdv '''

#!/usr/bin/env python3
import matplotlib.pyplot as plot  # access to matplotlib and renaming it as plot

# Function to get wedge's size from file
def getSize():
    stats = {}  # create dictionary
    sizeList= []  # create list

    # opens and reads file to retrieve wedge's data, assigns respective key-value-pair in dictionary,
    # converts wedge's size to float, and creates list for wedge's size
    with open('/home/student/mycode/graphing/2022animestats.txt', 'r') as fileIn:        
        for line in fileIn:
            label, size = line.strip().split(':')
            size = float(size)
            stats[label] = size
            sizeList.append(stats[label])

    return sizeList  # returns list of wedge's size

# Function to get wedge's label from file
def getLabel():
    stats = {}  # create dictionary
    labelList= []  # create list

    # opens and reads file to retrieve wedge's data, assigns respective key-value-pair in dictionary,
    # converts wedge's size to float, and creates list for wedge's label
    with open('/home/student/mycode/graphing/2022animestats.txt', 'r') as fileIn:
        for line in fileIn:
            label, size = line.strip().split(':')
            size = float(size)
            stats[label] = size

        for label in stats.keys():
            labelList.append(label)

    return tuple(labelList)  # returns tuple of wedge's label

# Program that creates a pie chart from a text file
def main():
    print('PIE MAKER (piemaker.py)')  # displays message to screen

    # wedge data  to make the pie
    size = getSize()  # call getSize function to get wedge's size
    explode = (0, 0.1, 0, 0, 0)  # offset second wedge
    label = getLabel()  # call getLabel function to get wedge's label
    color=['orchid', 'lightcoral', 'wheat', 'lightgreen', 'lightblue']  #  wedge's color
    title = '2022 ANIME STATISTICS\nAnime Sales Exported Content retrieved 09/01/2022'
    title = title + '\nfrom https://fictionhorizon.com/how-many-people-watch-anime/'

    # plot the pie
    plot.pie(size, explode=explode, labels=label, colors=color, autopct='%1.0f%%', shadow=True, startangle=45)
    plot.title(title, fontsize=8)
    plot.axis('equal')

    # saves a pdf copy locally and to "~/static" (the "files" view)
    plot.savefig("/home/student/mycode/graphing/2022animestats.pdf")
    plot.savefig("/home/student/static/2022animestats.pdf")

    # saves a png copy locally and to "~/static" (the "files" view)
    plot.savefig("/home/student/mycode/graphing/2022animestats.png")
    plot.savefig("/home/student/static/2022animestats.png")

    print('Finished making the pie!')  # display message to screen when the pie chart has been created

main()
