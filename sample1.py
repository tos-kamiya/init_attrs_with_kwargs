from enum import Enum
from init_attrs_with_kwargs import InitAttrsWKwArgs


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class MyArgs(InitAttrsWKwArgs):
    count: int
    name: str
    max_length: int
    color: Color

# Initialize with keyword argument.
v2: MyArgs = MyArgs(count=10, name='Jane', max_length=99, color=Color.RED)

print("dir(v2)=%s" % repr(dir(v2)))
print("v2.count=%s" % repr(v2.count))
print("v2.name=%s" % repr(v2.name))
print("v2.max_length=%s" % repr(v2.max_length))
print("v2.color=%s" % repr(v2.color))

# Initialize from docopt's return value, with casting str to int
v3: MyArgs = MyArgs(_cast_str_values=True, **{'<count>': '1', '--name': "Joe", '--max-length': '100', '--color': 'RED'})

print("dir(v3)=%s" % repr(dir(v3)))
print("v3.count=%s" % repr(v3.count))
print("v3.name=%s" % repr(v3.name))
print("v3.max_length=%s" % repr(v3.max_length))
print("v3.color=%s" % repr(v3.color))

# Error checking
# MyArgs(_cast_str_values=True, **{'--nam': "Joe"})  # raises NameError
# MyArgs(_cast_str_values=True, **{'<count>': "vii"})  # raises ValueError
# MyArgs(_cast_str_values=True, **{'---x': "vii"})  # raises ValueError
