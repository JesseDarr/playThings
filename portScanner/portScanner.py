import threading
import socket
import time

def getUserInput():
    address = input("Enter IP or DNS address to scan:")
    inputPortRange = input("Enter port range to scan, e.g. 1-1024: ")

    # if inputPortRange (contains only numbers and a single hyphen) make minPort and Max Port
    # else if inputPortRange contains only 1 number set minPort to it
    # else throw error that input is bad

    return address

### Need to add threading to this
def portScan(ipAddress, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        #### maybe put time stuff in here to show how fast we got a response on open ports ####
        result = s.connect_ex((ipAddress, port)) # (( )) b/c s.connect expects a tuple input...odd
        if result == 0:
            print(f"{port}: open")
        s.shutdown # stops communication, makes the next line's behavior instant
        s.close()
    except Exception as e: 
        print(e.__class__)  # print error class
        print(str(e))       # prints string of error

if __name__ == "__main__":
    ### need to handle pushing
    portScan(getUserInput(), 442)