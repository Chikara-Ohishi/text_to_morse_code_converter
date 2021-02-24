# Text to Morse Code Converter

LOGO = """
######## #######  ##   ##  ########          ########  #####            ##   ##   #####   ######    #####   #######            #####    #####   ######   #######
#  ##  #  ##  ##   ## ##   #  ##  #          #  ##  # ##   ##           ### ###  ##   ##   ##  ##  ##   ##   ##  ##           ##   ##  ##   ##   ##  ##   ##  ##
   ##     ##        ###       ##                ##    ##   ##           #######  ##   ##   ##  ##  ##        ##               ##       ##   ##   ##  ##   ##
   ##     ####       #        ##                ##    ##   ##           ## # ##  ##   ##   #####    #####    ####             ##       ##   ##   ##  ##   ####
   ##     ##        ###       ##                ##    ##   ##           ##   ##  ##   ##   ####         ##   ##               ##       ##   ##   ##  ##   ##
   ##     ##  ##   ## ##      ##                ##    ##   ##           ##   ##  ##   ##   ## ##   ##   ##   ##  ##           ##   ##  ##   ##   ##  ##   ##  ##
  ####   #######  ##   ##    ####              ####    #####            ##   ##   #####   ###  ##   #####   #######            #####    #####   ######   #######
"""

MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}


def converter(input_text):
    coded_string = ""
    for char in list(input_text):
        code = MORSE_CODE.get(char.upper())
        # print(f"{char}: {code}")

        # leave space as it is
        if char == " ":
            code = ""

        if code != None:
            coded_string += code + " "

    return coded_string


print(LOGO)
text = input("Please input text(A-Z, 0-9)\n")
coded_text = converter(text)
print(f"Morse Code: {coded_text}")
