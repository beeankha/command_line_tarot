import time

from . import ascii_art
from . import card_meanings
from . import readings


timestr = time.strftime("%Y%m%d-%H%M%S")

def output_reading_only(reading_type, reading):
    with open(reading_type + timestr + '.txt', 'a') as output_file:
        output_file.write(f"{reading}")

def output_meaning(reading_type, card_index):
    with open(reading_type + timestr + '.txt', 'a') as output_file:
        output_file.write(f"{card_meanings.meanings[card_index]}\n" + "---\n")


def output_art(reading_type, card_index):
    with open(reading_type + timestr + '.txt', 'a') as output_file:
        output_file.write(f"{ascii_art.card_art[card_index]}\n" + "---\n")


def output_meaning_and_art(reading_type, card_index):
    with open(reading_type + timestr + '.txt', 'a') as output_file:
        output_file.write(f"{ascii_art.card_art[card_index]}\n" + f"{card_meanings.meanings[card_index]}\n" + "---\n")
