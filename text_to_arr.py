import numpy
import string

# Mainly Swedish characters because I want it to learn swedish!
CHARACTERS = "abcdefghijklmnopqrstuvwxyzåäö " + string.digits + string.punctuation

if __name__ == "__main__":
    print( CHARACTERS.split("") )