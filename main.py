import sys
import os
from src.programa import *

while True:
    menu()
    escolha = input("").lower()[0]
    
    match escolha:
        case "c":
            pass
        
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
