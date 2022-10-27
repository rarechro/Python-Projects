
from colorama import Fore, Back, Style

eyechar = input("Choose your Eye character.   ")
mouthchar = input("Choose your mouth character.   ")
durationN = input('')

def smileyface(eyes, mouth, duration):
    eyes = str(eyechar)
    mouth = str(mouthchar)
    duration = int(duration)
    spacing = ("                    ")
    for x in range(duration):
        print(2*(spacing), eyes, spacing, eyes, '\n\n', 2*(spacing), 2*(mouth), spacing, 2*(mouth), '\n',2*(spacing),mouth,spacing, mouth, '\n',2*(spacing), 21*(mouth))
        
    
smileyface(eyechar, mouthchar, duration);
yeet = input('press enter to close ;)')