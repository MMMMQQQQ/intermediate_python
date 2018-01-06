import argparse
import sys

def main():
    # because the AugmentParser is in capital for the first letter of the two words, so it is a class, then parser is an object of argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? ()add, sub, mul, or div')
    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))


def calc(args):
    operation=args.operation
    x=args.x
    y=args.y
    if operation=='add':
        return x+y
    if operation=='sub':
        return x-y
    if operation=='mul':
        return x*y
    if operation=='div':
        return x/y

if __name__=='__main__':
    main()

