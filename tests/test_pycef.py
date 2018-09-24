#!/usr/bin/env python

import pycef
import json
from unittest import TestCase

LINE1_REF = dict(DeviceName="Test event 1", field1="value1", field2="value2", field3="value3", DeviceVendor="pycef", CEFVersion="0", DeviceSeverity="3", DeviceEventClassID="2", DeviceProduct="python CEF tests", DeviceVersion="1")
LINE2_REF = dict(DeviceName="Test event 2", field6="value6", DeviceVendor="pycef", field4="value4", field5="value5", CEFVersion="0", DeviceSeverity="6", DeviceEventClassID="5", DeviceProduct="python CEF tests", DeviceVersion="4")
LINE3_REF = dict(DeviceName="Test event 3", field8="value8", field9="value9", DeviceVendor="pycef", CEFVersion="0", DeviceSeverity="9", DeviceEventClassID="8", DeviceProduct="python CEF tests", DeviceVersion="7")

REFERENCE_DATA = [LINE3_REF, LINE2_REF, LINE1_REF]

class TestPyCEF(TestCase):
    def test(self):
        with open("tests/testdata.cef", "r") as f:
            for l in f.readlines():
                d = pycef.parse(l)
                d_ref = REFERENCE_DATA.pop()
                self.assertDictEqual(d, d_ref)
