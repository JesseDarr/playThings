import threading
import socket
import sys
from multiprocessing import Pool, cpu_count
from itertools import repeat

def getUserInput():
    address = input("Enter IP or DNS address to scan: ")
    print("You can enter a single port, a hypenated range (1-1024), or a list of ports (80,443,4433)")
    inputPortRange = input("Enter port(s) to scan: ")

    ### Input parsing and sanitization for different port range input syntaxes ###
    # if single port is entered and numbers are in range 0 - 65535
    if inputPortRange.isdigit() and int(inputPortRange) > 0 and int(inputPortRange) <= 65535:
        ports = [int(inputPortRange)]
    # if single "-" and numbers on each side of it
    elif inputPortRange.count("-") == 1 and all([x.isdigit() for x in inputPortRange.split("-")]):
        # if numbers are in range 0 - 65535
        if int(inputPortRange.split("-")[0]) > 0 and int(inputPortRange.split("-")[1]) <= 65535:
            # if 1st number is < 2nd number
            if int(inputPortRange.split("-")[0]) < int(inputPortRange.split("-")[1]):
                ports = list(range(int(inputPortRange.split("-")[0]),int(inputPortRange.split("-")[1]) + 1))
            else: print("Invalid input...exiting"); sys.exit()
        else: print("Invalid input...exiting."); sys.exit()
    # if there is atleast 1 "," and everything else are numbers        
    elif inputPortRange.count(",") >= 1 and all([x.isdigit() for x in inputPortRange.split(",")]):
        # if each number is in range 0 - 65535
        if all([int(x) > 0 and int(x) <= 65535 for x in inputPortRange.split(",")]):
            ports = [int(x) for x in inputPortRange.split(",")]
        else: print("Invalid input...exiting."); sys.exit()
    else: print("Invalid input...exiting."); sys.exit()
                
    return (address, ports)

def portScan(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        #### maybe put time stuff in here to show how fast we got a response on open ports ####
        result = s.connect_ex((address, port)) # (( )) b/c s.connect expects a tuple input...odd
        if result == 0:
            print(f"{port}: open")
        s.shutdown # stops communication, makes the next line's behavior instant
        s.close()
    except Exception as e: 
        print(e.__class__)  # print error class
        print(str(e))       # prints string of error

if __name__ == "__main__":
    input = getUserInput()

    with Pool(cpu_count() * 2) as p: 
        p.starmap(portScan, zip(repeat(input[0]), input[1]))
    p.terminate()
    p.join() # avoids zombie processes
    