from typing import *

from docopt import docopt
from init_attrs_with_kwargs import cast_set_attrs


class MyArgs:
    compile: bool
    run: bool
    program: Optional[str]
    verbose: bool


__doc__ = """Compile and run a program.

Usage:
  sample3 compile [options] <program>
  sample3 run [options] [<program>]

Options:
  --verbose, -v     Verbose.
"""


def main():
    args = cast_set_attrs(MyArgs(), **docopt(__doc__))
    # print("args=%s" % args)
    if args.compile:
        assert args.program is not None
        print("Compile the source file: %s" % args.program)
    elif args.run:
        if args.program is None:
            args.program = "a.out"
        print("Run program: %s" % args.program)
    else:
        assert False


if __name__ == "__main__":
    main()
