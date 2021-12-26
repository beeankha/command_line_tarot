import argparse
import constants
import card_directory
import random

from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="A command line tarot reader!",
    formatter_class=RawTextHelpFormatter
    )

parser.add_argument("card",
                    nargs="?",
                    default=constants.default_count,
                    choices=[None],
                    help="Pass in no args for a single card reading"
                    )


parser.add_argument("-fd", "--free_draw",
                    type=int,
                    nargs="?",
                    const=constants.default_count,
                    help="""
    'Free Draw'\n
    Read a specific number of cards
    (passed as an integer after the '-fd'
    flag; defaults to a single-card pull)
                    """,
                    required=False,
                )

parser.add_argument("-s", "--seen",
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

parser.add_argument("-cm", "--card_meaning",
                    type=int,
                    nargs="?",
                    default=None,
                    help="Display the meaning of a specified card",
                    required=False,
                    )


parser.add_argument("-cd", "--card-directory",
                    type=int,
                    nargs="?",
                    default=None,
                    help="Display the meaning of a specified card",
                    required=False,
                    )


args = parser.parse_args()

reading = [card_directory.card_dict[k] for k in card_directory.card_dict]
cards = random.sample(reading, k=args.card)

# Great debugging print statement to see what args are invoked + what their values are!
# print(args)

if args.seen:
    args.card = None
    cards = random.sample(reading, k=constants.seen)
    print("""
    \r👁 To Be Seen 👁\n{0}\n\n👂 To Be Heard 👂\n{1}
    \n🫂 To Be Held 🫂\n{2}\n\n💫 Action 💫\n{3}\n""".format(cards[0], cards[1], cards[2], cards[3]))
elif args.card == 1 and (args.free_draw is None or args.free_draw == 1):
    args.free_draw = None
    print(f"\n✨ Your single card drawing is: ✨")
    print(*cards, sep = "\n")
    print("\r")
elif args.free_draw > 1:
    cards = random.sample(reading, k=args.free_draw)
    print(f"\n✨ You have pulled the following {args.free_draw} cards: ✨\n")
    print(*cards, sep = "\n")
    print("\r")
