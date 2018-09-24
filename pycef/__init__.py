#!/usr/bin/env python

from __future__ import print_function

import re

def parse(str_input):
    """
    Parse a string in CEF format and return a dict with the header values
    and the extension data.
    """

    # Create the empty dict we'll return later
    values = dict()

    # This regex separates the string into the CEF header and the extension
    # data.  Once we do this, it's easier to use other regexes to parse each
    # part.
    header_re = r'((^CEF:\d+)([^=\\]+\|){,7})(.*)'

    res = re.search(header_re, str_input)
    if res:
        header = res.group(1)
        extension = res.group(4)

        # Split the header on the "|" char.  Uses a negative lookbehind
        # assertion to ensure we don't accidentally split on escaped chars,
        # though.
        spl = re.split(r'(?<!\\)\|', header)

        # Since these values are set by their position in the header, it's
        # easy to know which is which.
        values["DeviceVendor"] = spl[1]
        values["DeviceProduct"] = spl[2]
        values["DeviceVersion"] = spl[3]
        values["DeviceEventClassID"] = spl[4]
        values["DeviceName"] = spl[5]
        if len(spl) > 6:
            values["DeviceSeverity"] = spl[6]

        # The first value is actually the CEF version, formatted like
        # "CEF:#".  Ignore anything before that (like a date from a syslog message).
        # We then split on the colon and use the second value as the
        # version number.
        cef_start = spl[0].find('CEF')
        if cef_start == -1:
            return None
        (cef, version) = spl[0][cef_start:].split(':')
        values["CEFVersion"] = version

        # The ugly, gnarly regex here finds a single key=value pair,
        # taking into account multiple whitespaces, escaped '=' and '|'
        # chars.  It returns an iterator of tuples.
        spl = re.findall(r'([^=\s]+)=((?:[\\]=|[^=])+)(?:\s|$)', extension)
        for i in spl:
            # Split the tuples and put them into the dictionary
            values[i[0]] = i[1]

        # Process custom field labels
        for key in list(values.keys()):
            # If the key string ends with Label, replace it in the appropriate
            # custom field
            if key[-5:] == "Label":
                customlabel = key[:-5]
                # Find the corresponding customfield and replace with the label
                for customfield in list(values.keys()):
                    if customfield == customlabel:
                        values[values[key]] = values[customfield]
                        del values[customfield]
                        del values[key]

    # Now we're done!
    return values

###### Main ######
if __name__ == "__main__":

    import sys
    import json

    if len(sys.argv) != 2:
        print("USAGE: %s <file>" % sys.argv[0])
        sys.exit(-1)

    file = sys.argv[1]

    for line in open(file, "r").readlines():
        line = line.rstrip('\n')

        # Read the file, and parse each line of CEF into a separate JSON
        # document to stdout
        try:
            values = parse(line)
        except (TypeError, ValueError) as e:
            sys.stderr.write('{0} parsing line:\n{1}\n'.format(e.message, line))
        else:
            if values:
                print(json.dumps(values))
