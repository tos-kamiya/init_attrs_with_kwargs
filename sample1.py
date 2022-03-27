from enum import Enum
from init_attrs_with_kwargs import cast_set_attrs


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class MyArgs:
    count: int
    name: str
    max_length: int
    color: Color


# Initialize from docopt's return value, with casting str to int.
v3 = cast_set_attrs(MyArgs(), **{"<count>": "1", "--name": "Joe", "--max-length": "100", "--color": "RED"})

print("dir(v3)=%s" % repr(dir(v3)))
print("v3.count=%s" % repr(v3.count))
print("v3.name=%s" % repr(v3.name))
print("v3.max_length=%s" % repr(v3.max_length))
print("v3.color=%s" % repr(v3.color))

# Options and positional arguments are fine as long as their names do not conflict.
v4 = cast_set_attrs(MyArgs(), **{"--count": "1", "<name>": "Joe", "--max_length": "100", "-color": "RED"})

print("dir(v4)=%s" % repr(dir(v4)))
print("v4.count=%s" % repr(v4.count))
print("v4.name=%s" % repr(v4.name))
print("v4.max_length=%s" % repr(v4.max_length))
print("v4.color=%s" % repr(v4.color))

# # Error checking
# cast_set_attrs(MyArgs(), **{'--nam': "Joe"})  # raises KeyError: "attribute `'nam'` not found in class `<class '__main__.MyArgs'>`"
# cast_set_attrs(MyArgs(), **{'<count>': "vii"})  # raises ValueError: invalid literal for int() with base 10: 'vii'
# cast_set_attrs(MyArgs(), **{'--color': "GLAY"})  # raises ValueError: Invalid Enum name: 'GLAY'
# cast_set_attrs(MyArgs(), **{'---x': "vii"})  # raises NameError: Invalid name for option or positional argument: '---x'
