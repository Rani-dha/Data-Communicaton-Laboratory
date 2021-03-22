import ipaddress  # Importing the ipaddress
import math       # Importing the Math module 

ipAdd = input("Enter the IP address:") # Enter the IP Address
i = ipAdd.split("/") # Splitting the IP address by  "/"

pre = i[1]
power = 32-int(pre)
val = math.pow(2,int(power))     # Calculating the Address space using formula

ntwk = ipaddress.IPv4Network(ipAdd) # Storing the Address using IPv4 Network
firstAdd, lastAdd = ntwk[1],ntwk[-1]  # Assigning the First and Last Address 

print("ADDRESS BLOCK", int(val)) # Printing the Address space 
print("FIRST ADDRESS", firstAdd) # Printing the First Address
print("LAST ADDRESS", lastAdd)   # Printing the Last Address
