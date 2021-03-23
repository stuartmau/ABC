# The alphabet A-Z, a-z with an animated transition.
# Press a to go to the next letter.
# Press b to go back to A.
# Touch logo to change case.

from microbit import *

# Load alphabet
alphabet = []
case = 'A'
caseOffset = 0

for index in range(0, 26):
    letter = chr(ord('A') + index)
    pixels = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] 
    display.show(letter, wait=False, clear=False)
    for x in range(0, 5):
        for y in range(0, 5):
            pixels[x][y] = display.get_pixel(x, y)
    alphabet.insert(index, pixels)
    sleep(1000/16)
    
    letter = chr(ord('a') + index)
    pixels = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] 
    display.show(letter, wait=False, clear=False)
    for x in range(0, 5):
        for y in range(0, 5):
            pixels[x][y] = display.get_pixel(x, y)
    alphabet.insert(index + 26, pixels)
    sleep(1000/16)

# Animation function
def animate(letterB):
    
    # sweep to right
    for x in range(0, 4):
        for y in range(0, 5):
            if display.get_pixel(x, y) > 0:
                display.set_pixel(x, y, 0)
                display.set_pixel(x+1, y, 9)
        sleep(1000/20)
    sleep(1000/5)
            
    # fad in on right if not on
    for value in range(0, 10):
        for y in range(0, 5):
            if display.get_pixel(4, y) < value:
                display.set_pixel(4, y, value)
        sleep(1000/100)    

    pixels = alphabet[ord(letterB) - ord(case) + caseOffset]
    # sweep to right leaving prev column on as needed
    for index in range(0, 5):
        x = 4 - index 
        for y in range(0, 5):
            if x >= 0:
                display.set_pixel(x, y, 9)
            if x < 4:
                value = pixels[x+1][y]
                if value > 0:
                    display.set_pixel(x+1, y, 9)
                else:
                    display.set_pixel(x+1, y, 0)
        sleep(1000/60)

    # fade out left column if not on
    for value in range(9, -1, -1):
        x = 0
        for y in range(0, 5):
            cur = display.get_pixel(x, y)
            target = pixels[x][y]
            if cur > max(value, target):
                display.set_pixel(x, y, value)
        sleep(1000/100)    

# Reset to A
letter = chr(ord(case))
animate(letter)
index = 0

# Main loop.
while True:
    if button_a.is_pressed():
        index = 0
        letter = chr(ord(case) + index)
        animate(letter)
    elif button_b.is_pressed():
        index = (index + 1) % 26
        letter = chr(ord(case) + index)
        animate(letter)
    elif pin_logo.is_touched():
        if case is 'A':
            case = 'a'
            caseOffset = 26
        else:
            case = 'A'
            caseOffset = 0
        letter = chr(ord(case) + index)
        animate(letter)


