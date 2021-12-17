from init_attrs_with_kwargs import InitAttrsWKwArgs


class Hoge(InitAttrsWKwArgs):
    count: int
    name: str
    max_length: int


# Initialize from docopt's return value (dict).
v1: Hoge = Hoge(**{'<count>': 1, '--name': "Joe", '--max-length': 100})

print("dir(v1)=%s" % repr(dir(v1)))
print("v1.count=%s" % repr(v1.count))
print("v1.name=%s" % repr(v1.name))
print("v1.max_length=%s" % repr(v1.max_length))

# Initialize with keyword argument.
v2: Hoge = Hoge(count=10, name='Jane', max_length=99)

print("dir(v2)=%s" % repr(dir(v2)))
print("v2.count=%s" % repr(v2.count))
print("v2.name=%s" % repr(v2.name))
print("v2.max_length=%s" % repr(v2.max_length))

# Initialize from docopt's return value, with casting str to int
v3: Hoge = Hoge(_cast_str_values=True, **{'<count>': '1', '--name': "Joe", '--max-length': '100'})

print("dir(v3)=%s" % repr(dir(v3)))
print("v3.count=%s" % repr(v3.count))
print("v3.name=%s" % repr(v3.name))
print("v3.max_length=%s" % repr(v3.max_length))
