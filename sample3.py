from typing import *

from docopt import docopt
from init_attrs_with_kwargs import InitAttrsWKwArgs


class MyArgs(InitAttrsWKwArgs):
    compile: bool
    run: bool
    program: Optional[str]
    verbose: bool


__doc__ = """Run a script.

Usage:
  sample3 compile [options] <program>
  sample3 run [options] [<program>]

Options:
  --verbose, -v     Verbose.
"""


def main():
    args = MyArgs(_cast_str_values=True, **docopt(__doc__))
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
