# roman-num
The script `roman.py` contains a class definition to use roman numerals in python.
To use it, import the class with:

```python
from roman import Roman
```

To create a roman numeral object use `Roman(value)` where `value` is either a valid string, or an integer.
Once a `Roman` object is created, its decimal equivalent can be retrieved in is attribute `decimal` and the roman string it represents throught the attribute `roman`.
Binary operations work with `Roman` objects and return `Roman` object. The division operand (`/`) performs integer division on `Roman` objects, equivalent to the `//` operand.

Use example:
```
>>> from roman import Roman
>>>
>>> r = Roman(14)
>>> r.roman
'XIV'
>>> r.decimal
14
>>> p = Roman("VI")
>>> p
VI
>>> p + r
XX
>>> r / p
II
>>> r > p
True
```