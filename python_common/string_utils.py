import re


def split_string_by_regex(regex, string):
    return list(filter(None, re.split(regex, string)))
