# This is a collection of utility scripts in Python

## String to list
This script converts a string indicating a range of values into a list: `"19-21,22,25"` => [19,20,21,22,25]. It also sorts the values in ascending order. This script can also be called from the command line:

`$ python3 string_to_list.py 12-13,15,20`
`[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 5]`

It handles negative values, misformatted ranges, and negative ranges. 