import sys
import os
from src.programa import *

args = sys.argv[1:]

while True:
    menu()
    escolha = input("").lower()[0]
    
    match escolha:
        case "c":
            user = cadastro(args[1], args[2], args[3])
        
        case "l":
            pass
        
        case "a":
            pass
        
        case "s":
            break
        
        case "d":
            pass
        
        case "e":
            elefante()
            
        case _:
            pass
