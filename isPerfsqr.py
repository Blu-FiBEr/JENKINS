#!/usr/bin/python3

def isSqr(n):    
    i = 1
    while(i*i<= n):    
        if ((n % i == 0) and (n / i == i)):
            return True    
        i = i + 1
    return False
