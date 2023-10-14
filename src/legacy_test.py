#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import legacy

class LegacyTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_reload(self):
        import sys

        _sys = sys
        sys = legacy.reload(sys)
        self.assertEqual(sys, _sys)
        self.assertEqual(id(sys), id(_sys))
