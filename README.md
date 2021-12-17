# init_attrs_with_kwargs
A helper for type-checked command-line argument store

## Sample

```python
from init_attrs_with_kwargs import InitAttrsWKwArgs

class MyArgs(InitAttrsWKwArgs):
    count: int
    name: str
    max_length: int

# Initialize from docopt's return value, with casting str to int
args: MyArgs = MyArgs(_cast_str_values=True, **{'<count>': '1', '--name': "Joe", '--max-length': '100'})

print("args.count=%s" % repr(args.count))
print("args.name=%s" % repr(args.name))
print("args.max_length=%s" % repr(args.max_length))
```

For more details, please refer to the [sample](https://github.com/tos-kamiya/init_attrs_with_kwargs/blob/main/sample1.py), which includes error handling.