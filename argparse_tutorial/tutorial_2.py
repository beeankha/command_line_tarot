import argparse

parser = argparse.ArgumentParser(description="Calculate X to the power of Y!")
group = parser.add_mutually_exclusive_group()

group.add_argument("-v", "--verbosity",
                    action="count",
                    default=0
                    )

group.add_argument("-q", "--quiet",
                   action="store_true",
                   )

parser.add_argument("x",
                    type=int,
                    help="The base number"
                    )

parser.add_argument("y",
                    type=int,
                    help="The exponent"
                    )

args = parser.parse_args()
answer = args.x ** args.y

if args.quiet:
    print(answer)
elif args.verbosity:
    print(f"{args.x} to the power of {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")
