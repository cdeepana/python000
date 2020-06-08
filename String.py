from django.template.defaultfilters import upper, lower

name = "chathura deepana"
StrLen = len(name)  # len for character count
print(StrLen)
print(upper(name))
print(lower(name))
title = "your grade is {}".format(25)
print(title)
str = "first string{}".format(" hi second {}".format("third one"))  # concatenation
print(str)