# pycef
A very simple CEF parser for Python

I originally wrote this because I wasn't able to find very many good Python CEF parsers out there.  I did find [one by Sooshie](https://github.com/sooshie/cef_parser) that got me started (thanks for sharing, sir!), but I elected to produce my own.  

The `cef_parse` function takes a string containing a single CEF record and returns a dict containing the following keys, as defined in the [CEF format documentation](https://www.protect724.hpe.com/docs/DOC-1072):

* CEFVersion
* DeviceVendor
* DeviceVersion
* DeviceEventClassID
* DeviceName
* DeviceSeverity

If there are any `key=value` pairs in the "extensions" section (and face it, pretty much every CEF record has these), they'll also be in the dict, with the dict key name the same as the CEF record's key name.

