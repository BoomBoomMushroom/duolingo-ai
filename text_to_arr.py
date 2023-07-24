import numpy
import string

# Mainly Swedish characters because I want it to learn swedish!
CHARACTERS = " abcdefghijklmnopqrstuvwxyzåäö" + string.digits + string.punctuation + "“”"
DEFAULT_LEN = 200

def convertString(input, length=DEFAULT_LEN):
    arr = numpy.full(length, -1, dtype=int)
    if len(input) > length: return arr
    
    i = 0
    for j in input:
        arr[i] = CHARACTERS.index( j.lower() )
        i += 1
    
    return arr

if __name__ == "__main__":
    convertString("Which one of these is “milk”? mjölk kaffe vatten")
    #print( [*CHARACTERS] )