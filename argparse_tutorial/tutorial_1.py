import argparse


# Following instructions found here https://docs.python.org/3/howto/argparse.html

parser = argparse.ArgumentParser()

parser.add_argument("square",
                    type=int,
                    help="Display the square of any given number"
                    )

parser.add_argument("-v", "--verbose",
                    # type=int,
                    # choices=[0,1,2],  # (this is the way to do stuff if you want specific options vs a count)
                    action="count",
                    default=0,
                    help="Increase output verbosity"
                    )


args = parser.parse_args()
answer = args.square ** 2

# bugfix: replace == with >=
if args.verbose >= 2:
    print(f"The square of {args.square} equals {answer}")
elif args.verbose >= 1:
    print(f"{args.square}^2 == {answer}")

else:
    print(answer)
