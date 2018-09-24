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

If there are any `key=value` pairs in the "extensions" section (and face it, pretty much every CEF record has these), they'll also be in the dict, with the dict key name the same as the CEF record's key name.

## Example Usage
    >>> import pycef
    >>> cef = 'CEF:0|pycef|python CEF tests|1|2|Test event 1|3| field1=value1 field2=value2 field3=value3'
    >>> d = pycef.parse(cef)
    >>> d
    {'DeviceVendor': 'pycef', 'DeviceProduct': 'python CEF tests', 'DeviceVersion': '1', 'DeviceEventClassID': '2', 'DeviceName': 'Test event 1', 'DeviceSeverity': '3', 'CEFVersion': '0', 'field1': 'value1', 'field2': 'value2', 'field3': 'value3'}
