import re

document = "https://docs.python.org/3/library/re.html",'https://docs.python.org/3/howto/regex.html#regex-howto'

# ^ Matches the beginning of a line
assert re.findall('^a','asas ndmdb') == ['a']
assert re.findall('^a','sasndmdb') == []

# $ Matches the end of the line
assert re.findall('end$','sm,bds end') == ['end']
assert re.findall('end$','sas end ndmdb') == []

# . Matches any character
assert re.findall('a.','any character') == ['an', 'ar', 'ac']

# \s Matches whitespace
assert re.findall('\s','''any character
secondline\ttab\r''') == [' ', '\n', '\t', '\r']

# \S Matches any non-whitespace character
assert re.findall('e\S','''any character\nsecondline\ttab''') == ['er', 'ec']

# ? match 0 or 1 repetitions of the preceding RE
assert re.findall('ab?','''a , ab both''') == ['a', 'ab']

# * Repeats a character zero or more times
assert re.findall('asa*','asaaz ndmasadba') == ['asaa', 'asa']

# *? Repeats a character zero or more times (non-greedy)
assert re.findall('asa*?','asaaz ndmasadba') == ['as','as']

# + Repeats a character one or more times
assert re.findall('asa+','asaaz ndmasadba') == ['asaa', 'asa']

# +? Repeats a character one or more times (non-greedy)
assert re.findall('asa+?','asaaz ndmasadba') == ['asa', 'asa']

# [aeiou] Matches a single character in the listed set
assert re.findall('[aeiou]','this will return all the vowels imn this text') == ['i', 'i', 'e', 'u', 'a', 'e', 'o', 'e', 'i', 'i', 'e']

# [^XYZ] Matches a single character not in the listed set
assert re.findall('[^ansd]','asaaz ndmasadba') == ['z', ' ', 'm', 'b']

# [a-z0-9]	The set of characters can include a range
assert re.findall('[a-z0-9]','text number 1.') == ['t', 'e', 'x', 't', 'n', 'u', 'm', 'b', 'e', 'r', '1']

# {m} Matches exactly m copies of the previous RE
assert re.findall('a{3}','matches aaa but not aa') == ['aaa']

# {m,n} Matches m to n repetitions copies of the previous RE
assert re.findall('a{3,5}','matches aaa,aaaa,aaaaa, aaaaaaa but not aa') == ['aaa', 'aaaa', 'aaaaa', 'aaaaa']
assert re.findall('a{3,5}','matches aaa,aaaa,aaaaa, aaaaaaaa 5+3 but not aa') == ['aaa', 'aaaa', 'aaaaa', 'aaaaa', 'aaa']

# {m,n}? Matches m to n repetitions copies of the previous RE (non-greedy)
assert re.findall('a{3,5}?','matches aaa,aaaa,aaaaa, aaaaaaa but not aa') == ['aaa', 'aaa', 'aaa', 'aaa', 'aaa']
assert re.findall('a{3,5}?','matches aaa,aaaa,aaaaa, aaaaaaaaa 3+3+3 but not aa') == ['aaa', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa']

# A|B regular expression that will match either A or B.
assert re.findall('[a-z]{3}|[0-9]{3}','abc & 091 bt nt ny1') == ['abc', '091']

# using re.sub(pattern, repl, string, count=0, flags=0)
def dashrepl(matchobj):
    if matchobj.group(0) == '-': return ' '
    else: return '-'

assert re.sub('-{1,2}', dashrepl, 'pro----gram-files') == 'pro--gram files'
assert re.sub('x*', '-', 'abc') == '-a-b-c-'
assert re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE) == 'Baked Beans & Spam'

# using re.subn(pattern, repl, string, count=0, flags=0)
assert re.subn('-{1,2}', dashrepl, 'pro----gram-files') == ('pro--gram files', 3)
assert re.subn('x*', '-', 'abc') == ('-a-b-c-', 4)
assert re.subn(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE) == ('Baked Beans & Spam', 1)

# using re.escape
assert re.escape("abcdefghijklmnopqrstuvwxyz0123456789!#$%&'*+-.^_`|~:") == "abcdefghijklmnopqrstuvwxyz0123456789\\!\\#\\$\\%\\&\\'\\*\\+\\-\\.\\^\\_\\`\\|\\~\\:"

# Using re.split(pattern, string, maxsplit=0, flags=0)
assert re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE) == ['0', '3', '9']
assert re.split(r'\W+', 'Words, words, words.words', 1) == ['Words', 'words, words.words']
assert re.split(r'\W+', 'Words, words, words.words') == ['Words', 'words', 'words', 'words']
assert re.split(r'(\W+)', '...words, words...') == ['', '...', 'words', ', ', 'words', '...', '']
assert re.split('x*', 'axbc') == ['a', 'bc'] # it should return ['', 'a', 'b', 'c', ''].
#                                       split() doesn't currently split a string on an empty pattern match

# re.purge() Clear the regular expression cache.
