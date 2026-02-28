# test_serverplex.py
"""
Tests for ServerPlex module.
"""

import unittest
from serverplex import ServerPlex

class TestServerPlex(unittest.TestCase):
    """Test cases for ServerPlex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ServerPlex()
        self.assertIsInstance(instance, ServerPlex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ServerPlex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
