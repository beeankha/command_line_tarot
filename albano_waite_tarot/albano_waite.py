import argparse
import ascii_art
import constants
import card_directory
import card_meanings
import random
import re
import sys
import time

from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(
    prog="albano-waite",
    description="A command line tarot reader based on the Albano-Waite deck!",
    formatter_class=RawTextHelpFormatter,
    epilog="Happy tarot-ing! 😄"
    )
group = parser.add_mutually_exclusive_group()

parser.add_argument("card",
                    nargs="?",
                    default=constants.default_count,
                    choices=[None],
                    help="Pass in no args for a single card reading"
                    )

parser.add_argument("-i", "--interpretation",
                    default=False,
                    action="store_true",
                    help="""
    When invoked, this flag will display the meaning of
    the cards.
                    """,
                    )

parser.add_argument("-a", "--art",
                    default=False,
                    action="store_true",
                    help="""
    Invoke this flag to show the card's art.
                    """,
                    )

group.add_argument("-fd", "--free_draw",
                    type=int,
                    dest="free",
                    nargs="?",
                    const=constants.default_count,
                    metavar="",
                    help="""
    'Free Draw'\n
    Read a specific number of cards
    (passed as an integer after the '-fd'
    flag; defaults to a single-card pull)
                    """,
                    required=False,
                )

group.add_argument("-s", "--seen_heard_held",
                    help="""
    'Seen Heard Held'\n
    A 4-card spread which reveals:
    Card 1 - What needs to be seen
    Card 2 - What needs to be heard
    Card 3 - What needs to be held
    Card 4 - Action to be taken\n
    Optional: Pull a single card afterwards as a clarifier
                    """,
                    dest="seen",
                    action="store_true",
                    required=False,
                    )

group.add_argument("-cm", "--card_meaning",
                    type=int,
                    nargs="?",
                    default=constants.default_meaning,
                    help="""
    Display the meaning of a specific card via
    the assigned ID number (e.g., "-cd 0" will
    look up '(0) The Fool')
    \n
    Note: IDs range in number from 0 to 77
                    """,
                    choices=range(0,78),
                    dest="meaning",
                    metavar="",
                    required=False,
                    )

args = parser.parse_args()


reading = list(card_directory.card_dict.values())


# Great debugging print statement to see what args are invoked + what their values are!
# print(args)

list_index = list(card_meanings.meanings.keys())

if args.seen:
    args.card = None
    cards = random.sample(reading, k=constants.seen)
    for i in range(len(cards)):
        index = int(re.search(r'\((.*?)\)', cards[i]).group(1))
        if args.interpretation is False and args.art is True:
            print("...generating card art...")
            time.sleep(2)
            print(f"\n{ascii_art.card_art[index]}\n")
    time.sleep(1)
    print(f"\n👁 To Be Seen 👁\n{cards[0]}")
    time.sleep(1.5)
    print(f"\n👂 To Be Heard 👂\n{cards[1]}")
    time.sleep(1.5)
    print(f"\n🫂 To Be Held 🫂\n{cards[2]}")
    time.sleep(1.5)
    print(f"\n💫 Action 💫\n{cards[3]}")
    time.sleep(1)
    for i in range(len(cards)):
        index = int(re.search(r'\((.*?)\)', cards[i]).group(1))
        if args.interpretation is True and args.art is False:
            print("...interpreting...")
            time.sleep(2)
            print(f"\n{card_meanings.meanings[index]}\n")
        if args.interpretation is True and args.art is True:
            print("...interpreting and generating card art...")
            time.sleep(2)
            print(f"\n{ascii_art.card_art[index]}\n")
            print(f"\n{card_meanings.meanings[index]}\n")

elif args.card == 1 and args.meaning is None:
    print("You need to specify a card ID! (choose between 0 and 77)")

elif args.card == 1 and args.meaning < 78:
    meaning = list_index.index(args.meaning)
    card = str(card_directory.card_dict[args.meaning])
    if args.art is True:
        time.sleep(1)
        print(f"Displaying card art for: {card}")
        time.sleep(2)
        print(f"\n{ascii_art.card_art[meaning]}\n")
        time.sleep(3)
    print(f"...looking up meaning for: {card}")
    time.sleep(2)
    print(f"\n{card_meanings.meanings[meaning]}\n")

elif args.card == 1 and (args.free is None or args.free == 1):
    cards = random.sample(reading, k=args.card)
    index = int(re.search(r'\((.*?)\)', cards[0]).group(1))
    args.free = None
    time.sleep(1)
    print(f"\n✨ Your single card drawing is: ✨")
    time.sleep(1.5)
    print(*cards, sep = "\n")
    if args.interpretation is False and args.art is True:
        time.sleep(1.5)
        print("...generating card art...")
        time.sleep(2)
        print(f"\n{ascii_art.card_art[index]}\n")
    if args.interpretation is True and args.art is False:
        time.sleep(1.5)
        print("...looking up interpretation...")
        time.sleep(2)
        print(f"\n{card_meanings.meanings[index]}\n")
    if args.interpretation is True and args.art is True:
        time.sleep(1.5)
        print("...interpreting and generating card art...")
        time.sleep(2)
        print(f"\n{ascii_art.card_art[index]}\n")
        print(f"\n{card_meanings.meanings[index]}\n")

elif args.free > 1:
    cards = random.sample(reading, k=args.free)
    print(f"\n✨ You have pulled the following {args.free} cards: ✨\n")
    time.sleep(1.5)
    print(*cards, sep = "\n")
    print("\r")
    for i in range(len(cards)):
        index = int(re.search(r'\((.*?)\)', cards[i]).group(1))
        if args.interpretation is True and args.art is False:
            print("...interpreting...")
            time.sleep(2)
            print(f"\n{card_meanings.meanings[index]}\n")
        if args.interpretation is True and args.art is True:
            print("...interpreting and generating card art...")
            time.sleep(2)
            print(f"\n{ascii_art.card_art[index]}\n")
            print(f"\n{card_meanings.meanings[index]}\n")
        if args.interpretation is False and args.art is True:
            print("...generating card art...")
            time.sleep(2)
            print(f"\n{ascii_art.card_art[index]}\n")
