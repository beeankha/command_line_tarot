import argparse
import ascii_art
import constants
import card_directory
import card_meanings
import random
import re
import sys

from argparse import RawTextHelpFormatter

print(sys.argv[0])
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


reading = [card_directory.card_dict[k] for k in card_directory.card_dict]


# Great debugging print statement to see what args are invoked + what their values are!
# print(args)

list_index = list(card_meanings.meanings.keys())

if args.seen:
    # TODO: Add in time breaks
    # TODO: Split up print statements so that art + interpretations
    # appear together with cards that are drawn
    args.card = None
    cards = random.sample(reading, k=constants.seen)
    print("""
    \r👁 To Be Seen 👁\n{0}\n\n👂 To Be Heard 👂\n{1}
    \n🫂 To Be Held 🫂\n{2}\n\n💫 Action 💫\n{3}\n""".format(cards[0], cards[1], cards[2], cards[3]))
    for i in range(len(cards)):
        index = int(re.search(r'\((.*?)\)', cards[i]).group(1))
        if args.interpretation is True and args.art is False:
            print(f"\n{card_meanings.meanings[index]}\n")
        if args.interpretation is True and args.art is True:
            print(f"\n{ascii_art.card_art[index]}\n")
            print(f"\n{card_meanings.meanings[index]}\n")
        if args.interpretation is False and args.art is True:
            print("Card art goes here.\n")
            print(f"\n{ascii_art.card_art[index]}\n")

elif args.card == 1 and args.meaning is None:
    print("You need to specify a card ID! (choose between 0 and 77)")

elif args.card == 1 and args.meaning < 78:
    # TODO: Add ability to display card art
    meaning = list_index.index(args.meaning)
    print(f"\n{card_meanings.meanings[meaning]}\n")

elif args.card == 1 and (args.free is None or args.free == 1):
    cards = random.sample(reading, k=args.card)
    index = int(re.search(r'\((.*?)\)', cards[0]).group(1))
    print(index)
    args.free = None
    print(f"\n✨ Your single card drawing is: ✨")
    print(*cards, sep = "\n")
    if args.art:
        print(f"\n{ascii_art.card_art[index]}\n")
    if args.interpretation:
        print(f"\n{card_meanings.meanings[index]}\n")

elif args.free > 1:
    # TODO: Add in ability to see interpretations and/or art
    cards = random.sample(reading, k=args.free)
    print(f"\n✨ You have pulled the following {args.free} cards: ✨\n")
    print(*cards, sep = "\n")
    print("\r")
