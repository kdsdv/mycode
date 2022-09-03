#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    """List - simple list"""
    # create a list called list1
    list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]

    # display list1
    print("list1:", list1)

    """List - making selections from a list using an index"""
    # display list1[1] which should only display arista_eos
    print("list1[1]:", list1[1])


    """LIST - EXTEND VS APPEND METHODS"""
    """List - using the extend method"""
    # create a new list containing a single item
    list2 = ["juniper"]

    # extend list1 by list2 (combine both lists together into a single list)
    list1.extend(list2)

    # display list1, which now contains juniper
    print("new combined list1:", list1)

    """List - using the append method"""
    # create list3
    list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
    
    # use the append operation to append list1 by list3
    list1.append(list3)
    
    # display the new complex list1
    print("new complex list1:", list1)

    # display value of item 5 in list1 which should only display the list of IP addresses
    print("list1[4]:", list1[4])

    # display the first IP address
    print("first IP address:", list1[4][0])

main()

