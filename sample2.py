from typing import *

from docopt import docopt
from init_attrs_with_kwargs import InitAttrsWKwArgs


class MyArgs(InitAttrsWKwArgs):
    maximum: bool
    minimum: bool
    average: bool
    number: List[float]


__doc__ = '''Get total of numbers.

Usage:
  sample2 [--maximum|--minimum|--average] <number>...

Options:
  --maximum, -M     Get the largest number.
  --minimum, -m     Get the smallest number.
  --average, -a     Get the average of the numbers.
'''


def main():
    args: MyArgs = MyArgs(_cast_str_values=True, **docopt(__doc__))
    # print("args=%s" % args)
    if args.maximum:
        print(max(args.number))
    elif args.minimum:
        print(min(args.number))
    else:
        t = sum(args.number)
        if args.average:
            print(t / len(args.number))
        else:
            print(t)


if __name__ == '__main__':
    main()
