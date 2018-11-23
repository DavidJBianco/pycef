#!/usr/bin/env python

import pycef
import json
from unittest import TestCase

LINE1_REF = dict(DeviceName="Test pipe event 1", field1="value1", field2="value2|more", field3="value3", DeviceVendor="pycef", CEFVersion="0", DeviceSeverity="3", DeviceEventClassID="2", DeviceProduct="python CEF tests", DeviceVersion="1")

REFERENCE_DATA = [LINE1_REF]

class TestPyCEFPipes(TestCase):
    def test_pipes(self):
        '''
        Test to ensure that embedded pipe symbols in the values don't interfere
        with parsing the CEF record.
        '''
        with open("tests/testdata-pipes.cef", "r") as f:
            for l in f.readlines():
                d = pycef.parse(l)
                d_ref = REFERENCE_DATA.pop()
                self.assertDictEqual(d, d_ref)
