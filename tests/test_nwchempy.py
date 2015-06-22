#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_nwchempy
----------------------------------

Tests for `nwchempy` module.
"""

import unittest

#from nwchempy import nwchempy
from nwchempy.nwchempy import NWChem, NWChemFreq

nwc = NWChem('./data/butan-1-ol')

class TestNwchempy(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


def test_init():
    assert isinstance(nwc.nwo, str)
    assert 'CITATION' in nwc.nwo


def test_get_freq():
    nwc = NWChemFreq('./data/butan-1-ol')
    f = nwc.get_freq()
    assert f.any()
