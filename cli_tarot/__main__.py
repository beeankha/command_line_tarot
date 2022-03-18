import argparse
import random
import re
import sys
import time

from . import ascii_art
from . import constants
from . import card_directory
from . import card_meanings

from argparse import RawTextHelpFormatter

def main():
    parser = argparse.ArgumentParser(
        prog="cli-tarot",
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

    group.add_argument("-cc", "--celtic_cross",
                        help="""
        'Celtic Cross'\n
        A 10-card spread which reveals:
        Card 1 - The present condition of the querent
        Card 2 - Immediate influence / obstacles
        Card 3 - Goal / destiny according to existing circumstances
        Card 4 - Distant past foundation
        Card 5 - Recent past events
        Card 6 - Future influence
        Card 7 - The questioner
        Card 8 - Environmental factors
        Card 9 - Inner emotions
        Card 10 - Final results\n
                        """,
                        dest="celtic",
                        action="store_true",
                        required=False,
                        )

    group.add_argument("-ppf", "--past_present_future",
                        help="""
        'Past, Present, and Future'\n
        A 3-card spread which reveals:
        Card 1 - Past
        Card 2 - Present
        Card 3 - Future\n
        Optional: Pull a single card afterwards as a clarifier
                        """,
                        dest="ppf",
                        action="store_true",
                        required=False,
                        )

    group.add_argument("-ch", "--choices",
                        help="""
        'Choices'\n
        A 3-card spread which reveals:
        Card 1 - Choice 1
        Card 2 - Choice 2
        Card 3 - Advice\n
        Optional: Pull a single card afterwards as a clarifier
                        """,
                        dest="choices",
                        action="store_true",
                        required=False,
                        )

    group.add_argument("-cm", "--card_meaning",
                        type=int,
                        nargs="?",
                        default=constants.default_meaning,
                        help="""
        Display the meaning of a specific card via
        the assigned ID number (e.g., "-cm 0" will
        look up the meaning for '(0) The Fool')
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

    # TODO: Celtic Cross Reading

    # TODO: Past, Present, Future Spread

    # TODO: Choices Spread

    elif args.card == 1 and args.meaning is None:
        print("You need to specify a card ID! (choose between 0 and 77)")

    elif args.card == 1 and args.meaning < 78:
        meaning = list_index.index(args.meaning)
        card = str(card_directory.card_dict[args.meaning])
        if args.art is True:
            time.sleep(1)
            print(f"\nDisplaying card art for:\n{card}")
            time.sleep(2)
            print(f"\n{ascii_art.card_art[meaning]}\n")
            time.sleep(2)
        print(f"\n...looking up meaning for:\n{card}")
        time.sleep(2)
        print(f"{card_meanings.meanings[meaning]}\n")

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
