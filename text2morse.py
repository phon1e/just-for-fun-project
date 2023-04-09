#mapping morse - letter 
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

def encrypt(msg):
    output = ''
    msg = msg.upper()
    print(f"input : {msg} (uppercase)")
    for letter in msg:
        if letter != ' ':
            output += MORSE_CODE_DICT[letter] + ' '
        else:
            output += ' '

    return output


usrInput =  str(input("This is morse converter!\n Enter string "))
print(f"output: {encrypt(usrInput)}")

