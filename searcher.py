# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = ur"(\b(?:[A-Z]){2,}\s)(\(.*?\))"

f = open("sample.txt","r")
newf = open("output.txt","w")
acronyms = {

}
for line in f:

    input_str = line

    matches = re.finditer(regex, input_str, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
  
        if match.group(1) not in acronyms.keys():
            acronyms[match.group(1)] = match.group(2)
            newf.write(str(match.group(1)) + " " + str(match.group(2))+"\n")

