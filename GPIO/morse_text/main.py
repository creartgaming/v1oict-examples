from machine import Pin
import time

gpio_pin = Pin(20, Pin.OUT)


def pulse(pin, high_time, low_time):

    pin.value(1)
    time.sleep(high_time)
    pin.value(0)
    time.sleep(low_time)


def morse(pin, dot_length, text):

    for x in text:
        if x == '.':
            pulse(pin, dot_length, dot_length * 2)
        elif x == '-':
            pulse(pin, dot_length * 3, dot_length * 2)
        elif x == ' ':
            pulse(pin, dot_length * 0, dot_length * 6)


def morse_text(pin, dot_length, text):
    """
    Laat de string s horen als morse code.
    De pin_nr is de pin die gebruikt wordt.
    De text mag de volgende characters bevatten: lowercase letters, spatie.
    De dot_length is de lengte van een punt (dot).
    De lengte van de andere characters wordt daar van afgeleid.
    """

    # implementeer deze functie

    morse_code_lijst = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ', ': '--..--', '.': '.-.-.-',
                       '?': '..--..', '/': '-..-.', '-': '-....-',
                       '(': '-.--.', ')': '-.--.-', ' ': '  '}

    morse_text_string = ''

    for x in text.upper():
         morse_text_string += morse_code_lijst[x]

    morse(pin, dot_length, morse_text_string)

morse_text(gpio_pin, 0.2, "sos")
