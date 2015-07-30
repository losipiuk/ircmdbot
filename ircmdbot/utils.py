import re


def whitespace_split(string, maxsplit=0):
    return re.compile('\s+').split(string, maxsplit)
