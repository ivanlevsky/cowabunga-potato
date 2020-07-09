import re, unicodedata


def split_string_by_regex(regex, string):
    return list(filter(None, re.split(regex, string)))


def split_string_by_numbers(string_to_split, split_length):
    regex_pattern = '?'
    regex_pattern = regex_pattern.rjust(split_length+1,'.')
    return re.findall(regex_pattern, string_to_split, flags=re.S)


# https://realpython.com/python-encodings-guide/
# print(unicodedata.name('😂'))
# print(unicodedata.lookup('FACE WITH TEARS OF JOY'))
