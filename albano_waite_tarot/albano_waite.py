import argparse
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
    args.card = None
    cards = random.sample(reading, k=constants.seen)
    print(cards)
    print("""
    \r👁 To Be Seen 👁\n{0}\n\n👂 To Be Heard 👂\n{1}
    \n🫂 To Be Held 🫂\n{2}\n\n💫 Action 💫\n{3}\n""".format(cards[0], cards[1], cards[2], cards[3]))
elif args.card == 1 and args.meaning is None:
    print("You need to specify a card ID!")
elif args.card == 1 and args.meaning < 78:
    meaning = list_index.index(args.meaning)
    print(f"\n{card_meanings.meanings[meaning]}\n")
elif args.card == 1 and (args.free is None or args.free == 1):
    cards = random.sample(reading, k=args.card)
    index = int(re.search(r'\((.*?)\)', cards[0]).group(1))
    args.free = None
    print(index)
    print(f"\n✨ Your single card drawing is: ✨")
    print(*cards, sep = "\n")
    print(f"\n{card_meanings.meanings[index]}\n")
elif args.free > 1:
    cards = random.sample(reading, k=args.free)
    print(f"\n✨ You have pulled the following {args.free} cards: ✨\n")
    print(*cards, sep = "\n")
    print("\r")
