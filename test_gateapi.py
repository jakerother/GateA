# test_gateapi.py
"""
Tests for GateAPI module.
"""

import unittest
from gateapi import GateAPI

class TestGateAPI(unittest.TestCase):
    """Test cases for GateAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GateAPI()
        self.assertIsInstance(instance, GateAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GateAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
