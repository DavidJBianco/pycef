#!/usr/bin/env python

import pycef
import json
from unittest import TestCase

CEF1_REF = dict(DeviceName="Test event 1", field1="value1", field2="value2", field3="value3", DeviceVendor="pycef", CEFVersion="0", DeviceSeverity="3", DeviceEventClassID="2", DeviceProduct="python CEF tests", DeviceVersion="1")
CEF2_REF = dict(DeviceName="Test event 2", field6="value6", DeviceVendor="pycef", field4="value4", field5="value5", CEFVersion="0", DeviceSeverity="6", DeviceEventClassID="5", DeviceProduct="python CEF tests", DeviceVersion="4")
CEF3_REF = dict(DeviceName="Test event 3", field8="value8", field9="value9", DeviceVendor="pycef", CEFVersion="0", DeviceSeverity="9", DeviceEventClassID="8", DeviceProduct="python CEF tests", DeviceVersion="7")
CEF4_REF = None
CEF_REFERENCE_DATA = [CEF4_REF, CEF3_REF, CEF2_REF, CEF1_REF]

SYSLOG1_REF = dict(DeviceName="Test event 1", field1="value1", field2="value2", field3="value3", DeviceVendor="pycef", CEFVersion="0", DeviceSeverity="3", DeviceEventClassID="2", DeviceProduct="python CEF tests", DeviceVersion="1")
SYSLOG_REFERENCE_DATA = [SYSLOG1_REF]

class TestPyCEF(TestCase):
    def test_cef_format(self):
        '''
        Test cases for properly formatted CEF samples.
        '''
        with open("tests/testdata.cef", "r") as f:
            for l in f.readlines():
                d = pycef.parse(l)
                d_ref = CEF_REFERENCE_DATA.pop()
                self.assertDictEqual(d, d_ref)

    def test_syslog_format(self):
        '''
        Test cases for syslog-formatted CEF samples (i.e., with syslog header
        junk at the beginning of each line)
        '''
        with open("tests/testdata-syslog.txt", "r") as f:
            for l in f.readlines():
                d = pycef.parse(l)
                d_ref = SYSLOG_REFERENCE_DATA.pop()
                self.assertDictEqual(d, d_ref)
