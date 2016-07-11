#!/usr/bin/env python

import sys
import re
import json

def cef_parse(str):

    values = dict()

    header_re = r'(.*(?<!\\)\|){,7}(.*)'
    
    res = re.search(header_re, str)
    if res:
        header = res.group(1)
        extension = res.group(2)

        spl = re.split(r'(?<!\\)\|', header)

        values["DeviceVendor"] = spl[1]
        values["DeviceProduct"] = spl[2]
        values["DeviceVersion"] = spl[3]
        values["DeviceEventClassID"] = spl[4]
        values["DeviceName"] = spl[5]
        values["DeviceSeverity"] = spl[6]
        

        (cef, version) = spl[0].split(':')
        values["CEFVersion"] = version
        
        spl = re.findall(r'([^=\s]+)=((?:[\\]=|[^=])+)(?:\s|$)', extension)
        for i in spl:
            values[i[0]] = i[1]

    return     values

###### Main ######
if len(sys.argv) != 2:
    print "USAGE: %s <file>" % sys.argv[0]
    sys.exit(-1)

file = sys.argv[1]

for line in open(file, "r").readlines():
    line = line.rstrip('\n')
    print line

    values = cef_parse(line)
    print json.dumps(values)

