import unittest
import portscan
from simpleservers import SimpleServers

class TestScan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.servers = SimpleServers(50000, 50001, 50002, 50003, 50004)
        cls.servers.start()
        
    @classmethod
    def tearDownClass(cls):
        cls.servers.stop()
        
    def testShouldNotAllowSmallerEndPort(self):
        with self.assertRaises(ValueError):
            portscan.scan('127.0.0.1', 5000, 4999)
            
    def testShouldNotAllowMuchSmallerEndPort(self):
        with self.assertRaises(ValueError):
            portscan.scan('127.0.0.1', 5000, 1)
            
    def testStartPortOnlyIsOpen(self):
        result = portscan.scan('127.0.0.1', 50000)
        expected = {50000: True}
        self.assertEqual(expected, result)
        
    def testStartPortOnlyIsNotOpen(self):
        result = portscan.scan('127.0.0.1', 50005)
        expected = {50005: False}
        self.assertEqual(expected, result)
        
    def testStartAndEndPortIsOpenSizeTwo(self):
        result = portscan.scan('127.0.0.1', 50000, 50001)
        expected = {50000: True, 50001: True}
        self.assertEqual(expected, result)
        
    def testStartAndEndPortIsOpenSizeThree(self):
        result = portscan.scan('127.0.0.1', 50000, 50002)
        expected = {50000: True, 50001: True, 50002: True}
        self.assertEqual(expected, result)
        
    def testStartAndEndPortIsOpenSizeFour(self):
        result = portscan.scan('127.0.0.1', 50000, 50003)
        expected = {50000: True, 50001: True, 50002: True, 50003: True}
        self.assertEqual(expected, result)
        
    def testStartAndEndPortIsOpenSizeFive(self):
        result = portscan.scan('127.0.0.1', 50000, 50004)
        expected = {50000: True, 50001: True, 50002: True, 50003: True, 50004: True}
        self.assertEqual(expected, result)
        
    def testStartAndEndPortIsOpenSizeSixWithOneNotOpen(self):
        result = portscan.scan('127.0.0.1', 50000, 50005)
        expected = {50000: True, 50001: True, 50002: True, 50003: True, 50004: True, 50005: False}
        self.assertEqual(expected, result)
        
    def testStartAndEndPortHalfOpenHalfClosed(self):
        result = portscan.scan('127.0.0.1', 50000, 50010)
        expected = {50000: True, 50001: True, 50002: True, 50003: True, 50004: True, 50005: False, 50006: False, 50007: False, 50008: False, 50009: False, 50010: False}
        self.assertEqual(expected, result)

