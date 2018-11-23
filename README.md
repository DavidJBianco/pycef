# pycef
A very simple CEF parser for Python 2/3

I originally wrote this because I wasn't able to find very many good Python CEF parsers out there.  I did find [one by Sooshie](https://github.com/sooshie/cef_parser) that got me started (thanks for sharing, sir!), but I elected to produce my own.  

The `parse` function takes a string containing a single CEF record and returns a dict containing the following keys, as defined in the [CEF format documentation](https://www.protect724.hpe.com/docs/DOC-1072):

* CEFVersion
* DeviceVendor
* DeviceVersion
* DeviceEventClassID
* DeviceName
* DeviceSeverity

If there are any `key=value` pairs in the "extensions" section (and face it, pretty much every CEF record has these), they'll also be in the dict, with the dict key name the same as the CEF record's key name. If it could not recognize any CEF data, the `parse` function will return `None`.


## Example Usage
Parsing a well-formatted CEF record

    >>> import pycef
    >>> cef = 'CEF:0|pycef|python CEF tests|1|2|Test event 1|3| field1=value1 field2=value2 field3=value3'
    >>> d = pycef.parse(cef)
    >>> d
    {'DeviceVendor': 'pycef', 'DeviceProduct': 'python CEF tests', 'DeviceVersion': '1', 'DeviceEventClassID': '2', 'DeviceName': 'Test event 1', 'DeviceSeverity': '3', 'CEFVersion': '0', 'field1': 'value1', 'field2': 'value2', 'field3': 'value3'}

Parsing a line of CEF from a source with header junk at the front (NOTE: this isn't specific to syslog headers as in the example. The parser just starts wherever 'CEF:0' is found):

    >>> import pycef
    >>> cef_syslog = 'Nov 16 21:24:18 arcsightfwd.davidbianco.io CEF:0|pycef|python CEF tests|1|2|Test event 1|3| field1=value1 field2=value2 field3=value3'
    >>> d = pycef.parse(cef_syslog)
    >>> d
    {'DeviceVendor': 'pycef', 'DeviceProduct': 'python CEF tests', 'DeviceVersion': '1', 'DeviceEventClassID': '2', 'DeviceName': 'Test event 1', 'DeviceSeverity': '3', 'CEFVersion': '0', 'field1': 'value1', 'field2': 'value2', 'field3': 'value3'}

## Logging
`Pycef` uses the standard Python `logging` module.  By default, you will not see any logs, but you can easily configure them within your own application.  Here's an example:

    import logging

    # We log with the name 'pycef'
    logger = logging.getLogger('pycef')

    # set log level to DEBUG to get the most verbose output
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # well-formatted CEF data will log the parsed values at DEBUG level
    cef = 'CEF:0|pycef|python CEF tests|1|2|Test event 1|3| field1=value1 field2=value2 field3=value3'
    d = pycef.parse(cef)
    2018-11-23 08:49:39,827 - pycef - DEBUG - Returning values: {'DeviceVendor': 'pycef', 'DeviceProduct': 'python CEF tests', 'DeviceVersion': '1', 'DeviceEventClassID': '2', 'DeviceName': 'Test event 1', 'DeviceSeverity': '3', 'CEFVersion': '0', 'field1': 'value1', 'field2': 'value2', 'field3': 'value3'}

    # Parse errors in the data will log at WARNING level
    pycef.parse('kjlk')
    2018-11-23 08:47:42,853 - pycef - WARNING - Could not parse record. Is it valid CEF format?
