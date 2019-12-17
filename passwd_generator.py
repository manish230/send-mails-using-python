import string
import random

## Function To Generate Random Password of 16 characters##
def pw_gen(size=16, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
        
file1 = open("file_name.txt","r")

## Using for loop to generate password for multiple users defined in file_name.txt ##

for i in file1: 
 print (pw_gen())

## Closing file ##
file1.close()
