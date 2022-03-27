init_attrs_with_kwargs
======================

A helper for type-checked command-line argument store.

Please refer to the [home page on the github](https://github.com/tos-kamiya/init_attrs_with_kwargs) for installation and usage.

## Sample

```python
from init_attrs_with_kwargs import cast_set_attrs

class MyArgs:
    count: int
    name: str
    max_length: int

# Initialize from docopt's return value, with casting str to int
args = cast_set_attrs(MyArgs(), **{'<count>': '1', '--name': "Joe", '--max-length': '100'})

print("args.count=%s" % repr(args.count))
print("args.name=%s" % repr(args.name))
print("args.max_length=%s" % repr(args.max_length))
```
